#!/usr/bin/env python3
"""
Generate Charlotte Hayes avatar clips via HeyGen API (proper setup — no MCP).

Requires:
  HEYGEN_API_KEY          — https://app.heygen.com/settings/api
  HEYGEN_AVATAR_ID        — optional; uses Video Agent if unset

Usage:
  python heygen_generate.py --project projects/01-foreigners-buy-property-ksa
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

API_BASE = "https://api.heygen.com"

AVATAR_SEGMENTS: list[dict] = [
    {
        "output": "avatar/hook.mp4",
        "prompt": (
            "16:9 video. Charlotte Hayes, glamorous professional British female presenter, "
            "modest dress, studio background navy and gold. Composed direct delivery. "
            "She says: If you've heard that foreigners can't buy property in Saudi Arabia — "
            "you're working with outdated information. In 2026, the rules have changed significantly. "
            "I'm Charlotte Hayes from Saudi Gateway. This channel uses AI-assisted production. "
            "Over the next fifteen minutes I'll walk you through who can buy, where, what it costs, "
            "and the mistakes that catch foreign buyers off guard."
        ),
    },
    {
        "output": "avatar/bridge-ch3.mp4",
        "prompt": (
            "16:9, 8 seconds. Charlotte Hayes, British female presenter, modest professional. "
            "Calm authority. She says: For many non-GCC foreigners, Premium Residency is the "
            "most important pathway. Here's how it works."
        ),
    },
    {
        "output": "avatar/bridge-ch4.mp4",
        "prompt": (
            "16:9, 8 seconds. Charlotte Hayes, British female presenter. "
            "She says: Without Premium Residency, designated development zones are the practical route. "
            "Here is what to verify on every project."
        ),
    },
    {
        "output": "avatar/myth-emphasis.mp4",
        "prompt": (
            "16:9, 15 seconds. Charlotte Hayes, firmer pace, still composed. "
            "She says: Five mistakes I see constantly. Assuming Dubai rules apply here — they don't. "
            "Skipping REGA verification. Buying off-plan without escrow confirmation. "
            "Overlooking Premium Residency. And proceeding without a Saudi property lawyer."
        ),
    },
    {
        "output": "avatar/close.mp4",
        "prompt": (
            "16:9. Charlotte Hayes, warm professional close. "
            "She says: Saudi Arabia's property market for foreigners is real, growing, and regulated. "
            "Download our free Foreign Buyer's Property Checklist — link in the description. "
            "Subscribe for next week's guide. I'm Charlotte Hayes. See you on Saudi Gateway."
        ),
    },
]


def api_key() -> str:
    key = os.environ.get("HEYGEN_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "HEYGEN_API_KEY not set. Add at https://cursor.com/dashboard/cloud-agents → Secrets"
        )
    return key


def api_request(method: str, path: str, body: dict | None = None) -> dict:
    headers = {"X-Api-Key": api_key(), "Content-Type": "application/json"}
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(f"{API_BASE}{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode()[:500]
        raise RuntimeError(f"HeyGen API {path} failed HTTP {e.code}: {err}") from e


def create_video_agent(prompt: str, avatar_id: str | None) -> str:
    payload: dict = {"prompt": prompt}
    if avatar_id:
        payload["avatar_id"] = avatar_id
    resp = api_request("POST", "/v3/video-agents", payload)
    session_id = resp.get("data", {}).get("session_id")
    if not session_id:
        raise RuntimeError(f"No session_id in response: {resp}")
    print(f"  Session: https://app.heygen.com/video-agent/{session_id}")
    return session_id


def wait_for_video_url(session_id: str, timeout_sec: int = 900) -> str:
    deadline = time.time() + timeout_sec
    video_id = None
    while time.time() < deadline:
        sess = api_request("GET", f"/v3/video-agents/{session_id}").get("data", {})
        video_id = sess.get("video_id") or video_id
        if video_id:
            break
        time.sleep(5)

    if not video_id:
        raise RuntimeError(f"Timed out waiting for video_id on session {session_id}")

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
                f"HeyGen render failed: {video.get('failure_code')} — {video.get('failure_message')}"
            )
        time.sleep(10)

    raise RuntimeError(f"Timed out waiting for video {video_id}")


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "SaudiGateway/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        dest.write_bytes(resp.read())


def generate_segment(project: Path, spec: dict, avatar_id: str | None) -> None:
    out = project / spec["output"]
    if out.exists() and out.stat().st_size > 50000:
        print(f"  Skip (exists): {spec['output']}")
        return
    print(f"→ Generating {spec['output']}...")
    session_id = create_video_agent(spec["prompt"], avatar_id)
    video_url = wait_for_video_url(session_id)
    download(video_url, out)
    print(f"✓ {spec['output']} ({out.stat().st_size // 1024} KB)")


def main() -> int:
    parser = argparse.ArgumentParser(description="HeyGen avatar clip generation")
    parser.add_argument("--project", type=Path, required=True)
    args = parser.parse_args()
    project = args.project.resolve()
    avatar_id = os.environ.get("HEYGEN_AVATAR_ID", "").strip() or None

    if not avatar_id:
        print("Note: HEYGEN_AVATAR_ID not set — using Video Agent auto avatar.", file=sys.stderr)
        print("For Charlotte Hayes: train photo avatar in HeyGen, add HEYGEN_AVATAR_ID to secrets.\n")

    for spec in AVATAR_SEGMENTS:
        try:
            generate_segment(project, spec, avatar_id)
        except Exception as e:
            print(f"✗ {spec['output']}: {e}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
