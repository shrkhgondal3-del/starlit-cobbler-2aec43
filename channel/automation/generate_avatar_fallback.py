#!/usr/bin/env python3
"""Generate avatar segment using voiceover audio + branded still (HeyGen fallback)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

W, H = 1920, 1080


def make_avatar_segment(
    audio_mp3: Path,
    output_mp4: Path,
    title: str = "Charlotte Hayes",
    subtitle: str = "Saudi Gateway",
) -> None:
    output_mp4.parent.mkdir(parents=True, exist_ok=True)
    dur = subprocess.check_output(
        [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(audio_mp3),
        ],
        text=True,
    ).strip()

    safe_title = title.replace(":", "\\:").replace("'", "\\'")
    safe_sub = subtitle.replace(":", "\\:").replace("'", "\\'")

    vf = (
        f"color=c=0x0D1B2A:s={W}x{H}:d={dur},"
        f"drawtext=text='{safe_title}':fontcolor=0xC5A572:fontsize=56:"
        f"x=(w-text_w)/2:y=(h/2)-80,"
        f"drawtext=text='{safe_sub}':fontcolor=white:fontsize=36:"
        f"x=(w-text_w)/2:y=(h/2),"
        f"drawtext=text='AI Presenter':fontcolor=0x888888:fontsize=24:"
        f"x=(w-text_w)/2:y=(h/2)+60"
    )

    subprocess.run(
        [
            "ffmpeg", "-y", "-f", "lavfi", "-i", vf, "-i", str(audio_mp3),
            "-c:v", "libx264", "-preset", "fast", "-crf", "20",
            "-c:a", "aac", "-b:a", "192k", "-shortest",
            str(output_mp4),
        ],
        check=True,
        capture_output=True,
    )


def main() -> int:
    project = Path(__file__).parent / "projects/01-foreigners-buy-property-ksa"
    vo = project / "voiceover"

    segments = [
        ("hook-hook.mp3", "avatar/hook.mp4"),
        ("chapter-3-premium-residency-route.mp3", "avatar/bridge-ch3.mp4", 8.0),
        ("chapter-4-designated-zones-developer-projects.mp3", "avatar/bridge-ch4.mp4", 8.0),
        ("chapter-8-common-mistakes.mp3", "avatar/myth-emphasis.mp4", 15.0),
        ("close-close.mp3", "avatar/close.mp4"),
    ]

    for item in segments:
        audio_name = item[0]
        out_rel = item[1]
        trim = item[2] if len(item) > 2 else None
        audio = vo / audio_name
        out = project / out_rel
        if not audio.exists():
            print(f"Skip missing {audio}", file=sys.stderr)
            continue
        if trim:
            trimmed = out.parent / f"_trim_{audio_name.replace('.mp3', '.mp3')}"
            subprocess.run(
                ["ffmpeg", "-y", "-i", str(audio), "-t", str(trim), "-c", "copy", str(trimmed)],
                check=True, capture_output=True,
            )
            make_avatar_segment(trimmed, out)
            trimmed.unlink(missing_ok=True)
        else:
            make_avatar_segment(audio, out)
        print(f"✓ {out_rel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
