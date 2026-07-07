# Saudi Gateway — AI-Only Production Playbook

**100% AI pipeline.** No real camera, no human presenter — but includes **AI avatar host Charlotte Hayes** for hooks, bridges, and CTAs.

---

## Video Format: Hybrid Avatar + Documentary

Best format for property/finance YouTube: trusted AI host + cinematic B-roll depth.

| Segment | Format | Tool |
|---------|--------|------|
| Hook, bridges, myth moments, close | **Avatar** (Charlotte Hayes) | HeyGen |
| Chapter body | **B-roll + graphics** | Higgsfield MCP (Kling/Veo) |
| Voice (all segments) | Same voice clone | ElevenLabs |
| Thumbnails | Avatar face | Higgsfield Soul or HeyGen still |
| Shorts opening | Avatar 3–5 sec | HeyGen 9:16 |

Full avatar setup: `avatar/AVATAR-PRODUCTION-GUIDE.md` and `avatar/CHARACTER-BIBLE.md`

| Layer | AI Tool | Output |
|-------|---------|--------|
| **Avatar clips** | HeyGen (Charlotte Hayes) | hook, bridges, close MP4s |
| **Script** | Claude Fable 5 + repo scripts | Markdown with AVATAR/B-ROLL markers |
| **Voiceover** | ElevenLabs (voice clone) | MP3 per B-roll chapter |
| **B-roll** | Higgsfield MCP (Kling/Veo) + Pexels | 4K clips per scene |
| **Motion graphics** | Canva / CapCut templates | Charts, flowcharts, lower-thirds |
| **Assembly** | CapCut | Avatar + B-roll on timeline |
| **Captions** | CapCut auto-caption | SRT (EN + AR via YouTube) |
| **Thumbnails** | HeyGen/Soul still + Canva text | 1280×720 × 3 variants |
| **Shorts** | HeyGen hook + Opus Clip or Higgsfield Clipper | 3 Shorts per long-form |

---

## End-to-End Pipeline (One Video)

```
Script (.md with AVATAR markers)
    ↓
prepare_video.py  →  voiceover.txt + broll_shotlist.json + production_brief.md
    ↓
HeyGen  →  avatar clips (hook, bridges, close) — Charlotte Hayes
    ↓
ElevenLabs  →  voice clone → B-roll chapter MP3s
    ↓
Higgsfield MCP  →  broll/*.mp4 (Kling 3, Veo 3.1)
    ↓
Canva  →  graphics/*.png
    ↓
CapCut  →  stitch avatar + B-roll on timeline
    ↓
CapCut captions + YouTube AR auto-translate
    ↓
Soul/HeyGen still + Canva  →  3 thumbnails (with Charlotte Hayes face)
    ↓
YouTube Studio  →  upload + synthetic content disclosure
    ↓
Opus Clip / Higgsfield Clipper  →  3 Shorts (avatar hook + B-roll)
```

**Time per long-form video (avatar + documentary):** 3–5 hours once pipeline is set up.

---

## Step 1: Prepare Script for AI Voice

Run the automation script:

```bash
cd channel/automation
python prepare_video.py ../content/scripts/01-foreigners-buy-property-ksa.md
```

Outputs to `channel/automation/output/01-foreigners-buy-property-ksa/`:
- `voiceover.txt` — clean narration text (no stage directions)
- `voiceover_chapters/` — one `.txt` per chapter for ElevenLabs
- `broll_shotlist.json` — scene prompts + stock search terms
- `production_brief.md` — full assembly instructions for editor

Or use pre-converted AI scripts in `content/scripts/ai-ready/`.

---

## Step 2: Generate Voiceover (ElevenLabs)

### Voice profile (lock this for brand consistency)

| Setting | Value |
|---------|-------|
| **Voice** | "Charlotte" (British) or "Alice" (British, soft) | Stability 0.65, Speed 0.95 |
| **Model** | Eleven Multilingual v2 |
| **Stability** | 0.65 |
| **Similarity** | 0.80 |
| **Style** | 0.15 (keep low — avoid dramatic acting) |
| **Speed** | 0.95 (slightly slower = more authority) |

### Process
1. Paste each chapter file from `voiceover_chapters/` into ElevenLabs
2. Export as MP3 192kbps
3. Name: `ch01-hook.mp3`, `ch02-old-rule.mp3`, etc.
4. Do **not** add background music in ElevenLabs — add in edit

### Intro line (use on every video)
> "Saudi Gateway — your path to property and business in Saudi Arabia."

---

## Step 3: Generate B-Roll & Visuals

### AI video generation (Runway / Kling)

Use prompts from `broll_shotlist.json` or `content/ai-prompts/BROLL-PROMPTS.md`.

**Runway settings:**
- Duration: 5–10 sec per clip
- Aspect: 16:9
- Style: cinematic, documentary, natural lighting
- **Always label** NEOM/giga-project clips as "artist impression" in post

### Stock footage fallback (Pexels / Storyblocks — free or subscription)

Search terms per chapter are in `broll_shotlist.json`. Priority:
1. Real Saudi footage (Riyadh skyline, Jeddah, business districts)
2. Generic Middle East aerials (if Saudi-specific unavailable)
3. AI-generated only when stock fails

### Motion graphics (Canva)

Create reusable templates:
- **Lower third:** "Saudi Gateway" + chapter title (green bar, navy bg)
- **Flowchart:** 4 pathways diagram (Script 01)
- **Source card:** "Source: REGA — rega.gov.sa" (show when citing regulations)
- **Disclaimer card:** 3 sec at start: "Educational content only. Not legal advice."
- **End card:** Subscribe CTA + checklist QR

Export as PNG with transparent background or MP4.

---

## Step 4: Assemble in CapCut (Recommended) or InVideo AI

### CapCut assembly workflow

1. **New project** → 1920×1080, 30fps
2. **Import** all chapter MP3s → place sequentially on audio track
3. **Auto-generate captions** from audio (English)
4. For each chapter:
   - Lay B-roll clips to cover voice duration
   - Cut every 4–6 seconds (retention — never static frame > 5 sec)
   - Overlay motion graphics at key points
5. **Add music:** Epidemic Sound or CapCut royalty-free — **-20dB under voice**
6. **Color grade:** Slight contrast boost, warm tones (desert gold feel)
7. **Intro sting:** 2 sec logo animation (Canva or CapCut template)
8. **Export:** H.264, 1080p, 15–20 Mbps

### InVideo AI alternative (faster, less control)

1. Paste full `voiceover.txt`
2. Select "Stock + AI" media mode
3. Paste B-roll prompts from shotlist
4. Review scene-by-scene, swap bad clips
5. Export and fine-tune in CapCut if needed

---

## Step 5: Subtitles (English + Arabic)

### English
- CapCut auto-caption → review for "REGA", "MISA", "ZATCA" spelling
- Export SRT

### Arabic
- YouTube Studio → Subtitles → **Auto-translate** to Arabic (post-upload)
- OR DeepL translate SRT → upload Arabic SRT
- OR ElevenLabs Arabic TTS for full dub (Phase 2)

---

## Step 6: AI Thumbnails

See `content/ai-prompts/THUMBNAIL-PROMPTS.md`.

**Quick process:**
1. Generate base image in Ideogram (navy bg, gold accents, Saudi skyline)
2. Add text in Canva (Montserrat Bold, max 6 words)
3. Add badge: "2026" / "FOREIGNERS" / "GUIDE"
4. Export 3 variants for A/B test

**No AI faces** unless using a consistent HeyGen avatar — use architecture/maps/documents instead.

---

## Step 7: Shorts (Automated)

### Opus Clip
1. Upload finished long-form
2. Prompt: "Find clips about foreign property ownership, REGA, Premium Residency, mistakes"
3. Generate 3–5 Shorts
4. Pick best 3, add hook text overlay in CapCut
5. Export 9:16, 30–55 sec

### CapCut AI clipper (free alternative)
- Import long-form → "AI clip" → select highlights

---

## Step 8: Upload & SEO

1. Upload to YouTube Studio
2. Paste title, description, tags from `operations/SEO-PLAYBOOK.md`
3. Upload 3 thumbnails → enable Test & Compare
4. Add chapters (timestamps from `production_brief.md`)
5. Add end screen (last 20 sec)
6. Pin comment (template in SEO playbook)
7. Schedule Shorts for Mon/Wed/Sat

---

## AI Disclosure (Required)

Add to **every video description** and **spoken in intro**:

> This video was created with AI-assisted production (voiceover and visuals). Content is researched from official Saudi government sources and reviewed for accuracy. Educational purposes only — not legal or investment advice.

Add to **channel About page**:
> Saudi Gateway uses AI production tools to deliver clear, current guides. All regulatory information is sourced from official portals (MISA, REGA, ZATCA).

YouTube may require "altered content" disclosure in upload settings if using synthetic media — **enable this**.

---

## Quality Checklist (AI-Specific)

Before publish:

- [ ] Voice pacing sounds natural (no robotic glitches at chapter joins)
- [ ] No single static frame longer than 5 seconds
- [ ] All regulation citations show source on screen
- [ ] AI-generated cityscapes labeled if not real footage
- [ ] "Educational only" disclaimer in first 10 seconds
- [ ] REGA, MISA, ZATCA spelled correctly in captions
- [ ] Background music ducked properly under voice
- [ ] YouTube "altered/synthetic content" disclosure set if required
- [ ] 3 thumbnail variants uploaded

---

## Batch Production (Produce 4 Videos in One Sitting)

| Hour | Task |
|------|------|
| 1 | Run `prepare_video.py` on scripts 01–04 |
| 2 | Batch ElevenLabs voiceover for all 4 |
| 3–4 | Batch B-roll generation (Runway) + stock download |
| 5–6 | Assemble video 01 + 02 in CapCut |
| 7–8 | Assemble video 03 + 04 |
| 9 | Thumbnails × 3 for each (12 total) |
| 10 | Upload all 4, schedule Tue/Fri for 2 weeks |
| 11 | Opus Clip → 12 Shorts, schedule |

---

## Monthly AI Tool Budget (Estimated)

| Tool | Plan | Cost/month |
|------|------|------------|
| ElevenLabs | Creator | ~$22 |
| **HeyGen** | **Creator** | **~$24** |
| CapCut | Pro | ~$10 |
| **Higgsfield** | **Plus** | **~$49** |
| Opus Clip | Pro | ~$29 |
| **Total** | | **~$134/month** |

Free tier alternative: HeyGen free (watermarked) + Higgsfield free credits + CapCut free.

---

*AI Production Playbook v1.0 — Saudi Gateway*
