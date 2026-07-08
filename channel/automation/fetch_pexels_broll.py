#!/usr/bin/env python3
"""Download B-roll from Pexels API (free — alternative to Higgsfield)."""

from __future__ import annotations

import json
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import api_config

CHAPTER_QUERIES: dict[str, list[str]] = {
    "chapter-1": ["riyadh skyline", "saudi arabia city", "real estate building", "government building"],
    "chapter-2": ["business meeting middle east", "gcc business", "corporate office", "handshake business"],
    "chapter-3": ["luxury apartment", "residency visa", "modern villa", "investment property"],
    "chapter-4": ["construction development", "coastal city aerial", "masterplan city", "luxury resort"],
    "chapter-5": ["corporate office", "business registration", "commercial building", "boardroom"],
    "chapter-6": ["signing contract", "property keys", "real estate agent", "document review"],
    "chapter-7": ["bank building", "mortgage documents", "financial district", "calculator finance"],
    "chapter-8": ["business mistake", "legal documents", "checklist office", "consultation meeting"],
}


def pexels_search(query: str, api_key: str) -> str | None:
    q = urllib.parse.quote(query)
    url = f"https://api.pexels.com/videos/search?query={q}&per_page=3&orientation=landscape"
    req = urllib.request.Request(url, headers={"Authorization": api_key})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode())
    for video in data.get("videos", []):
        files = sorted(
            [f for f in video.get("video_files", []) if f.get("width", 0) >= 1280],
            key=lambda f: f.get("width", 0),
            reverse=True,
        )
        if files:
            return files[0]["link"]
    return None


def download(url: str, dest: Path) -> bool:
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(url, headers={"User-Agent": "SaudiGateway/1.0"})
        with urllib.request.urlopen(req, timeout=120) as resp:
            dest.write_bytes(resp.read())
        return dest.stat().st_size > 50000
    except Exception as e:
        print(f"  Failed {dest.name}: {e}")
        return False


def normalize_clip(src: Path, dest: Path) -> None:
    subprocess.run(
        [
            "ffmpeg", "-y", "-i", str(src),
            "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30",
            "-c:v", "libx264", "-preset", "fast", "-crf", "20", "-an",
            str(dest),
        ],
        check=True,
        capture_output=True,
    )


def main() -> int:
    api_key = api_config.get("PEXELS_API_KEY")
    if not api_key:
        print("PEXELS_API_KEY not set — get free key at https://www.pexels.com/api/", file=sys.stderr)
        return 1

    project = Path(__file__).parent / "projects/01-foreigners-buy-property-ksa"
    for chapter, queries in CHAPTER_QUERIES.items():
        out_dir = project / "broll" / chapter
        out_dir.mkdir(parents=True, exist_ok=True)
        idx = 0
        for query in queries:
            if idx >= 4:
                break
            dest = out_dir / f"clip_{idx:02d}.mp4"
            if dest.exists() and dest.stat().st_size > 50000:
                idx += 1
                continue
            print(f"→ {chapter}: {query}")
            url = pexels_search(query, api_key)
            if not url:
                continue
            tmp = out_dir / f"_tmp_{idx}.mp4"
            if download(url, tmp):
                normalize_clip(tmp, dest)
                tmp.unlink(missing_ok=True)
                print(f"  ✓ clip_{idx:02d}.mp4")
                idx += 1
        print(f"✓ {chapter}: {idx} clips")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
