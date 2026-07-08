#!/usr/bin/env python3
"""
Generate Charlotte Hayes avatar clips via HeyGen API v3.

Requires:
  HEYGEN_API_KEY     — https://app.heygen.com/settings?nav=API
  HEYGEN_AVATAR_ID   — photo avatar look ID (required for v3 avatar videos)

Usage:
  python3 setup_api_keys.py          # diagnose keys first
  python heygen_generate.py --project projects/01-foreigners-buy-property-ksa
  python heygen_generate.py --project ... --force
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import api_config

API_BASE = "https://api.heygen.com"

AVATAR_SEGMENTS: list[dict] = [
    {
        "output": "avatar/hook.mp4",
        "title": "hook",
        "script": (
            "If you've heard that foreigners can't buy property in Saudi Arabia — "
            "you're working with outdated information. In 2026, the rules have changed significantly. "
            "I'm Charlotte Hayes from Saudi Gateway. This channel uses AI-assisted production. "
            "Over the next fifteen minutes I'll walk you through who can buy, where, what it costs, "
            "and the mistakes that catch foreign buyers off guard."
        ),
    },
    {
        "output": "avatar/bridge-ch3.mp4",
        "title": "bridge-ch3",
        "script": (
            "For many non-GCC foreigners, Premium Residency is the most important pathway. "
            "Here's how it works."
        ),
    },
    {
        "output": "avatar/bridge-ch4.mp4",
        "title": "bridge-ch4",
        "script": (
            "Without Premium Residency, designated development zones are the practical route. "
            "Here is what to verify on every project."
        ),
    },
    {
        "output": "avatar/myth-emphasis.mp4",
        "title": "myth-emphasis",
        "script": (
            "Five mistakes I see constantly. Assuming Dubai rules apply here — they don't. "
            "Skipping REGA verification. Buying off-plan without escrow confirmation. "
            "Overlooking Premium Residency. And proceeding without a Saudi property lawyer."
        ),
    },
    {
        "output": "avatar/close.mp4",
        "title": "close",
        "script": (
            "Saudi Arabia's property market for foreigners is real, growing, and regulated. "
            "Download our free Foreign Buyer's Property Checklist — link in the description. "
            "Subscribe for next week's guide. I'm Charlotte Hayes. See you on Saudi Gateway."
        ),
    },
]

MIN_HEYGEN_BYTES = 1_500_000  # real HeyGen exports are usually >1.5 MB


def api_key() -> str:
    key = api_config.get("HEYGEN_API_KEY")
    if not key:
        raise RuntimeError(
            "HEYGEN_API_KEY not set. Run: python3 setup_api_keys.py\n"
            "Get key: https://app.heygen.com/settings?nav=API"
        )
    return key


def verify_key() -> None:
    req = urllib.request.Request(
        f"{API_BASE}/v1/user/me",
        headers={"X-Api-Key": api_key()},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode())
            if data.get("code") != 100:
                raise RuntimeError(f"HeyGen key invalid: {data}")
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:200]
        raise RuntimeError(
            f"HeyGen 401 — key is invalid. Regenerate at app.heygen.com/settings?nav=API\n{body}"
        ) from e


def api_request(method: str, path: str, body: dict | None = None) -> dict:
    headers = {"X-Api-Key": api_key(), "Content-Type": "application/json"}
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(f"{API_BASE}{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode()[:500]
        raise RuntimeError(f"HeyGen API {path} failed HTTP {e.code}: {err}") from e


def create_avatar_video(script: str, avatar_id: str, title: str) -> str:
    payload = {
        "type": "avatar",
        "avatar_id": avatar_id,
        "script": script,
        "title": f"Saudi Gateway — {title}",
        "resolution": "1080p",
        "aspect_ratio": "16:9",
    }
    voice_id = api_config.get("HEYGEN_VOICE_ID")
    if voice_id:
        payload["voice_id"] = voice_id

    resp = api_request("POST", "/v3/videos", payload)
    video_id = resp.get("data", {}).get("video_id")
    if not video_id:
        raise RuntimeError(f"No video_id: {resp}")
    print(f"  Video ID: {video_id}")
    return video_id


def wait_for_video_url(video_id: str, timeout_sec: int = 900) -> str:
    deadline = time.time() + timeout_sec
    while time.time() < deadline:
        video = api_request("GET", f"/v3/videos/{video_id}").get("data", {})
        status = video.get("status")
        if status == "completed":
            url = video.get("video_url")
            if url:
                return url
            raise RuntimeError(f"Completed but no video_url: {video}")
        if status == "failed":
            raise RuntimeError(
                f"HeyGen render failed: {video.get('error')} — {video.get('message')}"
            )
        time.sleep(15)
    raise RuntimeError(f"Timed out waiting for video {video_id}")


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "SaudiGateway/1.0"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        dest.write_bytes(resp.read())


def generate_segment(project: Path, spec: dict, avatar_id: str, force: bool) -> None:
    out = project / spec["output"]
    if out.exists() and out.stat().st_size >= MIN_HEYGEN_BYTES and not force:
        print(f"  Skip (HeyGen export exists): {spec['output']}")
        return
    if out.exists() and not force:
        print(f"  Replacing fallback/small file: {spec['output']}")

    print(f"→ Generating {spec['output']}...")
    video_id = create_avatar_video(spec["script"], avatar_id, spec["title"])
    video_url = wait_for_video_url(video_id)
    download(video_url, out)
    print(f"✓ {spec['output']} ({out.stat().st_size // 1024} KB)")


def main() -> int:
    parser = argparse.ArgumentParser(description="HeyGen avatar clip generation (v3 API)")
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--force", action="store_true", help="Regenerate even if files exist")
    args = parser.parse_args()

    api_config.load_env_files()
    try:
        verify_key()
    except RuntimeError as e:
        print(f"✗ {e}", file=sys.stderr)
        print("\nRun: python3 setup_api_keys.py", file=sys.stderr)
        return 1

    project = args.project.resolve()
    avatar_id = api_config.get("HEYGEN_AVATAR_ID")
    if not avatar_id:
        print("✗ HEYGEN_AVATAR_ID required for v3 avatar videos.", file=sys.stderr)
        print("  1. HeyGen → Avatars → Photo Avatar → Create Charlotte Hayes", file=sys.stderr)
        print("  2. Copy Avatar/Look ID → add to Secrets as HEYGEN_AVATAR_ID", file=sys.stderr)
        return 1

    for spec in AVATAR_SEGMENTS:
        try:
            generate_segment(project, spec, avatar_id, args.force)
        except Exception as e:
            print(f"✗ {spec['output']}: {e}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
