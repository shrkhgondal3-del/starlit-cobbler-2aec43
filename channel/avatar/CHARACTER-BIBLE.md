# Saudi Gateway — Avatar Character Bible

Your channel presenter: **James Reid**, AI-generated, consistent across every video.

---

## Character Profile

| Attribute | Specification |
|-----------|---------------|
| **Name** | James Reid |
| **Role** | Expat investment advisor — property & business in Saudi Arabia |
| **Age appearance** | 38–45 |
| **Gender** | Male (alternative: see "Variant B" below) |
| **Nationality vibe** | British/European international — relatable to UK/US/EU target audience |
| **Ethnicity** | Caucasian or ambiguous Mediterranean — neutral, professional |
| **Personality** | Calm professor, not sales rep. Confident, precise, warm but not hypey |
| **Wardrobe** | Navy blazer, open-collar white or light blue shirt. No tie. No suit. |
| **Setting** | Modern office with subtle Riyadh skyline through window (blurred), OR clean navy backdrop with green/gold accent |
| **Energy** | 140 words/min, measured pace, slight lean-in on key points |
| **Never** | Point at camera aggressively, exaggerated gestures, "influencer" energy, Saudi flag pin |

### Variant B (optional second host for A/B testing)
| Attribute | Specification |
|-----------|---------------|
| **Name** | Sarah Mitchell |
| **Role** | Same as James — corporate lawyer / investment advisor tone |
| **Wardrobe** | Tailored blazer, cream blouse, minimal jewelry |
| **Use when** | Property-heavy videos (audience skews slightly more female for lifestyle property) |

**Launch with James Reid only.** Add Sarah only after 10K subs if data supports it.

---

## Visual Reference Spec (for AI training)

When creating reference images for HeyGen or Higgsfield Soul, all photos must match:

```
- Same person across all 8–20 reference images
- Age: early 40s
- Hair: short, neat, dark brown with slight grey at temples (distinguishing feature)
- Face: clean-shaven or very light stubble
- Expression range: neutral, slight smile, thoughtful, confident (serious topics)
- Framing: head + shoulders, 16:9 and 9:16 crops
- Lighting: soft key light, professional studio, no harsh shadows
- Background: consistent blurred office OR solid navy #0D1B2A
- Clothing: SAME navy blazer + white shirt in all references
- No sunglasses, no hats, no logo clothing
```

---

## Voice Profile (must match avatar)

| Tool | Voice | Settings |
|------|-------|----------|
| **HeyGen** | Use avatar's built-in voice OR upload ElevenLabs clone | British RP or neutral British |
| **ElevenLabs** | "George" or "Daniel" | Stability 0.65, Speed 0.95 |
| **Rule** | Avatar lip-sync voice and ElevenLabs B-roll voice **must be the same person** | Clone once, use everywhere |

### Voice clone workflow (recommended)
1. Generate 3 minutes of clean ElevenLabs speech from Script 01 hook
2. Upload to HeyGen as custom voice for James Reid avatar
3. All avatar clips use this voice — seamless match with B-roll narration

---

## On-Screen Branding (Avatar shots)

| Element | Spec |
|---------|------|
| **Lower third** | `James Reid` / `Saudi Gateway` — green bar `#006C35` |
| **Background** | Blurred KAFD skyline OR navy studio with subtle gateway logo |
| **Disclaimer bug** | Small text bottom-left on first avatar appearance: "AI presenter · Educational only" |

---

## Thumbnail Usage

Once avatar is trained, **use James Reid's face on thumbnails** — faces increase CTR 15–25%.

| Rule | Detail |
|------|--------|
| Expression | Serious/confident, not smiling too wide |
| Position | Left 40% of frame |
| Text | Right side — max 4 words |
| Consistency | Same face every thumbnail — audience recognizes the host |

Update `content/ai-prompts/THUMBNAIL-PROMPTS.md` to use trained Soul/HeyGen stills instead of faceless skylines.

---

## Legal & Disclosure

Include on every video with avatar:

**Spoken (first avatar appearance):**
> "I'm James Reid, your guide on Saudi Gateway. This channel uses AI-assisted production, including this presenter. All content is educational — not legal or investment advice."

**Description:**
> 🤖 AI disclosure: Presenter and portions of this video are AI-generated. Content is researched from official Saudi government sources (MISA, REGA, ZATCA).

**YouTube upload:** Enable **altered/synthetic content** disclosure.

---

## File Naming Convention

```
avatar/
├── james-reid-reference/          # 8–20 training photos
├── james-reid-heygen-avatar-id.txt  # HeyGen avatar ID once created
├── james-reid-voice-clone-id.txt    # ElevenLabs voice ID
└── clips/                         # Exported avatar segments per video
    ├── 01-hook.mp4
    ├── 01-ch1-bridge.mp4
    └── 01-close.mp4
```

---

*Character bible v1.0 — James Reid is a fictional AI presenter for Saudi Gateway*
