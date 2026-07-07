#!/usr/bin/env python3
"""
Saudi Gateway — AI Video Production Prep

Converts a markdown script into AI-production assets:
  - voiceover.txt (full narration)
  - voiceover_chapters/*.txt (per-chapter for ElevenLabs)
  - broll_shotlist.json (scene list with AI prompts)
  - production_brief.md (assembly instructions)

Usage:
  python prepare_video.py ../content/scripts/01-foreigners-buy-property-ksa.md
  python prepare_video.py ../content/scripts/*.md --batch
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# B-roll prompt templates keyed by keyword in visual tags or chapter titles
BROLL_TEMPLATES: dict[str, dict] = {
    "riyadh": {
        "prompt": "Aerial drone shot of modern Riyadh skyline at golden hour, Kingdom Centre visible, cinematic",
        "stock": ["riyadh skyline", "saudi arabia city aerial"],
    },
    "jeddah": {
        "prompt": "Jeddah Corniche Red Sea waterfront, modern Saudi city, aerial cinematic",
        "stock": ["jeddah corniche", "jeddah skyline"],
    },
    "neom": {
        "prompt": "Futuristic sustainable city concept Red Sea coastline, artist impression, aerial",
        "stock": ["futuristic city coast", "smart city aerial"],
        "label": "Artist impression",
    },
    "rega": {
        "prompt": "Modern government administrative building exterior, formal architecture, establishing shot",
        "stock": ["government building", "official documents desk"],
    },
    "misa": {
        "prompt": "Professional working on laptop in modern office, government portal, over-shoulder",
        "stock": ["business laptop office", "corporate office middle east"],
    },
    "property": {
        "prompt": "Luxury modern apartment exterior Middle Eastern city, palm trees, slow pan",
        "stock": ["luxury apartment building", "real estate exterior"],
    },
    "contract": {
        "prompt": "Close-up hands reviewing property documents on desk, shallow depth of field",
        "stock": ["signing contract", "property documents"],
    },
    "boardroom": {
        "prompt": "Corporate boardroom floor-to-ceiling windows city view, professional atmosphere",
        "stock": ["boardroom skyline", "corporate meeting"],
    },
    "desert": {
        "prompt": "Vast Saudi desert landscape aerial, sand dunes, cinematic flyover",
        "stock": ["saudi desert aerial", "desert dunes drone"],
    },
    "diriyah": {
        "prompt": "Heritage mud-brick Najdi architecture golden hour, Diriyah style gateway",
        "stock": ["middle eastern heritage architecture", "historic arab architecture"],
    },
    "flowchart": {
        "prompt": "Motion graphic flowchart on dark navy background, green and gold accents",
        "stock": [],
        "type": "motion_graphic",
    },
    "map": {
        "prompt": "Minimal map of Saudi Arabia dark navy background gold outline infographic",
        "stock": [],
        "type": "motion_graphic",
    },
    "default": {
        "prompt": "Professional Saudi Arabian business cityscape, modern development, cinematic documentary",
        "stock": ["saudi arabia", "middle east business"],
    },
}


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text)[:60]


def parse_script(content: str) -> dict:
    """Parse markdown script into metadata and chapters."""
    lines = content.splitlines()
    meta: dict = {"title": "", "runtime": "", "pillar": "", "thumbnail": ""}
    chapters: list[dict] = []
    current: dict | None = None
    in_production_notes = False

    for line in lines:
        if line.startswith("# Script"):
            meta["title"] = line.replace("# Script", "").strip(" —").strip()
        elif line.startswith("**Runtime target:**"):
            meta["runtime"] = line.split("**Runtime target:**", 1)[1].strip()
        elif line.startswith("**Pillar:**"):
            meta["pillar"] = line.split("**Pillar:**", 1)[1].strip()
        elif line.startswith("**Thumbnail title:**"):
            meta["thumbnail"] = line.split("`")[1] if "`" in line else line

        if line.strip() == "## Production Notes":
            in_production_notes = True
            if current:
                chapters.append(current)
                current = None
            continue

        if in_production_notes:
            continue

        chapter_match = re.match(
            r"^## (HOOK|CHAPTER \d+|CLOSE)(?:\s*:\s*(.+?))?(?:\s*\((.+?)\))?\s*$",
            line,
        )
        if chapter_match:
            if current:
                chapters.append(current)
            kind, title, timestamp = chapter_match.groups()
            title = title or kind
            current = {
                "id": slugify(f"{kind}-{title}"),
                "kind": kind,
                "title": title.strip(),
                "timestamp": timestamp or "",
                "narration": [],
                "visuals": [],
            }
            continue

        if current is None:
            continue

        visual_match = re.match(r"^\*\*\[B-roll:\s*(.+?)\]\*\*$", line.strip())
        if visual_match or line.strip().startswith("[B-roll:"):
            vis = visual_match.group(1) if visual_match else line.strip()
            current["visuals"].append(vis)
            continue

        if line.strip().startswith("[On-screen") or line.strip().startswith("**[On-screen"):
            current["visuals"].append(line.strip().strip("*[]"))
            continue

        if line.strip().startswith("[On camera") or line.strip().startswith("**[On camera"):
            continue

        if line.strip().startswith("|") or line.strip().startswith("---"):
            continue

        # Narration: quoted text or plain paragraphs
        quoted = re.match(r'^"(.+)"$', line.strip())
        if quoted:
            current["narration"].append(quoted.group(1))
        elif line.strip() and not line.strip().startswith("#") and not line.strip().startswith("**Runtime"):
            cleaned = re.sub(r"\*\*(.+?)\*\*", r"\1", line.strip())
            cleaned = re.sub(r"\*(.+?)\*", r"\1", cleaned)
            if cleaned and not cleaned.startswith("-"):
                current["narration"].append(cleaned)
            elif cleaned.startswith("- "):
                current["narration"].append(cleaned[2:])

    if current:
        chapters.append(current)

    return {"meta": meta, "chapters": chapters}


def clean_for_voiceover(text: str) -> str:
    """Convert narration to ElevenLabs-friendly plain text."""
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"—", ", ", text)
    text = re.sub(r"\s+", " ", text).strip()
    # Numbers 1-10 as words for natural TTS
    replacements = {
        "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
        "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten",
    }
    for num, word in replacements.items():
        text = re.sub(rf"\b{num}\b", word, text)
    return text


def match_broll(chapter: dict) -> list[dict]:
    """Generate B-roll entries for a chapter."""
    combined = (chapter["title"] + " " + " ".join(chapter["visuals"])).lower()
    scenes: list[dict] = []
    matched_keys: set[str] = set()

    for key, template in BROLL_TEMPLATES.items():
        if key == "default":
            continue
        if key in combined or any(key in v.lower() for v in chapter["visuals"]):
            matched_keys.add(key)
            scenes.append({
                "chapter": chapter["id"],
                "keyword": key,
                "type": template.get("type", "video"),
                "ai_prompt": template["prompt"] + ", cinematic documentary, 4K, no text",
                "stock_search": template["stock"],
                "on_screen_label": template.get("label"),
                "duration_sec": 6,
            })

    if not scenes:
        t = BROLL_TEMPLATES["default"]
        scenes.append({
            "chapter": chapter["id"],
            "keyword": "default",
            "type": "video",
            "ai_prompt": t["prompt"] + ", cinematic documentary, 4K, no text",
            "stock_search": t["stock"],
            "duration_sec": 6,
        })

    # Flowchart/map for explainer chapters
    if "pathway" in combined or "step" in combined or "flow" in combined:
        scenes.append({
            "chapter": chapter["id"],
            "keyword": "flowchart",
            "type": "motion_graphic",
            "ai_prompt": BROLL_TEMPLATES["flowchart"]["prompt"],
            "stock_search": [],
            "duration_sec": 8,
            "notes": "Build in Canva — export PNG sequence or MP4",
        })

    return scenes


def build_production_brief(meta: dict, chapters: list[dict], shots: list[dict]) -> str:
    title = meta.get("title", "Untitled")
    lines = [
        f"# Production Brief — {title}",
        "",
        "## AI Production Summary",
        "",
        f"- **Format:** AI Documentary (voiceover + B-roll + motion graphics)",
        f"- **Runtime target:** {meta.get('runtime', 'TBD')}",
        f"- **Pillar:** {meta.get('pillar', 'TBD')}",
        f"- **Thumbnail title:** `{meta.get('thumbnail', 'TBD')}`",
        "",
        "## Step 1: Voiceover (ElevenLabs)",
        "",
        "Voice: Charlotte or Alice (British female) | Model: Multilingual v2 | Stability: 0.65",
        "",
        "Generate one MP3 per chapter:",
        "",
    ]
    for i, ch in enumerate(chapters, 1):
        words = sum(len(clean_for_voiceover(n).split()) for n in ch["narration"])
        est_min = max(0.5, words / 150)
        lines.append(f"{i}. `{ch['id']}.mp3` — {ch['title']} (~{est_min:.1f} min, {words} words)")

    lines.extend([
        "",
        "## Step 2: Chapter Timestamps (for YouTube)",
        "",
    ])
    t = 0.0
    for ch in chapters:
        words = sum(len(clean_for_voiceover(n).split()) for n in ch["narration"])
        dur = words / 150 * 60
        mins, secs = divmod(int(t), 60)
        lines.append(f"- {mins}:{secs:02d} — {ch['title']}")
        t += dur

    lines.extend([
        "",
        "## Step 3: B-Roll Assembly",
        "",
        f"Total scenes: {len(shots)}",
        "",
        "| # | Chapter | Type | AI Prompt / Action |",
        "|---|---------|------|-------------------|",
    ])
    for i, s in enumerate(shots, 1):
        prompt = s["ai_prompt"][:60] + "..." if len(s["ai_prompt"]) > 60 else s["ai_prompt"]
        lines.append(f"| {i} | {s['chapter']} | {s['type']} | {prompt} |")

    lines.extend([
        "",
        "## Step 4: CapCut Assembly",
        "",
        "1. Import chapter MP3s sequentially on audio track",
        "2. Auto-generate English captions",
        "3. Lay B-roll — cut every 4-6 sec, never static > 5 sec",
        "4. Add disclaimer card first 3 seconds",
        "5. Music: -20dB under voice (Epidemic Sound / CapCut royalty-free)",
        "6. Export 1080p H.264",
        "",
        "## Step 5: Post-Upload",
        "",
        "- Enable YouTube altered/synthetic content disclosure",
        "- Auto-translate captions to Arabic",
        "- Upload 3 AI thumbnails (see ai-prompts/THUMBNAIL-PROMPTS.md)",
        "- Opus Clip → 3 Shorts",
        "",
        "## Disclaimer (spoken + on-screen)",
        "",
        "> This video was created with AI-assisted production. Educational purposes only — not legal or investment advice.",
        "",
    ])
    return "\n".join(lines)


def process_script(script_path: Path, output_root: Path) -> Path:
    content = script_path.read_text(encoding="utf-8")
    parsed = parse_script(content)
    meta, chapters = parsed["meta"], parsed["chapters"]

    out_dir = output_root / slugify(script_path.stem)
    out_dir.mkdir(parents=True, exist_ok=True)
    chapters_dir = out_dir / "voiceover_chapters"
    chapters_dir.mkdir(exist_ok=True)

    all_voice: list[str] = []
    all_shots: list[dict] = []

    intro = (
        "Welcome to Saudi Gateway — your path to property and business in Saudi Arabia. "
        "This video was created with AI-assisted production. "
        "It is for educational purposes only and is not legal, tax, or investment advice."
    )

    for i, ch in enumerate(chapters):
        parts = [clean_for_voiceover(n) for n in ch["narration"] if n.strip()]
        if not parts:
            continue
        text = "\n\n".join(parts)
        if i == 0:
            text = intro + "\n\n" + text
        all_voice.append(text)
        (chapters_dir / f"{ch['id']}.txt").write_text(text, encoding="utf-8")
        all_shots.extend(match_broll(ch))

    full_voice = "\n\n---\n\n".join(all_voice)
    (out_dir / "voiceover.txt").write_text(full_voice, encoding="utf-8")

    shotlist = {
        "script": script_path.name,
        "title": meta.get("title"),
        "total_scenes": len(all_shots),
        "scenes": all_shots,
    }
    (out_dir / "broll_shotlist.json").write_text(
        json.dumps(shotlist, indent=2), encoding="utf-8"
    )

    brief = build_production_brief(meta, chapters, all_shots)
    (out_dir / "production_brief.md").write_text(brief, encoding="utf-8")

    return out_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare Saudi Gateway script for AI video production")
    parser.add_argument("scripts", nargs="+", type=Path, help="Script markdown file(s)")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent / "output",
        help="Output directory (default: automation/output)",
    )
    args = parser.parse_args()

    for script in args.scripts:
        if not script.exists():
            print(f"ERROR: not found: {script}", file=sys.stderr)
            return 1
        out = process_script(script.resolve(), args.output.resolve())
        print(f"✓ {script.name} → {out}")
        print(f"  - voiceover.txt")
        print(f"  - voiceover_chapters/ ({len(list((out / 'voiceover_chapters').glob('*.txt')))} files)")
        print(f"  - broll_shotlist.json")
        print(f"  - production_brief.md")

    return 0


if __name__ == "__main__":
    sys.exit(main())
