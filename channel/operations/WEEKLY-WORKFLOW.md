# Saudi Gateway — AI-Only Weekly Workflow

Repeat this cycle every week. **Total time: ~4–6 hours/week** with AI pipeline (vs. 12–16 hours manual).

**No camera. No presenter. No recording.**

---

## Monday — Analytics & Short #1 (45 min)

| Time | Task | Tool |
|------|------|------|
| 15 min | Review YouTube analytics: CTR, AVD, traffic sources | YouTube Studio |
| 15 min | Confirm this week's 2 topics from content calendar | Repo |
| 15 min | Run regulation check — any MISA/REGA updates? | Official portals + AI research |
| 30 min | Opus Clip → extract & publish **Short #1** from last long-form | Opus Clip |
| 15 min | AI-reply to comments (draft in ChatGPT, post manually) | ChatGPT |

**Output:** Short #1 live, week confirmed

---

## Tuesday — Generate Long-Form #1 (2 hrs)

| Time | Task | Tool |
|------|------|------|
| 10 min | Run `prepare_video.py` on this week's script #1 | Automation |
| 45 min | Paste chapter texts into ElevenLabs → export all MP3s | ElevenLabs |
| 45 min | Generate B-roll from `broll_shotlist.json` + Pexels stock | Runway + Pexels |
| 20 min | Create motion graphics (flowcharts, source cards, disclaimer) | Canva |

**Output:** All assets ready for assembly

---

## Wednesday — Assemble & Publish Long-Form #1 (2 hrs)

| Time | Task | Tool |
|------|------|------|
| 90 min | CapCut assembly: audio → B-roll → graphics → music → captions | CapCut |
| 20 min | Generate 3 AI thumbnails | Ideogram + Canva |
| 15 min | Upload, SEO description, chapters, end screen, synthetic disclosure | YouTube Studio |
| 15 min | Opus Clip → **Short #2** | Opus Clip |

**Output:** Long-form #1 live, Short #2 scheduled

---

## Thursday — Generate Long-Form #2 (2 hrs)

| Time | Task | Tool |
|------|------|------|
| 10 min | `prepare_video.py` on script #2 | Automation |
| 45 min | ElevenLabs voiceover batch | ElevenLabs |
| 45 min | B-roll batch generation | Runway + Pexels |
| 20 min | Canva graphics | Canva |

**Output:** Assets for Friday video

---

## Friday — Assemble & Publish Long-Form #2 (2 hrs)

| Time | Task | Tool |
|------|------|------|
| 90 min | CapCut assembly + captions | CapCut |
| 20 min | 3 AI thumbnails | Ideogram + Canva |
| 15 min | Upload + full SEO package + Arabic auto-translate | YouTube Studio |
| 15 min | Schedule **Short #3** for Saturday | Opus Clip |

**Output:** Long-form #2 live

---

## Saturday — Short #3 & Batch (45 min)

| Time | Task | Tool |
|------|------|------|
| 15 min | Publish Short #3 | YouTube Studio |
| 15 min | Batch-run `prepare_video.py` on next week's scripts | Automation |
| 15 min | Update content tracker on hub page | Repo |

**Output:** Short #3 live, next week prepped

---

## Sunday — Batch Production (Optional, 3–4 hrs)

Use this day to get ahead:

1. ElevenLabs voiceover for 2–4 videos at once
2. B-roll batch in Runway (10+ clips)
3. Pre-assemble videos 1–2 in CapCut, export but don't publish
4. Generate 6–12 thumbnails in one Canva session

**Goal:** Always have 1–2 videos in the bank.

---

## AI Role Map (No Humans Required)

| Function | AI Tool | Human action |
|----------|---------|--------------|
| Scriptwriting | Claude/ChatGPT + repo scripts | Approve new topics |
| Script → voiceover | `prepare_video.py` | None |
| Narration | ElevenLabs | None |
| B-roll video | Runway / Kling | None |
| Stock footage | Pexels API / manual search | None |
| Motion graphics | Canva AI templates | None |
| Video assembly | CapCut / InVideo AI | None |
| Captions EN | CapCut auto-caption | Spot-check REGA/MISA spelling |
| Captions AR | YouTube auto-translate | None |
| Thumbnails | Ideogram + Canva | Pick A/B variant |
| Shorts | Opus Clip | None |
| SEO copy | Repo SEO playbook | Paste on upload |
| Comment replies | ChatGPT drafts | Copy-paste post |
| Community posts | ChatGPT | Paste in YouTube Community tab |

---

## Quality Gates (AI-Specific)

Before every publish:

- [ ] Voice sounds natural at chapter joins (no clicks/pops)
- [ ] No static frame > 5 seconds
- [ ] Disclaimer spoken in intro + on-screen card
- [ ] Regulation sources shown on screen with URL
- [ ] AI cityscapes labeled "artist impression" if not real footage
- [ ] REGA, MISA, ZATCA spelled correctly in captions
- [ ] YouTube synthetic/altered content disclosure enabled
- [ ] 3 thumbnail variants uploaded
- [ ] Arabic subtitles enabled (auto-translate)
- [ ] Description includes AI disclosure paragraph

---

## Monthly Review (First Sunday)

1. Export YouTube analytics CSV
2. Rank videos by CTR and AVD — re-thumb worst 2 (new Ideogram variants)
3. Retire scripts that underperform — generate replacements with `ai-prompts/SCRIPT-GENERATION-PROMPTS.md`
4. Review ElevenLabs voice — adjust stability if sounding robotic
5. Update hub page tracker

---

*AI Workflow v2.0 — zero human on-camera production*
