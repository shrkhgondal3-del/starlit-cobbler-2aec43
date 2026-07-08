# Saudi Gateway — Video Automation

**Agent-operated pipeline — no CapCut, no manual assembly.**

## Commands

```bash
# 1. Init project from script
python3 run_pipeline.py init --script ../content/scripts/01-foreigners-buy-property-ksa.md

# 2. Generate voiceovers (needs ELEVENLABS_API_KEY)
export ELEVENLABS_API_KEY=sk_...
python3 elevenlabs_generate.py \
  --voice-id YOUR_VOICE_ID \
  --input-dir output/01-foreigners-buy-property-ksa/voiceover_chapters \
  --output-dir projects/01-foreigners-buy-property-ksa/voiceover

# 3. Agent adds avatar/*.mp4 (HeyGen) and broll/chapter-N/*.mp4 (Higgsfield)

# 4. Auto-assemble final video
python3 run_pipeline.py assemble \
  --project projects/01-foreigners-buy-property-ksa
```

## Scripts

| Script | Purpose |
|--------|---------|
| `prepare_video.py` | Script → voiceover text + broll shot list |
| `generate_manifest.py` | Timeline manifest for assembly |
| `elevenlabs_generate.py` | API → voiceover MP3s |
| `assemble_video.py` | FFmpeg → `output/final.mp4` |
| `run_pipeline.py` | Orchestrator |

## Output

```
projects/01-foreigners-buy-property-ksa/
├── avatar/*.mp4
├── voiceover/*.mp3
├── broll/chapter-N/*.mp4
└── output/
    ├── final.mp4       ← YouTube-ready
    ├── subtitles.srt
    └── chapters.txt
```

## Requirements

- Python 3.8+
- FFmpeg (`ffmpeg` + `ffprobe` on PATH)
- `ELEVENLABS_API_KEY` for voice generation
- Higgsfield MCP for B-roll (agent)

See `../operations/ZERO-MANUAL-ASSEMBLY.md` for full handoff guide.
