# Saudi Gateway — Brand Guide

## Brand Essence

**Tone:** Authoritative, calm, premium — not hype-driven. Think *Financial Times meets practical how-to*, not "get rich in Dubai" energy.

**Voice principles:**
- Lead with facts, then implications
- Say "it depends" when it does — builds trust
- Use "you" to speak directly to the foreign viewer
- Avoid superlatives ("amazing," "insane opportunity") unless quoting official programs
- Always distinguish **law** vs. **practice** vs. **rumor**

## Visual Identity

### Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| **Saudi Green** (primary) | `#006C35` | Accents, CTAs, lower-thirds |
| **Desert Gold** (secondary) | `#C5A572` | Highlights, icons, dividers |
| **Deep Navy** (background) | `#0D1B2A` | Thumbnails, end screens, banner |
| **Sand** (neutral) | `#F5F0E8` | Lower thirds text backgrounds |
| **White** | `#FFFFFF` | Primary text on dark |
| **Alert Red** | `#C0392B` | Warnings, "myth busted" stamps only |

### Typography

| Use | Font | Weight |
|-----|------|--------|
| Thumbnails & titles | **Montserrat** | Bold / ExtraBold |
| Body & lower-thirds | **Inter** | Regular / Medium |
| Arabic subtitles | **Noto Sans Arabic** | Regular |

Download: [Google Fonts](https://fonts.google.com)

### Logo Concept

Wordmark: **SAUDI** (white) + **GATEWAY** (gold) on navy background.  
Icon: Minimal arched gateway silhouette (suggestive of historic Diriyah architecture — not a literal flag).

**Do not:** Use the Saudi flag as a logo element. Use green/gold palette as cultural reference only.

## Thumbnail System (Avatar Face — Charlotte Hayes)

Use **Charlotte Hayes** on every thumbnail — same trained face builds recognition and lifts CTR.

**Pipeline:** HeyGen/Soul still export → Canva text overlay → 1280×720

Prompts: `content/ai-prompts/AVATAR-REFERENCE-PROMPTS.md` (Image 10) + `THUMBNAIL-PROMPTS.md`

### Layout (1280×720)

```
┌─────────────────────────────────────────┐
│  [JAMES REID FACE — left 40%]     [BADGE]│
│                                         │
│  BIG TITLE LINE 1 (3-4 words)           │
│  subtitle line (gold, smaller)          │
│                                         │
│  ─── green accent bar bottom ───        │
│  SAUDI GATEWAY (small watermark)        │
└─────────────────────────────────────────┘
```

### Rules
1. **Same face every video** — export from HeyGen avatar or Higgsfield Soul
2. **Max 6 words** in main title — add text in Canva only
3. **Expression:** confident/serious, direct eye contact
4. **Badge** top-right: "2026" / "FOREIGNERS" / "STEP BY STEP"
5. **3 variants** per video for YouTube Test & Compare

### Thumbnail Title Formulas

| Video type | Formula | Example |
|------------|---------|---------|
| Explainer | `[Topic] for Foreigners` | `Buy Property in KSA` |
| How-to | `How to [Action] in Saudi Arabia` | `How to Get a MISA License` |
| Myth-bust | `[Myth]? (Truth)` | `Foreigners Can't Buy? (Truth)` |
| List | `[N] Things You Must Know` | `7 Business Setup Mistakes` |
| Update | `[Topic] — 2026 Changes` | `RHQ Rules — 2026 Changes` |

## Video Production Standards (AI-Only)

**Format:** AI Documentary — ElevenLabs voiceover + Runway/Pexels B-roll + Canva motion graphics

Full pipeline: `operations/AI-PRODUCTION-PLAYBOOK.md`

### Intro (8 seconds max)
- 2-second logo sting (Canva animation template)
- AI voice (ElevenLabs): *"Welcome to Saudi Gateway — your path to property and business in Saudi Arabia. This video uses AI-assisted production. Educational purposes only."*
- Disclaimer card on screen (3 sec)

### On-screen elements
- **Lower third:** Chapter title, green bar (Canva template)
- **Source citations:** REGA/MISA/ZATCA URL on screen when citing regulations
- **Chapter markers:** Every 2–3 minutes
- **End screen:** Last 20 seconds — subscribe + next video + checklist link
- **Cut rhythm:** New visual every 4–6 seconds (critical for AI retention)

### Audio
- **Voice:** ElevenLabs — Charlotte or Alice (British female), stability 0.65, speed 0.95
- **Music:** CapCut royalty-free or Epidemic Sound — **-20dB under voice**
- **No mic needed**

### B-roll sources (priority order)
1. Pexels/Storyblocks real Saudi footage
2. Runway Gen-3 AI clips (`content/ai-prompts/BROLL-PROMPTS.md`)
3. Canva motion graphics for charts and flowcharts
- NEOM/giga-projects: always label **"Artist impression"** on screen

## Social & Channel Assets

### YouTube Banner (2560×1440)
- Safe zone (visible on all devices): center 1546×423
- Text: **Saudi Gateway** | *Property & Business in Saudi Arabia for Foreigners*
- CTA: *New videos every Tuesday & Friday*
- Upload schedule badge

### Profile Picture (800×800)
- Gateway icon on navy circle, or presenter headshot with green ring

### Watermark
- Small "SG" monogram, bottom-right, appears last 15 seconds

## Description Boilerplate (paste below every video)

```
🇸🇦 Saudi Gateway — helping foreigners navigate property and business in Saudi Arabia.

📋 FREE CHECKLIST: [link to hub page]
📧 Consultation inquiries: [email]

⏱ CHAPTERS:
[auto-generated or manual]

🔗 OFFICIAL SOURCES:
[list relevant MISA/REGA/ZATCA links]

⚠️ DISCLAIMER: This video is for educational purposes only and is not legal, tax, or investment advice. Regulations change — verify with licensed professionals in KSA.

#SaudiArabia #SaudiBusiness #SaudiProperty #Vision2030 #MISA #ForeignInvestment

━━━ ABOUT SAUDI GATEWAY ━━━
We produce clear, current guides for foreign investors, entrepreneurs, and expats interested in Saudi Arabia's property market and business environment. Subscribe for weekly updates.

━━━ CONNECT ━━━
Website: [hub URL]
LinkedIn: [handle]
Instagram: [handle]
```

## Shorts Format

- **Duration:** 30–55 seconds
- **Hook:** First 2 seconds = bold text on screen + verbal hook
- **Structure:** Hook → 1 insight → CTA ("Full guide on our channel")
- **Captions:** Always on, large font, center-bottom
- **Reuse:** Cut from long-form — do not create unique Shorts-only content in Phase 1 (efficiency)

## AI Voice Profile (Lock for All Videos)

| Setting | Value |
|---------|-------|
| Tool | ElevenLabs Multilingual v2 |
| Voice | Charlotte or Alice (British female) — glamorous, composed, professional |
| Stability | 0.65 |
| Similarity | 0.80 |
| Style | 0.15 |
| Speed | 0.95 |
| Pace | 140–160 words/minute |

Do not change voice between videos — consistency builds brand recognition.

## AI Disclosure (Brand Requirement)

Every video must include:
1. **Spoken** in intro: "AI-assisted production"
2. **On-screen** disclaimer card (first 5 seconds)
3. **Written** in YouTube description (see SEO playbook boilerplate)
4. **YouTube upload:** altered/synthetic content disclosure enabled

---

*AI brand assets: generate in Ideogram/Canva — see `content/ai-prompts/`*
