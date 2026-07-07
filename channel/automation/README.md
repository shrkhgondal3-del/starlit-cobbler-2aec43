# Saudi Gateway — Video Automation

Converts markdown scripts into AI-production assets.

## Quick Start

```bash
python3 prepare_video.py ../content/scripts/01-foreigners-buy-property-ksa.md
```

## Output (per script)

```
output/01-foreigners-buy-property-ksa/
├── voiceover.txt              # Full narration for InVideo AI or review
├── voiceover_chapters/        # One .txt per chapter → paste into ElevenLabs
│   ├── hook.txt
│   ├── chapter-1-....txt
│   └── ...
├── broll_shotlist.json        # AI prompts + stock search terms per scene
└── production_brief.md        # Assembly instructions for CapCut
```

## Batch Mode

```bash
python3 prepare_video.py ../content/scripts/01-*.md ../content/scripts/02-*.md
```

## Requirements

- Python 3.8+ (stdlib only — no pip install needed)

## Next Steps After Running

1. **ElevenLabs** — paste each `voiceover_chapters/*.txt` → export MP3
2. **Runway** — use prompts from `broll_shotlist.json`
3. **CapCut** — follow `production_brief.md`
4. **Ideogram** — thumbnails per `../content/ai-prompts/THUMBNAIL-PROMPTS.md`

See `../operations/AI-PRODUCTION-PLAYBOOK.md` for the full pipeline.
