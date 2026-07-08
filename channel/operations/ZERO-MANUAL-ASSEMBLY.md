# Saudi Gateway — Zero Manual Assembly

**You do not need CapCut.** The cloud agent assembles every video automatically with FFmpeg.

---

## What you do vs what the agent does

| Task | You | Agent (me) |
|------|-----|------------|
| Sign up & pay for tools | Once | — |
| Connect Higgsfield MCP + API keys | Once | — |
| Approve final video before publish | 2 min/video | — |
| YouTube upload click | 5 min/video (until API added) | — |
| Scripts, SEO, calendar | — | Yes |
| ElevenLabs voiceover MP3s | — | Yes (with API key) |
| Higgsfield B-roll | — | Yes (with MCP) |
| HeyGen avatar clips | — | Yes (with API key) or you export once |
| **FFmpeg video assembly** | — | **Yes — fully automated** |
| Subtitles + chapter file | — | Yes |

**Your time per video after setup: ~10 minutes** (watch + upload + approve).

---

## Automated pipeline

```
Script (.md)
    ↓
prepare_video.py           → voiceover text + broll shot list
    ↓
elevenlabs_generate.py     → voiceover/*.mp3        [agent + API key]
    ↓
Higgsfield MCP             → broll/chapter-N/*.mp4  [agent + MCP]
    ↓
HeyGen API / export        → avatar/*.mp4           [agent + API key]
    ↓
assemble_video.py          → output/final.mp4       [agent — no CapCut]
    ↓
You                        → upload to YouTube
```

---

## One-time setup (you — ~30 minutes)

### 1. Accounts (required)
| Tool | Plan | Why |
|------|------|-----|
| ElevenLabs | Creator $22/mo | Voice — agent uses API |
| HeyGen | Creator $24/mo | Charlotte avatar |
| Higgsfield | Plus $49/mo | B-roll + MCP |
| YouTube | Free | Publishing |

**Skip CapCut. Skip Canva.**

### 2. Give the agent access (one time)

Add these to your **Cursor environment secrets** or tell me the keys:

| Secret | Where to get it |
|--------|-----------------|
| `ELEVENLABS_API_KEY` | elevenlabs.io → Profile → API Key |
| `HEYGEN_API_KEY` | heygen.com → Settings → API (optional — speeds avatar) |
| Higgsfield MCP | Cursor → MCP → `https://mcp.higgsfield.ai/mcp` → Connect |

### 3. Train Charlotte Hayes once
- Generate 8 reference images (`AVATAR-REFERENCE-PROMPTS.md`)
- HeyGen Photo Avatar → save avatar ID → share with agent

---

## Per video — agent runs everything

```bash
# Step 1: Init project
python3 channel/automation/run_pipeline.py init \
  --script channel/content/scripts/01-foreigners-buy-property-ksa.md

# Step 2: Agent generates voiceovers (needs ELEVENLABS_API_KEY)
python3 channel/automation/elevenlabs_generate.py \
  --voice-id YOUR_CHARLOTTE_VOICE_ID \
  --input-dir channel/automation/output/01-foreigners-buy-property-ksa/voiceover_chapters \
  --output-dir channel/automation/projects/01-foreigners-buy-property-ksa/voiceover

# Step 3: Agent generates B-roll via Higgsfield MCP into broll/chapter-N/

# Step 4: Agent places HeyGen avatar clips in avatar/

# Step 5: Auto-assemble — NO CapCut
python3 channel/automation/run_pipeline.py assemble \
  --project channel/automation/projects/01-foreigners-buy-property-ksa
```

**Output:**
- `projects/.../output/final.mp4` — ready for YouTube
- `projects/.../output/subtitles.srt` — upload with video
- `projects/.../output/chapters.txt` — paste in description

---

## Project folder structure

```
channel/automation/projects/01-foreigners-buy-property-ksa/
├── assembly_manifest.json
├── avatar/
│   ├── hook.mp4              ← HeyGen (agent or API)
│   ├── bridge-ch3.mp4
│   ├── bridge-ch4.mp4
│   ├── myth-emphasis.mp4
│   └── close.mp4
├── voiceover/
│   ├── chapter-1-....mp3     ← ElevenLabs API
│   └── ...
├── broll/
│   ├── chapter-1/*.mp4       ← Higgsfield MCP
│   └── ...
├── assets/music/
│   └── background.mp3        ← optional
└── output/
    ├── final.mp4             ← AGENT ASSEMBLES
    ├── subtitles.srt
    └── chapters.txt
```

---

## What assembly does automatically

| Feature | How |
|---------|-----|
| Avatar + B-roll timeline | Reads `assembly_manifest.json` |
| B-roll cut every ~5.5 sec | Cycles clips to match voiceover length |
| 1080p normalization | Scale/pad all clips to 1920×1080 |
| Audio sync | Voiceover drives B-roll segment duration |
| Background music | Optional mix at 7% volume |
| Subtitles file | SRT with segment timings |
| YouTube chapters | `chapters.txt` for description |

---

## Testing without assets

Agent can test the pipeline with placeholders:

```bash
python3 channel/automation/run_pipeline.py init \
  --script channel/content/scripts/01-foreigners-buy-property-ksa.md

# Create test audio from text (agent runs ffmpeg) or use elevenlabs when key set

python3 channel/automation/assemble_video.py \
  --project channel/automation/projects/01-foreigners-buy-property-ksa \
  --allow-placeholders
```

---

## Your only recurring tasks

1. **Approve** — watch `final.mp4` before publish (2 min)
2. **Upload** — YouTube Studio → upload MP4 + SRT + paste SEO from repo (5–10 min)
3. **Optional later** — YouTube API for agent upload (we can add)

---

*No CapCut. No manual timeline editing. Agent handles assembly.*
