#!/usr/bin/env python3
"""
Import user-produced assets from ~/Downloads into a Video 01 project folder.

Expected in Downloads:
  - 5 HeyGen avatar MP4s: hook.mp4, bridge-ch3.mp4, bridge-ch4.mp4, myth-emphasis.mp4, close.mp4
  - 10 ElevenLabs voiceover MP3s (generic filenames)
  - 1 ZIP with ~15 Higgsfield B-roll MP4 clips

Usage:
  python3 import_downloads.py --project projects/01-foreigners-buy-property-ksa
  python3 import_downloads.py --downloads /path/to/Downloads --project ...
"""

from __future__ import annotations

import argparse
import difflib
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
PREP = ROOT / "output/01-foreigners-buy-property-ksa/voiceover_chapters"

CHAPTER_MP3_NAMES = [
    "chapter-1-the-old-rule-vs-todays-reality.mp3",
    "chapter-2-gcc-nationals.mp3",
    "chapter-3-premium-residency-route.mp3",
    "chapter-4-designated-zones-developer-projects.mp3",
    "chapter-5-buying-through-a-saudi-company.mp3",
    "chapter-6-the-purchase-process-step-by-step.mp3",
    "chapter-7-financing-mortgages.mp3",
    "chapter-8-common-mistakes.mp3",
]

AVATAR_NAMES = ["hook.mp4", "bridge-ch3.mp4", "bridge-ch4.mp4", "myth-emphasis.mp4", "close.mp4"]

# Keywords to route Higgsfield clips into chapter folders (filename or path hints)
CHAPTER_HINTS: dict[str, list[str]] = {
    "chapter-1": ["chapter-1", "chapter1", "ch1", "old-rule", "todays-reality", "vision-2030", "flowchart", "pathway"],
    "chapter-2": ["chapter-2", "chapter2", "ch2", "gcc", "gulf"],
    "chapter-3": ["chapter-3", "chapter3", "ch3", "premium", "residency", "iqama"],
    "chapter-4": ["chapter-4", "chapter4", "ch4", "designated", "zone", "developer", "neom", "diriyah", "red-sea"],
}


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower().strip())


def load_reference_texts() -> dict[str, str]:
    refs: dict[str, str] = {}
    for mp3_name in CHAPTER_MP3_NAMES:
        stem = mp3_name.replace(".mp3", "")
        txt = PREP / f"{stem}.txt"
        if txt.exists():
            refs[mp3_name] = normalize_text(txt.read_text(encoding="utf-8"))
    return refs


def transcribe_mp3(path: Path) -> str:
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        raise RuntimeError("faster-whisper not installed — pip install faster-whisper")

    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(path), language="en")
    return normalize_text(" ".join(s.text for s in segments))


def match_mp3_to_chapter(path: Path, refs: dict[str, str], use_whisper: bool) -> str | None:
    if use_whisper:
        try:
            transcript = transcribe_mp3(path)
        except Exception as e:
            print(f"  Whisper failed for {path.name}: {e}", file=sys.stderr)
            transcript = ""
    else:
        transcript = ""

    best_name = None
    best_score = 0.0
    for mp3_name, ref in refs.items():
        if transcript:
            score = difflib.SequenceMatcher(None, transcript[:400], ref[:400]).ratio()
        else:
            score = 0.0
        if score > best_score:
            best_score = score
            best_name = mp3_name

    if best_score >= 0.35:
        return best_name
    return None


def guess_chapter_from_name(name: str) -> str | None:
    low = name.lower()
    for chapter, hints in CHAPTER_HINTS.items():
        if any(h in low for h in hints):
            return chapter
    return None


def import_avatars(downloads: Path, project: Path) -> int:
    dest = project / "avatar"
    dest.mkdir(parents=True, exist_ok=True)
    count = 0
    for name in AVATAR_NAMES:
        src = downloads / name
        if not src.exists():
            print(f"  Missing avatar: {name}")
            continue
        shutil.copy2(src, dest / name)
        print(f"  ✓ avatar/{name}")
        count += 1
    return count


def import_voiceovers(downloads: Path, project: Path, use_whisper: bool) -> int:
    dest = project / "voiceover"
    dest.mkdir(parents=True, exist_ok=True)
    refs = load_reference_texts()
    mp3s = sorted(downloads.glob("*.mp3"))
    if not mp3s:
        print("  No MP3 files in Downloads")
        return 0

    assigned: dict[str, Path] = {}
    for mp3 in mp3s:
        match = match_mp3_to_chapter(mp3, refs, use_whisper)
        if match and match not in assigned:
            assigned[match] = mp3
            print(f"  ✓ {mp3.name} → {match}" + ("" if use_whisper else " (whisper off — low confidence)"))

    for mp3_name, src in assigned.items():
        shutil.copy2(src, dest / mp3_name)

    # hook / close MP3s intentionally not copied — avatar clips carry that audio
    skipped = len(mp3s) - len(assigned)
    if skipped:
        print(f"  ({skipped} MP3(s) unused — likely hook/close or unmatched)")
    return len(assigned)


def import_broll_zip(downloads: Path, project: Path) -> int:
    zips = sorted(downloads.glob("*.zip"))
    if not zips:
        print("  No ZIP in Downloads")
        return 0

    zip_path = zips[0]
    extract_dir = downloads / ".broll_extract"
    if extract_dir.exists():
        shutil.rmtree(extract_dir)
    extract_dir.mkdir()

    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(extract_dir)

    clips = sorted(extract_dir.rglob("*.mp4"))
    if not clips:
        print(f"  No MP4 inside {zip_path.name}")
        return 0

    # Clear chapters 1-4 only; leave 5-8 empty per workflow
    for i in range(1, 5):
        ch_dir = project / "broll" / f"chapter-{i}"
        if ch_dir.exists():
            for old in ch_dir.glob("*.mp4"):
                old.unlink()
        else:
            ch_dir.mkdir(parents=True)

    for i in range(5, 9):
        ch_dir = project / "broll" / f"chapter-{i}"
        if ch_dir.exists():
            for old in ch_dir.glob("*.mp4"):
                old.unlink()

    buckets: dict[str, list[Path]] = {f"chapter-{i}": [] for i in range(1, 5)}
    unassigned: list[Path] = []

    for clip in clips:
        hint = guess_chapter_from_name(clip.name) or guess_chapter_from_name(str(clip.parent.name))
        if hint and len(buckets[hint]) < 4:
            buckets[hint].append(clip)
        else:
            unassigned.append(clip)

    # Distribute leftovers round-robin up to 4 per chapter
    for clip in unassigned:
        for ch in buckets:
            if len(buckets[ch]) < 4:
                buckets[ch].append(clip)
                break

    total = 0
    for ch, items in buckets.items():
        out_dir = project / "broll" / ch
        for i, src in enumerate(items[:4]):
            dest = out_dir / f"clip_{i:02d}.mp4"
            shutil.copy2(src, dest)
            total += 1
        print(f"  ✓ {ch}: {min(len(items), 4)} clips")

    return total


def main() -> int:
    parser = argparse.ArgumentParser(description="Import Downloads assets into Video 01 project")
    parser.add_argument("--downloads", type=Path, default=Path.home() / "Downloads")
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--whisper", action="store_true", help="Transcribe MP3s to match chapters")
    args = parser.parse_args()

    downloads = args.downloads.resolve()
    project = args.project.resolve()

    print(f"Downloads: {downloads}")
    print(f"Project:   {project}\n")

    if not downloads.exists():
        print(f"ERROR: Downloads folder not found: {downloads}", file=sys.stderr)
        return 1

    contents = list(downloads.iterdir())
    if not contents:
        print("WARNING: Downloads folder is empty — upload assets and re-run.", file=sys.stderr)

    print("→ Avatars")
    avatars = import_avatars(downloads, project)
    print(f"  {avatars}/5 avatar clips\n")

    print("→ Voiceovers (8 chapter MP3s)")
    vos = import_voiceovers(downloads, project, args.whisper)
    print(f"  {vos}/8 chapter voiceovers\n")

    print("→ B-roll ZIP")
    broll = import_broll_zip(downloads, project)
    print(f"  {broll} broll clips in chapters 1-4\n")

    if avatars == 0 and vos == 0 and broll == 0:
        print("No new assets imported.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
