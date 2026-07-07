# Saudi Gateway — AI-Only Launch Checklist

Complete every item in order. **No camera or microphone needed.**

---

## Phase 0: AI Tool Setup (Before Day 1)

- [ ] **Google account** for YouTube channel
- [ ] **HeyGen** Creator plan — create Charlotte Hayes avatar (see `avatar/AVATAR-PRODUCTION-GUIDE.md`)
- [ ] **ElevenLabs** Creator — voice clone for Charlotte Hayes
- [ ] **Higgsfield** Plus + MCP connector (`https://mcp.higgsfield.ai/mcp`) — B-roll + Soul character
- [ ] **CapCut** Pro
- [ ] **Canva** Pro — brand kit + lower thirds
- [ ] Generate 8 reference images using `content/ai-prompts/AVATAR-REFERENCE-PROMPTS.md`

---

## Day 1: Channel + AI Brand Assets

- [ ] Create YouTube channel **Saudi Gateway** → handle `@SaudiGateway`
- [ ] Generate **profile picture** in Ideogram:
  ```
  Minimal arched gateway logo icon, Saudi inspired architecture, gold on deep navy circle, clean modern, no text, app icon style
  ```
- [ ] Generate **banner** in Canva (2560×1440) — use brand colors, add text in Canva
- [ ] Set channel description (include AI disclosure):

```
Saudi Gateway helps foreigners buy property and start businesses in Saudi Arabia.

AI-assisted production | Researched from official sources (MISA, REGA, ZATCA)
New videos every Tuesday & Friday

⚠️ Educational content only — not legal or investment advice.
📋 Free checklists: [HUB URL]
```

- [ ] Create 4 playlists (Property, Business, Regulations, Market Updates)
- [ ] Enable YouTube upload defaults: Education category, auto-chapters ON

---

## Day 2: Produce Video 01 with AI

- [ ] Run automation:
  ```bash
  python3 channel/automation/prepare_video.py channel/content/scripts/01-foreigners-buy-property-ksa.md
  ```
- [ ] Open `channel/automation/output/01-foreigners-buy-property-ksa/production_brief.md`
- [ ] **ElevenLabs:** paste each `voiceover_chapters/*.txt` → export MP3s
- [ ] **Runway:** generate clips from `broll_shotlist.json` prompts
- [ ] **Pexels:** download stock for any weak AI clips (search terms in shotlist)
- [ ] **Canva:** create disclaimer card + 4-pathways flowchart + source cards
- [ ] Lawyer review of `voiceover.txt` (optional but recommended for regulation claims)

---

## Day 3: Assemble & Thumbnail Video 01

- [ ] **CapCut assembly** per `production_brief.md`:
  - Import MP3s sequentially
  - Lay B-roll (cut every 4–6 sec)
  - Overlay graphics at key moments
  - Background music at -20dB
  - Auto-caption → fix REGA, MISA, ZATCA spelling
- [ ] Export 1080p H.264
- [ ] **Ideogram + Canva:** 3 thumbnail variants (see `ai-prompts/THUMBNAIL-PROMPTS.md` Video 01)
- [ ] Copy SEO title, description, tags from `operations/SEO-PLAYBOOK.md`

---

## Day 4: Publish Video 01 + Shorts

- [ ] Upload to YouTube Studio
- [ ] **Enable altered/synthetic content disclosure**
- [ ] Add chapters from `production_brief.md` timestamps
- [ ] Upload 3 thumbnails → Test & Compare
- [ ] Auto-translate captions to Arabic
- [ ] Add end screen + cards
- [ ] Pin comment with checklist link
- [ ] **Opus Clip:** upload long-form → generate 3 Shorts → publish 2, schedule 1

---

## Day 5: Hub Page + Video 02 AI Production

- [ ] Deploy `channel/hub/index.html` (GitHub Pages / Netlify)
- [ ] Connect email form (Formspree/Mailchimp)
- [ ] Run `prepare_video.py` on Script 02
- [ ] Batch ElevenLabs + Runway for Video 02

---

## Day 6–7: Publish Video 02

- [ ] CapCut assemble Video 02
- [ ] AI thumbnails × 3
- [ ] Publish + cross-link with Video 01
- [ ] Opus Clip → 3 Shorts from Video 02

---

## Week 2+: Automated Cadence

Follow `operations/WEEKLY-WORKFLOW.md` — 2 AI long-form + 3 AI Shorts per week.

### Batch tip (produce 2 weeks ahead)
```bash
python3 channel/automation/prepare_video.py channel/content/scripts/0*.md
# Then batch all ElevenLabs → batch all Runway → assemble 4 videos
```

---

## Day 30 AI Success Criteria

| Goal | Target |
|------|--------|
| AI long-form published | 8+ |
| AI Shorts published | 12+ |
| Subscribers | 500+ |
| Total views | 15,000+ |
| Avg. production time per video | < 4 hours |
| Hub email signups | 25+ |

---

*AI Launch Checklist v2.0*
