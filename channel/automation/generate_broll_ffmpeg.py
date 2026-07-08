#!/usr/bin/env python3
"""Generate branded documentary B-roll clips via FFmpeg (no external APIs)."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

W, H = 1920, 1080
FPS = 30
DURATION = 5.5

# Saudi Gateway palette
NAVY = "0x0D1B2A"
GOLD = "0xC5A572"
GREEN = "0x006C35"
WHITE = "white"

CHAPTER_CLIPS: dict[str, list[tuple[str, str]]] = {
    "chapter-1": [
        ("Riyadh Skyline", f"gradients=navy-gold"),
        ("Property Law Reform", "legal-documents"),
        ("Foreign Ownership", "global-investors"),
        ("Saudi Vision 2030", "modern-development"),
    ],
    "chapter-2": [
        ("GCC Nationals", "gcc-region"),
        ("Equal Rights", "property-deed"),
        ("Residency Benefits", "residential-tower"),
        ("Investment Access", "business-district"),
    ],
    "chapter-3": [
        ("Premium Residency", "visa-premium"),
        ("SAR 4M Threshold", "luxury-property"),
        ("Property Requirement", "villa-exterior"),
        ("Long-term Stay", "family-home"),
    ],
    "chapter-4": [
        ("Designated Zones", "masterplan-aerial"),
        ("NEOM & Red Sea", "mega-project"),
        ("Developer Projects", "construction-site"),
        ("Freehold Zones", "coastal-development"),
    ],
    "chapter-5": [
        ("Saudi Company Route", "corporate-office"),
        ("Commercial Registration", "business-license"),
        ("Land Ownership", "commercial-plot"),
        ("Corporate Structure", "boardroom"),
    ],
    "chapter-6": [
        ("Purchase Process", "signing-contract"),
        ("REGA Registration", "government-building"),
        ("Due Diligence", "property-inspection"),
        ("Title Transfer", "keys-handover"),
    ],
    "chapter-7": [
        ("Mortgage Options", "bank-building"),
        ("Saudi Banks", "financial-district"),
        ("Financing Rules", "calculator-documents"),
        ("Investment Returns", "growth-chart"),
    ],
    "chapter-8": [
        ("Common Mistakes", "warning-review"),
        ("Legal Compliance", "law-books"),
        ("Due Diligence Tips", "checklist"),
        ("Expert Guidance", "consultation"),
    ],
}

GRADIENTS = [
    f"color=c={NAVY}:s={W}x{H}:d={DURATION}",
    f"color=c={NAVY}:s={W}x{H}:d={DURATION}",
    f"color=c=0x1B2838:s={W}x{H}:d={DURATION}",
    f"color=c=0x0A1628:s={W}x{H}:d={DURATION}",
]


def safe_text(text: str) -> str:
    return text.replace(":", "\\:").replace("'", "\\'")


def make_clip(output: Path, title: str, subtitle: str, grad_idx: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    base = GRADIENTS[grad_idx % len(GRADIENTS)]
    safe_title = safe_text(title)
    safe_sub = safe_text(subtitle)

    # Subtle zoom + gold accent bar + chapter label
    vf = (
        f"{base},"
        f"zoompan=z='min(zoom+0.0008,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
        f"d={int(DURATION * FPS)}:s={W}x{H}:fps={FPS},"
        f"drawbox=x=0:y=ih-6:w=iw:h=6:color={GOLD}:t=fill,"
        f"drawbox=x=0:y=0:w=iw:h=4:color={GREEN}:t=fill,"
        f"drawtext=text='SAUDI GATEWAY':fontcolor={GOLD}:fontsize=28:"
        f"x=60:y=50,"
        f"drawtext=text='{safe_title}':fontcolor={WHITE}:fontsize=52:"
        f"x=(w-text_w)/2:y=(h/2)-40,"
        f"drawtext=text='{safe_sub}':fontcolor=0xAAAAAA:fontsize=32:"
        f"x=(w-text_w)/2:y=(h/2)+30"
    )

    subprocess.run(
        [
            "ffmpeg", "-y", "-f", "lavfi", "-i", vf,
            "-c:v", "libx264", "-preset", "fast", "-crf", "20",
            "-t", str(DURATION), "-r", str(FPS), "-an",
            str(output),
        ],
        check=True,
        capture_output=True,
    )


def main() -> int:
    project = Path(__file__).parent / "projects/01-foreigners-buy-property-ksa"
    for chapter, clips in CHAPTER_CLIPS.items():
        out_dir = project / "broll" / chapter
        for i, (title, tag) in enumerate(clips):
            out = out_dir / f"clip_{i:02d}.mp4"
            subtitle = tag.replace("-", " ").title()
            make_clip(out, title, subtitle, i)
            print(f"✓ {chapter}/clip_{i:02d}.mp4 — {title}")

    log = project / "broll" / "generation_log.json"
    log.write_text(json.dumps({"source": "ffmpeg-branded", "chapters": list(CHAPTER_CLIPS)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
