#!/usr/bin/env python3
"""
Saudi Gateway — Automated video assembly (no CapCut required).

Stitches avatar clips + B-roll + voiceover into a final YouTube-ready MP4.
Runs entirely via FFmpeg in the cloud agent environment.

Usage:
  python assemble_video.py --project projects/01-foreigners-buy-property-ksa
  python assemble_video.py --project projects/01-foreigners-buy-property-ksa --allow-placeholders

Project folder layout:
  assembly_manifest.json
  avatar/*.mp4
  voiceover/*.mp3
  broll/chapter-N/*.mp4
  assets/music/background.mp3  (optional)
  output/final.mp4
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

W, H = 1920, 1080
FPS = 30


def run(cmd: list[str], quiet: bool = False) -> None:
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed:\n{' '.join(cmd)}\n\nstderr:\n{result.stderr[-2000:]}"
        )
    if not quiet and result.stderr:
        pass  # ffmpeg logs to stderr


def ffprobe_duration(path: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(path),
        ],
        text=True,
    ).strip()
    return float(out)


def normalize_video(input_path: Path, output_path: Path, duration: float | None = None) -> None:
    """Scale/pad to 1080p H.264."""
    vf = f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={FPS}"
    cmd = [
        "ffmpeg", "-y", "-i", str(input_path),
        "-vf", vf,
        "-c:v", "libx264", "-preset", "fast", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    ]
    if duration is not None:
        cmd[2:2] = ["-t", str(duration)]
    cmd.append(str(output_path))
    run(cmd)


def make_placeholder_broll(output_path: Path, duration: float, label: str) -> None:
    """Navy slate with label when B-roll clips are missing."""
    safe = label.replace(":", "\\:").replace("'", "\\'")[:60]
    vf = (
        f"color=c=0x0D1B2A:s={W}x{H}:d={duration},"
        f"drawtext=text='{safe}':fontcolor=0xC5A572:fontsize=36:"
        f"x=(w-text_w)/2:y=(h-text_h)/2"
    )
    run([
        "ffmpeg", "-y", "-f", "lavfi", "-i", vf,
        "-c:v", "libx264", "-preset", "fast", "-crf", "20",
        "-t", str(duration), "-r", str(FPS), "-an",
        str(output_path),
    ])


def build_broll_track(
    broll_dir: Path,
    audio_path: Path,
    work_dir: Path,
    clip_target: float,
    chapter_id: str,
    allow_placeholders: bool,
) -> Path:
    audio_dur = ffprobe_duration(audio_path)
    clips = sorted(broll_dir.glob("*.mp4")) + sorted(broll_dir.glob("*.mov"))
    if not clips and allow_placeholders:
        placeholder = work_dir / f"{chapter_id}_placeholder.mp4"
        make_placeholder_broll(placeholder, audio_dur, f"Saudi Gateway — {chapter_id}")
        clips = [placeholder]
    elif not clips:
        raise FileNotFoundError(f"No B-roll in {broll_dir} (use --allow-placeholders for test)")

    normalized: list[Path] = []
    total = 0.0
    idx = 0
    while total < audio_dur:
        src = clips[idx % len(clips)]
        remaining = audio_dur - total
        seg_dur = min(clip_target, remaining)
        out = work_dir / f"{chapter_id}_broll_{len(normalized):03d}.mp4"
        src_dur = ffprobe_duration(src)
        trim = min(seg_dur, src_dur)
        vf = f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={FPS}"
        run([
            "ffmpeg", "-y", "-i", str(src), "-t", str(trim),
            "-vf", vf, "-an",
            "-c:v", "libx264", "-preset", "fast", "-crf", "20",
            str(out),
        ])
        normalized.append(out)
        total += trim
        idx += 1

    # Concat video clips
    concat_list = work_dir / f"{chapter_id}_concat.txt"
    concat_list.write_text(
        "".join(f"file '{p.resolve()}'\n" for p in normalized), encoding="utf-8"
    )
    video_only = work_dir / f"{chapter_id}_video.mp4"
    run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
        "-c:v", "libx264", "-preset", "fast", "-crf", "20", str(video_only),
    ])

    # Merge with narration audio (trim to shortest)
    merged = work_dir / f"{chapter_id}_merged.mp4"
    run([
        "ffmpeg", "-y", "-i", str(video_only), "-i", str(audio_path),
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-shortest", str(merged),
    ])
    return merged


def process_avatar(segment: dict, project: Path, work_dir: Path, allow_placeholders: bool) -> Path:
    src = project / segment["file"]
    if not src.exists():
        if not allow_placeholders:
            raise FileNotFoundError(f"Avatar missing: {src}")
        out = work_dir / Path(segment["file"]).name
        make_placeholder_broll(out, 5.0, "Avatar — pending HeyGen export")
        return out
    out = work_dir / f"avatar_{Path(segment['file']).stem}.mp4"
    normalize_video(src, out)
    return out


def concat_segments(segment_files: list[Path], output: Path) -> None:
    lst = output.parent / "final_concat.txt"
    lst.write_text(
        "".join(f"file '{p.resolve()}'\n" for p in segment_files), encoding="utf-8"
    )
    run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
        "-c:v", "libx264", "-preset", "fast", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k", str(output),
    ])


def add_background_music(video: Path, music: Path, volume: float, output: Path) -> None:
    run([
        "ffmpeg", "-y", "-i", str(video), "-i", str(music),
        "-filter_complex",
        f"[1:a]volume={volume}[bg];[0:a][bg]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "0:v", "-map", "[aout]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        str(output),
    ])


def generate_srt(segment_files: list[Path], output: Path) -> None:
    """Build basic SRT from segment durations (YouTube upload)."""
    lines: list[str] = []
    t = 0.0
    for i, seg in enumerate(segment_files, 1):
        dur = ffprobe_duration(seg)
        start = format_srt_time(t)
        end = format_srt_time(t + dur)
        lines.append(f"{i}\n{start} --> {end}\n[Segment {i}]\n")
        t += dur
    output.write_text("\n".join(lines), encoding="utf-8")


def format_srt_time(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def generate_chapters_txt(segment_files: list[Path], manifest: dict, output: Path) -> None:
  lines = ["# YouTube chapter markers (paste in description)\n"]
  t = 0.0
  for seg_file, seg_def in zip(segment_files, manifest["segments"]):
      mins, secs = divmod(int(t), 60)
      label = seg_def.get("chapter_id") or Path(seg_def.get("file", "segment")).stem
      if seg_def["type"] == "avatar":
          label = Path(seg_def["file"]).stem
      lines.append(f"{mins}:{secs:02d} {label}")
      t += ffprobe_duration(seg_file)
  output.write_text("\n".join(lines), encoding="utf-8")


def assemble(project: Path, allow_placeholders: bool = False) -> Path:
    manifest_path = project / "assembly_manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Missing {manifest_path} — run generate_manifest.py first")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    work_dir = project / ".work"
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir()

    segment_outputs: list[Path] = []
    clip_target = manifest.get("clip_duration_target_sec", 5.5)

    for seg in manifest["segments"]:
        if seg["type"] == "avatar":
            segment_outputs.append(
                process_avatar(seg, project, work_dir, allow_placeholders)
            )
        elif seg["type"] == "broll_vo":
            audio = project / seg["audio"]
            if not audio.exists():
                raise FileNotFoundError(f"Voiceover missing: {audio}")
            broll_dir = project / seg["broll_dir"]
            segment_outputs.append(
                build_broll_track(
                    broll_dir, audio, work_dir, clip_target,
                    seg.get("chapter_id", "ch"), allow_placeholders,
                )
            )
        else:
            raise ValueError(f"Unknown segment type: {seg['type']}")

    out_dir = project / "output"
    out_dir.mkdir(exist_ok=True)
    raw = out_dir / "final_raw.mp4"
    concat_segments(segment_outputs, raw)

    final = project / manifest["output"]["video"]
    music_cfg = manifest.get("music", {})
    music_path = project / music_cfg.get("file", "")
    if music_path.exists() and not music_cfg.get("optional", True) is False:
        add_background_music(raw, music_path, music_cfg.get("volume", 0.07), final)
    else:
        shutil.copy(raw, final)

    generate_srt(segment_outputs, project / manifest["output"]["subtitles"])
    generate_chapters_txt(segment_outputs, manifest, project / manifest["output"]["chapters"])

    shutil.rmtree(work_dir, ignore_errors=True)
    return final


def main() -> int:
    parser = argparse.ArgumentParser(description="Assemble Saudi Gateway video via FFmpeg")
    parser.add_argument("--project", type=Path, required=True, help="Project directory")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Use slate placeholders for missing avatar/B-roll (testing)",
    )
    args = parser.parse_args()

    project = args.project.resolve()
    try:
        final = assemble(project, args.allow_placeholders)
        dur = ffprobe_duration(final)
        print(f"✓ Assembled: {final}")
        print(f"  Duration: {dur / 60:.1f} minutes")
        print(f"  Subtitles: {project / 'output' / 'subtitles.srt'}")
        print(f"  Chapters:  {project / 'output' / 'chapters.txt'}")
        return 0
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
