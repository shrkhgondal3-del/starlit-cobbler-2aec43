#!/usr/bin/env python3
"""
Generate assembly_manifest.json for automated FFmpeg video assembly.

Usage:
  python generate_manifest.py \\
    --avatar-script ../content/scripts/01-foreigners-buy-property-ksa-AVATAR.md \\
    --prep-dir output/01-foreigners-buy-property-ksa \\
    --project-dir projects/01-foreigners-buy-property-ksa
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

# Timeline for video 01 — avatar + voiceover chapter mapping
VIDEO_01_TIMELINE = [
    {"type": "avatar", "file": "avatar/hook.mp4"},
    {"type": "broll_vo", "audio": "voiceover/chapter-1-the-old-rule-vs-todays-reality.mp3",
     "broll_dir": "broll/chapter-1", "chapter_id": "chapter-1"},
    {"type": "broll_vo", "audio": "voiceover/chapter-2-gcc-nationals.mp3",
     "broll_dir": "broll/chapter-2", "chapter_id": "chapter-2"},
    {"type": "avatar", "file": "avatar/bridge-ch3.mp4"},
    {"type": "broll_vo", "audio": "voiceover/chapter-3-premium-residency-route.mp3",
     "broll_dir": "broll/chapter-3", "chapter_id": "chapter-3"},
    {"type": "avatar", "file": "avatar/bridge-ch4.mp4"},
    {"type": "broll_vo", "audio": "voiceover/chapter-4-designated-zones-developer-projects.mp3",
     "broll_dir": "broll/chapter-4", "chapter_id": "chapter-4"},
    {"type": "broll_vo", "audio": "voiceover/chapter-5-buying-through-a-saudi-company.mp3",
     "broll_dir": "broll/chapter-5", "chapter_id": "chapter-5"},
    {"type": "broll_vo", "audio": "voiceover/chapter-6-the-purchase-process-step-by-step.mp3",
     "broll_dir": "broll/chapter-6", "chapter_id": "chapter-6"},
    {"type": "avatar", "file": "avatar/myth-emphasis.mp4"},
    {"type": "broll_vo", "audio": "voiceover/chapter-7-financing-mortgages.mp3",
     "broll_dir": "broll/chapter-7", "chapter_id": "chapter-7"},
    {"type": "broll_vo", "audio": "voiceover/chapter-8-common-mistakes.mp3",
     "broll_dir": "broll/chapter-8", "chapter_id": "chapter-8"},
    {"type": "avatar", "file": "avatar/close.mp4"},
]

VIDEO_REGISTRY: dict[str, list[dict]] = {
    "01-foreigners-buy-property-ksa": VIDEO_01_TIMELINE,
}


def build_manifest(video_id: str, title: str, prep_dir: Path | None) -> dict:
    segments = VIDEO_REGISTRY.get(video_id)
    if not segments:
        raise ValueError(f"No timeline registered for video_id={video_id}")

    chapters_meta = []
    if prep_dir and (prep_dir / "voiceover_chapters").exists():
        for txt in sorted((prep_dir / "voiceover_chapters").glob("*.txt")):
            chapters_meta.append({"id": txt.stem, "text_file": str(txt)})

    return {
        "video_id": video_id,
        "title": title,
        "resolution": [1920, 1080],
        "fps": 30,
        "clip_duration_target_sec": 5.5,
        "music": {
            "file": "assets/music/background.mp3",
            "volume": 0.07,
            "optional": True,
        },
        "disclaimer_overlay": {
            "text": "AI-assisted production · Educational only · Not legal advice",
            "duration_sec": 3,
            "optional": True,
        },
        "segments": segments,
        "chapters_meta": chapters_meta,
        "output": {
            "video": "output/final.mp4",
            "subtitles": "output/subtitles.srt",
            "chapters": "output/chapters.txt",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--video-id", default="01-foreigners-buy-property-ksa")
    parser.add_argument("--title", default="Can Foreigners Buy Property in Saudi Arabia? (2026)")
    parser.add_argument("--prep-dir", type=Path, default=None)
    parser.add_argument("--project-dir", type=Path, required=True)
    args = parser.parse_args()

    project = args.project_dir.resolve()
    project.mkdir(parents=True, exist_ok=True)

    for sub in ["avatar", "voiceover", "broll", "assets/music", "output"]:
        (project / sub).mkdir(parents=True, exist_ok=True)
    for i in range(1, 9):
        (project / "broll" / f"chapter-{i}").mkdir(parents=True, exist_ok=True)

    manifest = build_manifest(args.video_id, args.title, args.prep_dir)
    out = project / "assembly_manifest.json"
    out.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"✓ Manifest written: {out}")
    print(f"  Segments: {len(manifest['segments'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
