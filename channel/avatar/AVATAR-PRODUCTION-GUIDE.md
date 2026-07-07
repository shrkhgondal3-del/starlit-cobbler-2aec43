# Saudi Gateway — Avatar Production Guide

How to create, train, and use **Charlotte Hayes** across all videos.

---

## Recommended Format: Hybrid Avatar + Documentary

| Segment | Format | Duration per 15-min video |
|---------|--------|---------------------------|
| **Hook** | Charlotte Hayes, direct to camera | 0:00–0:35 |
| **Chapter bridges** | Avatar (5–10 sec) | ~60 sec total |
| **Chapter body** | B-roll + motion graphics + voiceover | ~12 min |
| **Key warnings** | Avatar emphasis | ~15 sec |
| **Close + CTA** | Avatar | 0:30–0:45 |

**Result:** ~2.5 min avatar / ~12.5 min B-roll.

---

## Cultural Sensitivity — Production Rules

Before publishing any Charlotte Hayes clip:

| Check | Requirement |
|-------|-------------|
| Wardrobe in frame | High neckline, sleeves to wrist, blazer on |
| Gestures | Composed — no exaggerated or flirtatious movement |
| HeyGen gesture setting | **Minimal** or **Disabled** |
| Script language | Respectful of Kingdom laws; say "the Kingdom" where natural |
| Same video B-roll | No alcohol, nightlife, or immodest stock near avatar cuts |
| Hook disclaimer | Mentions AI production + educational purpose |

Full guide: `CHARACTER-BIBLE.md` → Saudi Cultural Sensitivity section.

---

## Tool Stack

```
HeyGen          →  Avatar clips (Charlotte Hayes, modest professional look)
Higgsfield Soul →  Thumbnails + Shorts hooks (same face)
ElevenLabs      →  British female voice clone ("Charlotte" or "Alice")
Higgsfield MCP  →  B-roll
CapCut          →  Assembly
```

---

## Step-by-Step: Create Charlotte Hayes Avatar

### Phase 1 — Generate reference images (30 min)

Use prompts in `content/ai-prompts/AVATAR-REFERENCE-PROMPTS.md` (Images 01–08).

**Quality gate:**
- Same face in all 8 images
- Modest neckline and sleeves in every shot
- Discard any image that looks revealing or inconsistent

Save to `channel/avatar/charlotte-hayes-reference/`.

---

### Phase 2A — Train on HeyGen (20 min)

1. [heygen.com](https://heygen.com) → Avatars → **Photo Avatar**
2. Upload 8 reference images
3. Name: `Charlotte Hayes - Saudi Gateway`
4. **Voice:** ElevenLabs clone (British female) — see Phase 3
5. Test script:

```
If you've heard that foreigners can't buy property in Saudi Arabia, you're working with outdated information. I'm Charlotte Hayes from Saudi Gateway, and we help foreign investors navigate property and business in the Kingdom — with respect for Saudi law and culture.
```

6. Save Avatar ID → `avatar/charlotte-hayes-heygen-avatar-id.txt`

**HeyGen settings:**
| Setting | Value |
|---------|-------|
| Aspect ratio | 16:9 + 9:16 for Shorts |
| Background | Custom office plate (see reference prompts) |
| Gesture style | **Minimal** — critical for cultural tone |
| Talking speed | 0.95x |

---

### Phase 2B — Train Soul Character on Higgsfield (15 min)

```
Train a Soul Character named "Charlotte Hayes" from these reference photos.
Elegant British female investment advisor, age 37, navy blazer, high-neck cream blouse, modest professional attire.
```

Save ID → `avatar/charlotte-hayes-soul-character-id.txt`

---

### Phase 3 — Voice clone in ElevenLabs (15 min)

1. ElevenLabs voice: **Charlotte** (British) or **Alice** as base
2. Generate 3 min from Script 01 hook + close
3. Voice Lab → Instant Voice Clone → `Charlotte Hayes - Saudi Gateway`
4. Use in HeyGen + all B-roll narration

Save ID → `avatar/charlotte-hayes-voice-clone-id.txt`

---

### Phase 4 — Produce clips per video

Use `content/scripts/01-foreigners-buy-property-ksa-AVATAR.md` for ready-to-paste scripts.

| Clip | Length |
|------|--------|
| hook.mp4 | 30–35 sec |
| bridge-*.mp4 | 5–8 sec each |
| myth-emphasis.mp4 | 12–15 sec |
| close.mp4 | 40–45 sec |

---

### Phase 5 — CapCut assembly

```
[0:00]  hook.mp4 (Charlotte)
[0:35]  B-roll + VO
[...]   bridges + B-roll alternating
[14:00] close.mp4 (Charlotte)
```

---

## Shorts

Open every Short with Charlotte (3–5 sec, 9:16), then B-roll. Scripts in AVATAR script file.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Avatar feels "too glamorous" for topic | Reduce makeup in reference images; simpler hair |
| Concern from Saudi viewers | Verify modest dress in every frame; optional hijab variant Phase 2 |
| Voice too soft | Increase ElevenLabs stability to 0.70; slight clarity boost |
| Lip sync on long clips | Keep clips under 45 sec |

---

*Avatar production guide v2.0 — Charlotte Hayes*
