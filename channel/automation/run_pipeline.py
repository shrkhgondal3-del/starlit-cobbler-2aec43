#!/usr/bin/env python3
"""
End-to-end Saudi Gateway video pipeline (agent-operated, no CapCut).

Steps:
  1. prepare_video.py      — script → voiceover text + shot list
  2. generate_manifest.py  — timeline manifest
  3. [API]                 — ElevenLabs, HeyGen, Higgsfield (see SIMPLE-API-SETUP.md)
  4. assemble_video.py     — FFmpeg final MP4

Usage:
  python run_pipeline.py check
  python run_pipeline.py prepare --script ../content/scripts/01-foreigners-buy-property-ksa.md
  python run_pipeline.py manifest --video-id 01-foreigners-buy-property-ksa
  python run_pipeline.py generate-api --project projects/01-foreigners-buy-property-ksa
  python run_pipeline.py assemble --project projects/01-foreigners-buy-property-ksa
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PROJECTS = ROOT / "projects"


def run_py(script: str, args: list[str]) -> int:
    cmd = [sys.executable, str(ROOT / script)] + args
    print(f"\n→ {' '.join(cmd)}\n")
    return subprocess.call(cmd)


def main() -> int:
    parser = argparse.ArgumentParser(description="Saudi Gateway video pipeline")
    sub = parser.add_subparsers(dest="command", required=True)

    p_prep = sub.add_parser("prepare", help="Script → voiceover + shot list")
    p_prep.add_argument("--script", type=Path, required=True)

    p_man = sub.add_parser("manifest", help="Create assembly manifest + folders")
    p_man.add_argument("--video-id", default="01-foreigners-buy-property-ksa")
    p_man.add_argument("--title", default="Can Foreigners Buy Property in Saudi Arabia? (2026)")

    p_asm = sub.add_parser("assemble", help="FFmpeg assemble final video")
    p_asm.add_argument("--project", type=Path, required=True)
    p_asm.add_argument("--allow-placeholders", action="store_true")

    p_chk = sub.add_parser("check", help="Verify API keys (ElevenLabs, HeyGen, Higgsfield)")
    p_gen = sub.add_parser("generate-api", help="HeyGen avatars + Higgsfield B-roll via API")
    p_gen.add_argument("--project", type=Path, required=True)

    p_all = sub.add_parser("init", help="prepare + manifest for a new video")
    p_all.add_argument("--script", type=Path, required=True)
    p_all.add_argument("--video-id", default=None)

    args = parser.parse_args()

    if args.command == "prepare":
        return run_py("prepare_video.py", [str(args.script.resolve())])

    if args.command == "manifest":
        video_id = args.video_id
        prep = ROOT / "output" / video_id
        project = PROJECTS / video_id
        return run_py("generate_manifest.py", [
            "--video-id", video_id,
            "--title", args.title,
            "--prep-dir", str(prep),
            "--project-dir", str(project),
        ])

    if args.command == "assemble":
        asm_args = ["--project", str(args.project.resolve())]
        if args.allow_placeholders:
            asm_args.append("--allow-placeholders")
        return run_py("assemble_video.py", asm_args)

    if args.command == "check":
        return run_py("check_setup.py", [])

    if args.command == "generate-api":
        project = str(args.project.resolve())
        if run_py("heygen_generate.py", ["--project", project]) != 0:
            return 1
        return run_py("higgsfield_generate.py", ["--project", project])

    if args.command == "init":
        script = args.script.resolve()
        video_id = args.video_id or script.stem
        if run_py("prepare_video.py", [str(script)]) != 0:
            return 1
        prep = ROOT / "output" / video_id
        project = PROJECTS / video_id
        return run_py("generate_manifest.py", [
            "--video-id", video_id,
            "--prep-dir", str(prep),
            "--project-dir", str(project),
        ])

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
