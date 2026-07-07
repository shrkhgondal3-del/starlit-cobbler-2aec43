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
| **Production** | Agent-automated: HeyGen + Higgsfield + ElevenLabs + FFmpeg assembly |
| **Host** | Charlotte Hayes — glamorous British presenter (modest, culturally respectful) |

## Repository Structure

```
channel/
├── README.md                         ← You are here
├── strategy/
│   └── CHANNEL-STRATEGY.md
├── avatar/
│   ├── CHARACTER-BIBLE.md           ← Charlotte Hayes host spec
│   └── AVATAR-PRODUCTION-GUIDE.md   ← HeyGen + Soul setup
│   └── BRAND-GUIDE.md                ← AI visual identity + thumbnails
├── content/
│   ├── CONTENT-CALENDAR.md
│   ├── scripts/                      ← Source scripts
│   └── ai-prompts/                   ← B-roll, thumbnail, script AI prompts
├── automation/
│   ├── run_pipeline.py             ← Orchestrator
│   ├── assemble_video.py           ← FFmpeg assembly (no CapCut)
│   ├── elevenlabs_generate.py      ← Voice API
│   └── projects/                   ← Per-video production folders
├── operations/
│   ├── ZERO-MANUAL-ASSEMBLY.md     ← ★ What you do vs what agent does
│   ├── AI-PRODUCTION-PLAYBOOK.md
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
3. **Day 2** — Agent generates voiceovers (ElevenLabs API) + B-roll (Higgsfield MCP) + avatar (HeyGen)
4. **Day 3** — Agent runs `assemble_video.py` → `final.mp4` ready for your YouTube upload

**Full guide:** `operations/ZERO-MANUAL-ASSEMBLY.md`

## AI Tool Stack (~$95/mo — no CapCut, no Canva)

| Tool | Purpose | Who operates |
|------|---------|--------------|
| ElevenLabs Creator | Voice clone + API | Agent |
| HeyGen Creator | Charlotte avatar | Agent (with API) |
| Higgsfield Plus | B-roll + MCP | Agent |
| FFmpeg | Video assembly | Agent (built-in) |
| YouTube | Publish | You (5 min upload) |

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

| Fully automated by agent | You do once |
|--------------------------|-------------|
| Scripts, SEO, shot lists | Sign up + pay for tools |
| ElevenLabs voiceover (API) | `ELEVENLABS_API_KEY` in Cursor |
| Higgsfield B-roll (MCP) | Connect `https://mcp.higgsfield.ai/mcp` |
| HeyGen avatar clips | Train Charlotte once in HeyGen |
| FFmpeg assembly → `final.mp4` | YouTube upload (~5 min) |
| Subtitles + chapters file | Approve video before publish |

## AI Disclosure (Required on Every Video)

> This video was created with AI-assisted production (voiceover and visuals). Content is researched from official Saudi government sources. Educational purposes only — not legal or investment advice.

Enable YouTube **altered/synthetic content** disclosure on upload.

---

**Next step:** Open `operations/AI-PRODUCTION-PLAYBOOK.md` and produce Video 01.
