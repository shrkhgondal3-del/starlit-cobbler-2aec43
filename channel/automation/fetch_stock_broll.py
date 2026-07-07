#!/usr/bin/env python3
"""Download free stock B-roll for Saudi Gateway chapters (no Higgsfield required)."""

from __future__ import annotations

import json
import subprocess
import urllib.request
from pathlib import Path

# Free Mixkit CDN clips (commercial use allowed per Mixkit license)
STOCK_LIBRARY: dict[str, list[str]] = {
    "riyadh": [
        "https://assets.mixkit.co/videos/preview/mixkit-night-view-of-a-city-with-lights-4151-large.mp4",
        "https://assets.mixkit.co/videos/preview/mixkit-aerial-panorama-of-a-city-4150-large.mp4",
    ],
    "property": [
        "https://assets.mixkit.co/videos/preview/mixkit-modern-building-under-a-blue-sky-4069-large.mp4",
        "https://assets.mixkit.co/videos/preview/mixkit-panoramic-view-of-a-modern-building-4068-large.mp4",
    ],
    "rega": [
        "https://assets.mixkit.co/videos/preview/mixkit-businessman-signing-a-contract-4845-large.mp4",
        "https://assets.mixkit.co/videos/preview/mixkit-man-working-on-his-laptop-308-large.mp4",
    ],
    "misa": [
        "https://assets.mixkit.co/videos/preview/mixkit-man-having-a-video-call-on-his-laptop-3080-large.mp4",
        "https://assets.mixkit.co/videos/preview/mixkit-person-working-on-a-laptop-4908-large.mp4",
    ],
    "boardroom": [
        "https://assets.mixkit.co/videos/preview/mixkit-business-people-in-a-meeting-4608-large.mp4",
        "https://assets.mixkit.co/videos/preview/mixkit-businessman-in-a-meeting-4607-large.mp4",
    ],
    "desert": [
        "https://assets.mixkit.co/videos/preview/mixkit-aerial-view-of-a-desert-landscape-4248-large.mp4",
        "https://assets.mixkit.co/videos/preview/mixkit-sand-dunes-in-the-desert-4247-large.mp4",
    ],
    "default": [
        "https://assets.mixkit.co/videos/preview/mixkit-city-traffic-at-night-4389-large.mp4",
        "https://assets.mixkit.co/videos/preview/mixkit-people-walking-in-the-city-4378-large.mp4",
    ],
}

CHAPTER_KEYWORDS: dict[str, list[str]] = {
    "chapter-1": ["riyadh", "rega", "property", "default"],
    "chapter-2": ["boardroom", "default"],
    "chapter-3": ["property", "desert", "default"],
    "chapter-4": ["property", "desert", "default"],
    "chapter-5": ["boardroom", "misa", "default"],
    "chapter-6": ["rega", "misa", "default"],
    "chapter-7": ["property", "boardroom", "default"],
    "chapter-8": ["rega", "default"],
}


def download(url: str, dest: Path) -> bool:
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and dest.stat().st_size > 10000:
            return True
        print(f"  Downloading {dest.name}...")
        urllib.request.urlretrieve(url, dest)
        return dest.exists() and dest.stat().st_size > 1000
    except Exception as e:
        print(f"  Failed {dest.name}: {e}")
        return False


def main() -> int:
    project = Path(__file__).parent / "projects/01-foreigners-buy-property-ksa"
    for chapter, keywords in CHAPTER_KEYWORDS.items():
        out_dir = project / "broll" / chapter
        out_dir.mkdir(parents=True, exist_ok=True)
        idx = 0
        for kw in keywords:
            for url in STOCK_LIBRARY.get(kw, STOCK_LIBRARY["default"]):
                dest = out_dir / f"clip_{idx:02d}.mp4"
                if download(url, dest):
                    idx += 1
                if idx >= 4:
                    break
            if idx >= 4:
                break
        print(f"✓ {chapter}: {idx} clips")

    manifest_path = project / "broll" / "download_log.json"
    manifest_path.write_text(json.dumps({"source": "mixkit", "chapters": CHAPTER_KEYWORDS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
