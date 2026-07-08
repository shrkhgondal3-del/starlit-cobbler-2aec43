#!/usr/bin/env python3
"""
Generate B-roll clips via Higgsfield Platform API (proper setup — no MCP).

Requires:
  HIGGSFIELD_API_KEY
  HIGGSFIELD_API_SECRET
  Get keys: https://platform.higgsfield.ai

Usage:
  python higgsfield_generate.py --project projects/01-foreigners-buy-property-ksa
  python higgsfield_generate.py --project ... --chapter chapter-1 --limit 2
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

API_BASE = "https://platform.higgsfield.ai"
# Kling text-to-video — adjust model if your plan exposes different endpoints
VIDEO_ENDPOINT = "/v1/text2video/kling-v2-1-master"


def credentials() -> str:
    key = os.environ.get("HIGGSFIELD_API_KEY", "").strip()
    secret = os.environ.get("HIGGSFIELD_API_SECRET", "").strip()
    if not key or not secret:
        raise RuntimeError(
            "HIGGSFIELD_API_KEY and HIGGSFIELD_API_SECRET required. "
            "Add at https://cursor.com/dashboard/cloud-agents → Secrets"
        )
    return f"Key {key}:{secret}"


def api_post(path: str, body: dict) -> dict:
    data = json.dumps(body).encode()
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=data,
        headers={"Authorization": credentials(), "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode()[:500]
        raise RuntimeError(f"Higgsfield {path} HTTP {e.code}: {err}") from e


def api_get(path: str) -> dict:
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        headers={"Authorization": credentials()},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode()[:500]
        raise RuntimeError(f"Higgsfield GET {path} HTTP {e.code}: {err}") from e


def chapter_folder(chapter: str) -> str:
    """Map shotlist chapter id to broll/chapter-N folder."""
    m = re.search(r"chapter-(\d+)", chapter)
    if m:
        return f"chapter-{m.group(1)}"
    if chapter.startswith("hook"):
        return "chapter-1"
    return "chapter-1"


def poll_request(request_id: str, timeout_sec: int = 600) -> str:
    deadline = time.time() + timeout_sec
    while time.time() < deadline:
        resp = api_get(f"/requests/{request_id}/status")
        status = resp.get("status") or resp.get("data", {}).get("status")
        if status in ("completed", "succeeded", "success"):
            url = (
                resp.get("video_url")
                or resp.get("output_url")
                or resp.get("data", {}).get("video_url")
                or resp.get("data", {}).get("output", {}).get("url")
            )
            if url:
                return url
            results = resp.get("results") or resp.get("data", {}).get("results") or []
            if results and isinstance(results[0], dict):
                url = results[0].get("url") or results[0].get("video_url")
                if url:
                    return url
            raise RuntimeError(f"Completed but no URL in response: {resp}")
        if status in ("failed", "error"):
            raise RuntimeError(f"Higgsfield job failed: {resp}")
        time.sleep(8)
    raise RuntimeError(f"Timed out polling request {request_id}")


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "SaudiGateway/1.0"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        dest.write_bytes(resp.read())


def generate_clip(prompt: str, dest: Path) -> None:
    if dest.exists() and dest.stat().st_size > 50000:
        print(f"  Skip (exists): {dest.name}")
        return

    body = {
        "prompt": prompt,
        "duration": 5,
        "aspect_ratio": "16:9",
    }
    resp = api_post(VIDEO_ENDPOINT, body)
    request_id = (
        resp.get("request_id")
        or resp.get("id")
        or resp.get("data", {}).get("request_id")
        or resp.get("data", {}).get("id")
    )
    if not request_id:
        raise RuntimeError(f"No request_id: {resp}")

    print(f"  Job {request_id} — polling...")
    video_url = poll_request(request_id)
    download(video_url, dest)
    print(f"✓ {dest} ({dest.stat().st_size // 1024} KB)")


def load_shotlist(prep_dir: Path) -> list[dict]:
    path = prep_dir / "broll_shotlist.json"
    if not path.exists():
        raise FileNotFoundError(f"Missing {path} — run prepare_video.py first")
    data = json.loads(path.read_text(encoding="utf-8"))
    return [s for s in data.get("scenes", []) if s.get("type") == "video"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Higgsfield B-roll generation")
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--prep-dir", type=Path, default=None)
    parser.add_argument("--chapter", type=str, default=None, help="e.g. chapter-1")
    parser.add_argument("--limit", type=int, default=4, help="Max clips per chapter")
    args = parser.parse_args()

    project = args.project.resolve()
    prep = args.prep_dir or (Path(__file__).parent / "output/01-foreigners-buy-property-ksa")
    scenes = load_shotlist(prep)

    by_chapter: dict[str, list[dict]] = {}
    for scene in scenes:
        folder = chapter_folder(scene.get("chapter", ""))
        by_chapter.setdefault(folder, []).append(scene)

    targets = [args.chapter] if args.chapter else sorted(by_chapter.keys())
    for ch in targets:
        items = by_chapter.get(ch, [])[: args.limit]
        if not items:
            print(f"No scenes for {ch}", file=sys.stderr)
            continue
        out_dir = project / "broll" / ch
        for i, scene in enumerate(items):
            prompt = scene.get("ai_prompt", "Saudi Arabia modern city cinematic documentary 4K")
            dest = out_dir / f"clip_{i:02d}.mp4"
            try:
                print(f"→ {ch}/clip_{i:02d}.mp4")
                generate_clip(prompt, dest)
            except Exception as e:
                print(f"✗ {dest}: {e}", file=sys.stderr)
                return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
