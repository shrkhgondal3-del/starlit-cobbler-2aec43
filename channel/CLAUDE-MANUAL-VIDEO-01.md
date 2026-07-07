# Claude — Manual Video 01 Production (All Browser Tabs)

**Copy everything below this line and paste into Claude with Computer Use enabled.**

---

You are producing **Saudi Gateway Video 01** manually using my paid subscriptions in **Google Chrome**. Control the browser tabs. Only stop me for login, 2FA, or payment.

**Video:** Can Foreigners Buy Property in Saudi Arabia? (2026)  
**Presenter:** Charlotte Hayes — British, professional, modest dress  
**Format:** 1920×1080 (16:9), ~14 minutes

---

## PHASE 0 — Create folder on Desktop

Create this folder structure on my computer:

```
Desktop/Saudi-Gateway-Video-01/
├── avatar/          ← HeyGen exports (5 files)
├── broll/
│   ├── chapter-1/
│   ├── chapter-2/
│   ├── chapter-3/
│   ├── chapter-4/
│   ├── chapter-5/
│   ├── chapter-6/
│   ├── chapter-7/
│   └── chapter-8/
├── voiceover/       ← ElevenLabs MP3s (10 files)
└── output/          ← final assembled video
```

---

## TAB 1 — GitHub (scripts reference)

Open: **https://github.com/shrkhgondal3-del/starlit-cobbler-2aec43/tree/cursor/ksa-youtube-channel-launch-e56b**

Download or open these files for reference:
- `channel/content/scripts/01-foreigners-buy-property-ksa-AVATAR.md` (avatar scripts)
- `channel/automation/output/01-foreigners-buy-property-ksa/voiceover_chapters/` (all `.txt` files)

Keep this tab open for copy-paste.

---

## TAB 2 — ElevenLabs (voiceovers)

Open: **https://elevenlabs.io/app/speech-synthesis**

**Voice:** Alice (British) OR cloned Charlotte voice if available  
**Voice ID reference:** `Xb7hH8MSUJpSbSDYk0k2`

For each file below:
1. Open the matching `.txt` from GitHub voiceover_chapters
2. Paste full text into ElevenLabs
3. Generate → Download MP3
4. Save to `Desktop/Saudi-Gateway-Video-01/voiceover/` with **exact filename**:

| Save as | Source text file |
|---------|------------------|
| `hook-hook.mp3` | hook-hook.txt |
| `chapter-1-the-old-rule-vs-todays-reality.mp3` | chapter-1-the-old-rule-vs-todays-reality.txt |
| `chapter-2-gcc-nationals.mp3` | chapter-2-gcc-nationals.txt |
| `chapter-3-premium-residency-route.mp3` | chapter-3-premium-residency-route.txt |
| `chapter-4-designated-zones-developer-projects.mp3` | chapter-4-designated-zones-developer-projects.txt |
| `chapter-5-buying-through-a-saudi-company.mp3` | chapter-5-buying-through-a-saudi-company.txt |
| `chapter-6-the-purchase-process-step-by-step.mp3` | chapter-6-the-purchase-process-step-by-step.txt |
| `chapter-7-financing-mortgages.mp3` | chapter-7-financing-mortgages.txt |
| `chapter-8-common-mistakes.mp3` | chapter-8-common-mistakes.txt |
| `close-close.mp3` | close-close.txt |

**Settings:** Stability ~50%, Clarity ~75%, no extreme speed changes.

---

## TAB 3 — HeyGen (Charlotte avatar — 5 clips)

Open: **https://app.heygen.com**

### 3A — Create Charlotte if not done
1. **Avatars** → **Photo Avatar** → **Create**
2. Upload 8 photos (professional British woman, navy blazer, high-neck blouse, modest)
3. Name: **Charlotte Hayes - Saudi Gateway**

### 3B — Generate 5 avatar videos

Use **Create Video** → select **Charlotte Hayes** → **16:9** → **1080p**

| Export filename | Script (paste exactly) | ~Duration |
|-----------------|------------------------|-----------|
| `hook.mp4` | See HOOK script below | ~35 sec |
| `bridge-ch3.mp4` | For many non-GCC foreigners, Premium Residency is the most important pathway. Here's how it works. | ~8 sec |
| `bridge-ch4.mp4` | Without Premium Residency, designated development zones are the practical route. Here is what to verify on every project. | ~8 sec |
| `myth-emphasis.mp4` | Five mistakes I see constantly. Assuming Dubai rules apply here — they don't. Skipping REGA verification. Buying off-plan without escrow confirmation. Overlooking Premium Residency. And proceeding without a Saudi property lawyer. Don't let that be you. | ~15 sec |
| `close.mp4` | See CLOSE script below | ~45 sec |

**HOOK script for hook.mp4:**
```
If you've heard that foreigners can't buy property in Saudi Arabia — you're working with outdated information. In 2026, the rules have changed significantly. And depending on your nationality, residency status, and where you want to buy, you may have more options than you think.

I'm Charlotte Hayes from Saudi Gateway. This channel uses AI-assisted production. We present Saudi regulations with respect for the Kingdom's laws and culture. This video is for educational purposes only — not legal or investment advice.

Over the next fifteen minutes, I'll walk you through who can buy, where, what it costs, and the mistakes that catch foreign buyers off guard. Let's begin.
```

**CLOSE script for close.mp4:**
```
Saudi Arabia's property market for foreigners is real, growing, and regulated — but eligibility depends on your status, the zone, and the specific project.

Download our free Foreign Buyer's Property Checklist — link in the description. Subscribe for next week's guide on starting a business in Saudi Arabia as a foreigner.

Tell us in the comments: are you looking at Riyadh, Jeddah, or a giga-project? We read every one.

I'm Charlotte Hayes. See you on Saudi Gateway.
```

**HeyGen settings:** Minimal gestures, professional studio background, no watermark.

Download all 5 to `Desktop/Saudi-Gateway-Video-01/avatar/`

---

## TAB 4 — Higgsfield (B-roll — 32 clips)

Open: **https://cloud.higgsfield.ai** or **https://higgsfield.ai**

Use **Text to Video** or **Cinema Studio**. Model: **Veo 3.1** or **Kling 3.0** if available.  
**Aspect ratio:** 16:9 · **Duration:** 5–6 seconds each · **4 clips per chapter**

Generate and save as `clip_00.mp4`, `clip_01.mp4`, `clip_02.mp4`, `clip_03.mp4` in each chapter folder.

### chapter-1 (`broll/chapter-1/`)
1. `clip_00.mp4` — Aerial drone shot of modern Riyadh skyline at golden hour, Kingdom Centre visible, cinematic documentary, 4K, no text
2. `clip_01.mp4` — Modern government administrative building exterior, formal architecture, establishing shot, cinematic documentary, 4K, no text
3. `clip_02.mp4` — Luxury modern apartment exterior Middle Eastern city, palm trees, slow pan, cinematic documentary, 4K, no text
4. `clip_03.mp4` — Professional business cityscape Saudi Arabia Vision 2030, modern towers, cinematic documentary, 4K, no text

### chapter-2 (`broll/chapter-2/`)
1. `clip_00.mp4` — Professional Saudi Arabian business district, modern development, wide shot, cinematic documentary, 4K, no text
2. `clip_01.mp4` — Corporate boardroom Middle East floor-to-ceiling windows, cinematic documentary, 4K, no text
3. `clip_02.mp4` — Diverse professional team meeting modern office Saudi Arabia, cinematic documentary, 4K, no text
4. `clip_03.mp4` — Modern residential towers affluent district Riyadh, cinematic documentary, 4K, no text

### chapter-3 (`broll/chapter-3/`)
1. `clip_00.mp4` — Luxury villa exterior gated community Saudi Arabia, palm trees, cinematic documentary, 4K, no text
2. `clip_01.mp4` — Passport and residency documents on desk professional office, shallow depth of field, no readable text, cinematic
3. `clip_02.mp4` — King Abdullah Financial District Riyadh glass towers, establishing shot, cinematic documentary, 4K, no text
4. `clip_03.mp4` — Family home modern Saudi residential neighborhood, warm golden hour, cinematic documentary, 4K, no text

### chapter-4 (`broll/chapter-4/`)
1. `clip_00.mp4` — Futuristic sustainable city aerial Red Sea coastline NEOM style artist impression, soft daylight, cinematic, 4K, no text
2. `clip_01.mp4` — Aerial view Red Sea coastline Saudi Arabia turquoise water luxury development, cinematic, 4K, no text
3. `clip_02.mp4` — Construction site modern master planned community Saudi Arabia aerial, cinematic documentary, 4K, no text
4. `clip_03.mp4` — Coastal development luxury apartments Red Sea, cinematic documentary, 4K, no text

### chapter-5 (`broll/chapter-5/`)
1. `clip_00.mp4` — Modern corporate office exterior glass building Saudi Arabia, cinematic documentary, 4K, no text
2. `clip_01.mp4` — Professional signing business documents handshake modern office, cinematic documentary, 4K, no text
3. `clip_02.mp4` — Commercial plot aerial masterplan development zone, cinematic documentary, 4K, no text
4. `clip_03.mp4` — Executive boardroom presentation blurred screen, cinematic documentary, 4K, no text

### chapter-6 (`broll/chapter-6/`)
1. `clip_00.mp4` — Hands reviewing property contract on desk professional office, shallow depth of field, no readable text, cinematic
2. `clip_01.mp4` — Modern government administrative building exterior REGA style, formal architecture, cinematic documentary, 4K, no text
3. `clip_02.mp4` — Property inspection professional walking through modern apartment, cinematic documentary, 4K, no text
4. `clip_03.mp4` — Handing over house keys real estate closing, cinematic documentary, 4K, no text

### chapter-7 (`broll/chapter-7/`)
1. `clip_00.mp4` — Modern bank building financial district Saudi Arabia, cinematic documentary, 4K, no text
2. `clip_01.mp4` — Financial district skyline business towers, cinematic documentary, 4K, no text
3. `clip_02.mp4` — Calculator and mortgage documents on desk professional setting, no readable text, cinematic
4. `clip_03.mp4` — Growth chart visualization green gold on dark background motion graphics style, cinematic, 4K, no text

### chapter-8 (`broll/chapter-8/`)
1. `clip_00.mp4` — Professional reviewing documents concerned expression office, cinematic documentary, 4K, no text
2. `clip_01.mp4` — Law books and legal documents on desk professional office, cinematic, 4K, no text
3. `clip_02.mp4` — Checklist clipboard due diligence property review, cinematic documentary, 4K, no text
4. `clip_03.mp4` — Business consultation two professionals discussing documents, cinematic documentary, 4K, no text

Append to every prompt: `cinematic documentary style, natural lighting, 4K, no text overlays, no watermarks`

---

## TAB 5 — Assembly (FFmpeg or Cursor Agent)

### Option A — Upload to Cursor Cloud Agent

1. Zip folder: `Desktop/Saudi-Gateway-Video-01.zip`
2. Open **https://cursor.com/agents** → New Agent → repo `starlit-cobbler-2aec43`
3. Upload zip and send:

```
Unzip to channel/automation/projects/01-foreigners-buy-property-ksa/
Run: python channel/automation/assemble_video.py --project channel/automation/projects/01-foreigners-buy-property-ksa
Deliver final.mp4
```

### Option B — FFmpeg on my computer (if installed)

Tell me to install FFmpeg, then run assembly script from cloned repo.

---

## PHASE 6 — Report completion

When done, tell me:

```
VIDEO 01 MANUAL PRODUCTION COMPLETE
- Voiceovers: 10/10
- Avatar clips: 5/5
- B-roll clips: 32/32
- Final video: [path or uploaded]
```

List any missing clips.

---

## Rules

- Use exact filenames (assembly breaks if names are wrong)
- 16:9 1080p for everything
- Charlotte: modest professional — no low neckline, no sleeveless
- Stop only for logins: ElevenLabs, HeyGen, Higgsfield, Cursor
- Work tab by tab in order: GitHub → ElevenLabs → HeyGen → Higgsfield → Assembly

---

*End of Claude prompt*
