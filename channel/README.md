# Saudi Gateway — YouTube Channel Operations Hub

**100% AI-produced channel.** No camera, no human presenter. Scripts → AI voice → AI/stock visuals → automated edit → publish.

A complete launch-and-growth system for a YouTube channel targeting **foreign investors, expats, and entrepreneurs** interested in **KSA real estate** and **business setup in Saudi Arabia**.

## Channel Identity

| Element | Value |
|---------|-------|
| **Channel Name** | Saudi Gateway |
| **Tagline** | Your path to property & business in Saudi Arabia |
| **Niche** | KSA property for foreigners + business formation & licensing |
| **Primary Audience** | UK/EU/US/GCC expats, diaspora, remote founders, family offices |
| **Upload Cadence** | 2 long-form videos/week + 3 Shorts/week |
| **Language** | English (Arabic subtitles via YouTube auto-translate) |
| **Production** | AI-only (ElevenLabs + Runway/CapCut + Opus Clip) |

## Repository Structure

```
channel/
├── README.md                         ← You are here
├── strategy/
│   └── CHANNEL-STRATEGY.md
├── brand/
│   └── BRAND-GUIDE.md                ← AI visual identity + thumbnails
├── content/
│   ├── CONTENT-CALENDAR.md
│   ├── scripts/                      ← Source scripts
│   └── ai-prompts/                   ← B-roll, thumbnail, script AI prompts
├── automation/
│   ├── prepare_video.py              ← Script → voiceover + shot list + brief
│   └── output/                       ← Generated production assets per video
├── operations/
│   ├── AI-PRODUCTION-PLAYBOOK.md     ← ★ START HERE for AI pipeline
│   ├── LAUNCH-CHECKLIST.md
│   ├── SEO-PLAYBOOK.md
│   └── WEEKLY-WORKFLOW.md            ← AI-only weekly cycle
└── hub/
    └── index.html
```

## Quick Start — AI Pipeline (First 3 Days)

1. **Day 1** — Create YouTube channel `@SaudiGateway` + subscribe to AI tools (~$109/mo — see playbook)
2. **Day 1** — Run automation on Script 01:
   ```bash
   python3 channel/automation/prepare_video.py channel/content/scripts/01-foreigners-buy-property-ksa.md
   ```
3. **Day 2** — Paste `output/.../voiceover_chapters/*.txt` into **ElevenLabs** → export MP3s
4. **Day 2** — Generate B-roll from `broll_shotlist.json` prompts in **Runway** + download **Pexels** stock
5. **Day 3** — Assemble in **CapCut**, auto-caption, AI thumbnails in **Ideogram + Canva**, publish + 3 Shorts via **Opus Clip**

**Full guide:** `operations/AI-PRODUCTION-PLAYBOOK.md`

## AI Tool Stack (Monthly ~$109)

| Tool | Purpose |
|------|---------|
| ElevenLabs | AI voiceover (locked voice profile) |
| CapCut Pro | Edit, captions, assembly |
| Runway | AI B-roll generation |
| Canva Pro | Motion graphics + thumbnail text |
| Ideogram | Thumbnail base images |
| Opus Clip | Auto-generate Shorts from long-form |

Free alternative: CapCut free + Pexels stock + YouTube auto-translate.

## Success Metrics (90-Day Targets)

| Metric | Target |
|--------|--------|
| Subscribers | 5,000+ |
| Total views | 150,000+ |
| Avg. watch time (long-form) | 8+ minutes |
| CTR (impressions → click) | 6%+ |
| Inbound leads (consultation form) | 50+ |
| Videos published (AI) | 24 long-form + 36 Shorts |

## What Runs on AI vs. What You Approve

| Fully AI-automated | You approve once |
|--------------------|------------------|
| Script → voiceover conversion (`prepare_video.py`) | AI tool subscriptions / API keys |
| ElevenLabs narration | YouTube channel ownership |
| B-roll generation (Runway + stock) | Legal review of regulation claims |
| CapCut assembly + captions | Upload & schedule in YouTube Studio |
| Thumbnails (Ideogram + Canva) | Enable synthetic content disclosure |
| Shorts extraction (Opus Clip) | Email/CRM on hub page |
| SEO titles, descriptions, tags | Domain for hub page |

## AI Disclosure (Required on Every Video)

> This video was created with AI-assisted production (voiceover and visuals). Content is researched from official Saudi government sources. Educational purposes only — not legal or investment advice.

Enable YouTube **altered/synthetic content** disclosure on upload.

---

**Next step:** Open `operations/AI-PRODUCTION-PLAYBOOK.md` and produce Video 01.
