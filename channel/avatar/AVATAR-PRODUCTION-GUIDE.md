# Saudi Gateway — Avatar Production Guide

How to create, train, and use **James Reid** across all videos.

---

## Recommended Format: Hybrid Avatar + Documentary

The highest-performing format for finance/property YouTube in 2026:

| Segment | Format | Duration per 15-min video |
|---------|--------|---------------------------|
| **Hook** | Avatar (James, direct to camera) | 0:00–0:30 |
| **Chapter intros** | Avatar (5–10 sec bridge) | ~60 sec total |
| **Chapter body** | B-roll + motion graphics + voiceover | ~12 min |
| **Key warnings / myths** | Avatar (emphasis moment) | ~30 sec |
| **Close + CTA** | Avatar (subscribe, checklist) | 0:30–1:00 |

**Result:** ~2.5 min avatar / ~12.5 min B-roll — trust of a host + depth of documentary.

---

## Tool Choice: HeyGen vs Higgsfield Soul

| Factor | HeyGen | Higgsfield Soul Character |
|--------|--------|---------------------------|
| **Avatar quality** | Industry-leading lip sync (Avatar IV) | Good, improving fast |
| **Long-form** | Up to 5+ min per clip | Shorter clips (~15 sec–1 min) |
| **Agent/MCP control** | API only | Native MCP (`create_character`, `generate_video`) |
| **Voice clone** | Built-in | Use ElevenLabs + sync |
| **Thumbnail stills** | Export frame | Soul generates consistent images |
| **Price** | ~$24/mo Creator | Included in Higgsfield Plus $49 |
| **Best for** | Long avatar segments (hooks, closes) | Character training + Shorts + thumbs |

### Recommended stack (use both)

```
HeyGen          →  Long avatar clips (hook 30s, close 45s, chapter bridges 8s each)
Higgsfield Soul →  Train same face for thumbnails, Shorts hooks, social stills
ElevenLabs      →  Voice clone used in BOTH tools
Higgsfield MCP  →  B-roll (Kling/Veo) + I orchestrate the full pipeline
CapCut          →  Stitch avatar + B-roll on timeline
```

**If budget is tight ($49 only):** Higgsfield Soul only — shorter avatar clips, accept less lip-sync polish on long segments.

**If quality is priority ($73/mo):** HeyGen Creator ($24) + Higgsfield Plus ($49).

---

## Step-by-Step: Create James Reid Avatar

### Phase 1 — Generate reference images (30 min)

Use **Higgsfield Soul**, **Midjourney**, or **Ideogram** to create 8–12 reference photos.

**Master prompt (repeat with expression/angle variations):**

```
Professional headshot of a confident British businessman age 42, short dark brown hair with grey at temples, clean-shaven, navy blazer over white open-collar shirt, soft studio lighting, blurred modern office window with city skyline background, looking at camera, trustworthy expression, corporate video presenter style, photorealistic, 85mm portrait lens, shallow depth of field, no text, no watermark
```

**Variations to generate (one prompt each):**
1. Neutral confident (default)
2. Slight smile, welcoming
3. Thoughtful, hand near chin
4. Serious, explaining (brows slightly engaged)
5. 3/4 angle left
6. 3/4 angle right
7. Straight on, wider framing (chest up)
8. Same as #1 but 9:16 vertical crop composition

**Quality gate:** All 8 must look like the **same person**. Discard any that drift.

Save to `channel/avatar/james-reid-reference/`.

---

### Phase 2A — Train on HeyGen (20 min)

1. Go to [heygen.com](https://heygen.com) → **Avatars** → **Create Instant Avatar** or **Photo Avatar**
2. Upload 8–12 reference images from Phase 1
3. Name: `James Reid - Saudi Gateway`
4. **Voice:** Upload ElevenLabs voice clone OR select "George" (British)
5. Test with 30-second script:

```
If you've heard that foreigners can't buy property in Saudi Arabia, you're working with outdated information. I'm James Reid, and on Saudi Gateway we break down exactly what foreign investors need to know about property and business in the Kingdom.
```

6. Review lip sync, eye contact, gestures — regenerate if uncanny
7. Save **Avatar ID** to `avatar/james-reid-heygen-avatar-id.txt`

**HeyGen settings for Saudi Gateway:**
| Setting | Value |
|---------|-------|
| Aspect ratio | 16:9 (also export 9:16 for Shorts) |
| Background | Custom: upload navy studio image OR blur office |
| Gesture style | Minimal / professional |
| Talking speed | 0.95x |

---

### Phase 2B — Train Soul Character on Higgsfield (15 min)

*Skip if using HeyGen only. Do this if you connected Higgsfield MCP.*

Via Higgsfield app or MCP prompt:
```
Train a Soul Character named "James Reid" from these reference photos.
Professional British investment advisor, navy blazer, white shirt, age 42.
Use for consistent character across images and short video clips.
```

Or MCP tool: `create_character` with uploaded references.

Save character ID to `avatar/james-reid-soul-character-id.txt`.

**Use Soul for:**
- Thumbnail face stills (same face every video)
- 15-second Shorts hooks
- Instagram/LinkedIn promotional images

---

### Phase 3 — Voice clone in ElevenLabs (15 min)

1. Generate 3 minutes of clean speech (Script 01 hook + close, no music)
2. ElevenLabs → **Voice Lab** → **Instant Voice Clone**
3. Name: `James Reid - Saudi Gateway`
4. Use this voice ID in:
   - HeyGen avatar voice setting
   - ElevenLabs B-roll narration (so avatar + voiceover match)

Save ID to `avatar/james-reid-voice-clone-id.txt`.

---

### Phase 4 — Produce avatar clips per video (45 min)

For each long-form video, generate these **HeyGen clips** separately:

| Clip | Script source | Target length |
|------|---------------|---------------|
| `hook.mp4` | Script HOOK section | 25–35 sec |
| `bridge-ch1.mp4` | "Let's start with how the rules actually changed." | 5–8 sec |
| `bridge-ch2.mp4` | Chapter 2 one-liner bridge | 5–8 sec |
| ... | One bridge per chapter (optional — min 3) | 5–8 sec |
| `myth-emphasis.mp4` | "Here's what most people get wrong." | 10–15 sec |
| `close.mp4` | Script CLOSE section | 30–45 sec |

**Tip:** Generate all clips in one HeyGen session while avatar settings are fresh.

---

### Phase 5 — Assemble in CapCut (hybrid timeline)

```
Timeline:
[0:00]  hook.mp4          ← AVATAR
[0:30]  broll + VO ch1    ← DOCUMENTARY
[2:20]  bridge-ch2.mp4    ← AVATAR (8 sec)
[2:28]  broll + VO ch2    ← DOCUMENTARY
...
[14:00] myth-emphasis.mp4 ← AVATAR
[14:15] broll montage     ← DOCUMENTARY
[15:00] close.mp4         ← AVATAR
```

**Transitions:** Simple cut or 0.3s cross-dissolve — no flashy wipes.

---

## Shorts With Avatar

Every Short should open with **James Reid face + hook** for 3–5 seconds, then cut to B-roll.

| Seconds | Content |
|---------|---------|
| 0–3 | Avatar: bold hook line |
| 3–45 | B-roll + captions + voiceover |
| 45–50 | Avatar or end card: "Full guide on Saudi Gateway" |

Generate Shorts avatar hooks in **HeyGen 9:16** or **Higgsfield Soul** vertical.

---

## Avatar Clip Scripts — Video 01 (Ready to Paste)

### hook.mp4 (30 sec)
```
If you've heard that foreigners can't buy property in Saudi Arabia — you're working with outdated information. In 2026, the rules have changed dramatically. Depending on your nationality, residency status, and where you want to buy, you may have more options than you think. I'm James Reid from Saudi Gateway, and in the next fifteen minutes I'll walk you through exactly who can buy, where, what it costs, and the mistakes that catch foreign buyers off guard.
```

### bridge-premium-residency.mp4 (8 sec)
```
The most important pathway for many foreigners is Premium Residency. Here's how it works.
```

### bridge-designated-zones.mp4 (8 sec)
```
If you don't have Premium Residency, designated development zones are your main option. Let me break down what to verify.
```

### myth-emphasis.mp4 (12 sec)
```
Five mistakes I see constantly. Number one: assuming Dubai rules apply in Saudi Arabia. They don't. This is a completely separate legal system.
```

### close.mp4 (40 sec)
```
Saudi Arabia's property market for foreigners is real and growing — but it's not a free-for-all. Your eligibility depends on your status, the zone, and the specific project. Download our free Foreign Buyer's Checklist — link below. Subscribe for next week's guide on starting a business in Saudi Arabia as a foreigner. Comment below with your situation — we read every one.
```

---

## Monthly Avatar Production Checklist

Per 2 long-form videos/week:

| Task | Time | Tool |
|------|------|------|
| 2× hook clips | 20 min | HeyGen |
| 2× close clips | 20 min | HeyGen |
| 6–10× bridge clips | 30 min | HeyGen |
| 6× Shorts avatar hooks | 20 min | HeyGen or Soul |
| 6× thumbnail face stills | 15 min | Higgsfield Soul |
| **Total** | **~2 hrs/week** | |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Lip sync drifts on long clips | Keep avatar clips under 45 sec; split into segments |
| Face looks different between videos | Re-use same HeyGen avatar ID; never retrain unless intentional |
| Voice doesn't match B-roll | Use same ElevenLabs clone for avatar + narration |
| Uncanny valley / distrust | Reduce gesture intensity; use avatar for hooks only (30% format) |
| YouTube synthetic media flag | Enable disclosure; add spoken disclaimer in hook |

---

*Avatar production guide v1.0*
