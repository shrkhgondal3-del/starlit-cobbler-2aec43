#!/usr/bin/env python3
"""
Generate voiceover MP3s via ElevenLabs API (agent-automated).

Requires environment variable: ELEVENLABS_API_KEY

Usage:
  export ELEVENLABS_API_KEY=sk_...
  python elevenlabs_generate.py \\
    --voice-id EXAVITQu4vr4xnSDxMaL \\
    --input-dir output/01-foreigners-buy-property-ksa/voiceover_chapters \\
    --output-dir projects/01-foreigners-buy-property-ksa/voiceover
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

try:
    import urllib.request
    import json
except ImportError:
    pass

API_URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"


def generate_mp3(text: str, voice_id: str, api_key: str, out: Path) -> None:
    payload = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.65,
            "similarity_boost": 0.80,
            "style": 0.10,
            "use_speaker_boost": True,
        },
    }).encode("utf-8")

    req = urllib.request.Request(
        API_URL.format(voice_id=voice_id),
        data=payload,
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        out.write_bytes(resp.read())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--voice-id", required=True, help="ElevenLabs voice or clone ID")
    parser.add_argument("--input-dir", type=Path, required=True, help="Chapter .txt files")
    parser.add_argument("--output-dir", type=Path, required=True, help="Output .mp3 dir")
    args = parser.parse_args()

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: Set ELEVENLABS_API_KEY environment variable", file=sys.stderr)
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)
    chapters = sorted(args.input_dir.glob("*.txt"))
    if not chapters:
        print(f"ERROR: No .txt files in {args.input_dir}", file=sys.stderr)
        return 1

    for txt in chapters:
        # Map chapter txt names to manifest mp3 names
        name = txt.stem + ".mp3"
        out = args.output_dir / name
        text = txt.read_text(encoding="utf-8").strip()
        if not text:
            continue
        print(f"  Generating {out.name} ({len(text)} chars)...")
        generate_mp3(text, args.voice_id, api_key, out)

    print(f"✓ {len(chapters)} MP3s → {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
