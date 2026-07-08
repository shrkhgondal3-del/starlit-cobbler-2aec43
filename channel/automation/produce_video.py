#!/usr/bin/env python3
"""
Produce Saudi Gateway Video 01 with ZERO manual steps.

Works without HeyGen/Higgsfield/MCP. Uses API keys only when available.

Usage:
  cd channel/automation
  python3 produce_video.py
  python3 produce_video.py --video-id 01-foreigners-buy-property-ksa
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import api_config

ROOT = Path(__file__).parent
SCRIPT = ROOT.parent / "content/scripts/01-foreigners-buy-property-ksa.md"
VOICE_ID = "Xb7hH8MSUJpSbSDYk0k2"
DEFAULT_VIDEO = "01-foreigners-buy-property-ksa"


def run(cmd: list[str]) -> int:
    print(f"\n→ {' '.join(cmd)}\n")
    return subprocess.call(cmd)


def has_clips(broll_dir: Path) -> bool:
    return broll_dir.exists() and any(broll_dir.glob("*.mp4"))


def main() -> int:
    parser = argparse.ArgumentParser(description="One-command Video 01 production")
    parser.add_argument("--video-id", default=DEFAULT_VIDEO)
    parser.add_argument("--allow-placeholders", action="store_true")
    parser.add_argument("--premium", action="store_true", help="Require HeyGen + B-roll APIs")
    args = parser.parse_args()

    api_config.load_env_files()
    project = ROOT / "projects" / args.video_id
    prep = ROOT / "output" / args.video_id

    print("=" * 60)
    print("Saudi Gateway — produce_video.py")
    print("No API keys required. Premium APIs used when available.")
    print("=" * 60)

    # 1. Import user files from incoming/ if present
    incoming = ROOT / "incoming"
    if incoming.exists() and any(incoming.iterdir()):
        print("\n[1/7] Importing files from incoming/ …")
        code = run([
            sys.executable, str(ROOT / "import_downloads.py"),
            "--downloads", str(incoming),
            "--project", str(project),
            "--whisper",
        ])
        if code != 0:
            print("  (incoming import partial — continuing with automation)")

    # 2. Init project structure
    print("\n[2/7] Preparing script + manifest …")
    if run([sys.executable, str(ROOT / "run_pipeline.py"), "init", "--script", str(SCRIPT)]) != 0:
        return 1

    # 3. Voiceovers — ElevenLabs if key set, else keep existing
    print("\n[3/7] Voiceovers …")
    if api_config.elevenlabs_configured():
        run([
            sys.executable, str(ROOT / "elevenlabs_generate.py"),
            "--voice-id", api_config.get("ELEVENLABS_VOICE_ID", VOICE_ID),
            "--input-dir", str(prep / "voiceover_chapters"),
            "--output-dir", str(project / "voiceover"),
        ])
    else:
        print("  ELEVENLABS_API_KEY not set — using existing voiceover/*.mp3 if present")

    # 4. Avatars — HeyGen v3 API if valid, else fallback
    print("\n[4/7] Avatar clips …")
    if api_config.heygen_configured() and api_config.get("HEYGEN_AVATAR_ID"):
        if run([sys.executable, str(ROOT / "heygen_generate.py"), "--project", str(project)]) != 0:
            print("  HeyGen failed — using avatar fallback")
            run([sys.executable, str(ROOT / "generate_avatar_fallback.py")])
    else:
        if api_config.heygen_configured():
            print("  HeyGen key set but HEYGEN_AVATAR_ID missing — fallback")
        run([sys.executable, str(ROOT / "generate_avatar_fallback.py")])

    # 5. B-roll — Higgsfield → Pexels → Mixkit → FFmpeg
    print("\n[5/7] B-roll …")
    if api_config.higgsfield_configured():
        run([sys.executable, str(ROOT / "higgsfield_generate.py"), "--project", str(project)])
    if api_config.pexels_configured():
        run([sys.executable, str(ROOT / "fetch_pexels_broll.py")])
    run([sys.executable, str(ROOT / "fetch_stock_broll.py")])

    from generate_broll_ffmpeg import CHAPTER_CLIPS, make_clip
    for ch in CHAPTER_CLIPS:
        broll_dir = project / "broll" / ch
        if not has_clips(broll_dir):
            for i, (title, tag) in enumerate(CHAPTER_CLIPS[ch]):
                out = broll_dir / f"clip_{i:02d}.mp4"
                make_clip(out, title, tag.replace("-", " ").title(), i)
                print(f"  ✓ generated {ch}/clip_{i:02d}.mp4")

    # 6. Assemble
    print("\n[6/7] Assembling final video …")
    asm = [sys.executable, str(ROOT / "assemble_video.py"), "--project", str(project)]
    if args.allow_placeholders:
        asm.append("--allow-placeholders")
    if run(asm) != 0:
        return 1

    # 7. Copy to deliverables
    print("\n[7/7] Copying to deliverables …")
    deliver = ROOT.parent / "deliverables/video-01"
    deliver.mkdir(parents=True, exist_ok=True)
    out = project / "output"
    for name in ("final.mp4", "subtitles.srt", "chapters.txt"):
        src = out / name
        if src.exists():
            (deliver / name).write_bytes(src.read_bytes())
            print(f"  ✓ deliverables/video-01/{name}")

    final = deliver / "final.mp4"
    if final.exists():
        dur = subprocess.check_output(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(final)],
            text=True,
        ).strip()
        print(f"\n✓ DONE — {final}")
        print(f"  Duration: {float(dur)/60:.1f} minutes")
        print(f"  GitHub:   see channel/deliverables/VIDEO-LINK.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
