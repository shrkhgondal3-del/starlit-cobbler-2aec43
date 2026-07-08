# Saudi Gateway — AI Script Generation Prompts

Use these with Claude or ChatGPT to generate new video scripts in Saudi Gateway format. Always fact-check against official sources before voiceover.

---

## Master Script Prompt

```
You are the lead scriptwriter for "Saudi Gateway", an English-language YouTube channel about KSA property and business setup for foreigners.

Write a complete YouTube script for the following video:

TOPIC: [TOPIC]
TARGET LENGTH: [14-16 minutes / 8-10 minutes for Shorts compilation]
PILLAR: [Property / Business / Market Intelligence]
TARGET KEYWORD: [primary SEO keyword]
AUDIENCE: Foreign investors, expats, entrepreneurs (UK/EU/US/GCC) with no prior Saudi legal knowledge

REQUIREMENTS:
1. Format for AI voiceover — no stage directions like "on camera". Use [VISUAL: description] tags for B-roll.
2. Open with a 30-second hook that challenges a common misconception.
3. Include 6-8 chapters with clear timestamps.
4. Cite official sources (MISA/invest.sa, REGA/rega.gov.sa, ZATCA, Premium Residency portal) — note [VERIFY URL before publish].
5. Include "it depends" nuance — never overstate foreign ownership rights.
6. Add a disclaimer line in the intro and close.
7. End with CTA: free checklist, subscribe, comment prompt.
8. Include a "Common Mistakes" section (5 items).
9. Write at 140-160 words/minute speaking pace.
10. Avoid hype words: "insane", "crazy opportunity", "guaranteed returns".
11. Add [SHORTS CUT: 30-sec hook line] markers for 3 extractable Shorts.
12. Separate Arabic terms with English explanation on first use (e.g., "Commercial Registration — known as CR").

OUTPUT FORMAT:
# Script [NN] — [Title]
**Runtime target:** X minutes (~X words)
**Pillar:** X | **Playlist:** X
**Thumbnail title:** `X` | Badge: `X`

## HOOK (0:00–0:30)
[narration text]
[VISUAL: ...]

## CHAPTER 1: [Title] (0:30–X:XX)
...

## Production Notes
- Sources to display on screen
- Shorts cuts list
- Tags
```

---

## Shorts-Only Script Prompt

```
Write a 45-second YouTube Short script for Saudi Gateway.

TOPIC: [one specific insight from a long-form video]
HOOK (first 2 seconds): Bold contrarian statement or question
STRUCTURE: Hook → 1 key insight → CTA ("Full guide on Saudi Gateway")
FORMAT: AI voiceover, no presenter. Mark [VISUAL: ...] every 3-4 seconds.
Include on-screen text suggestions in [TEXT ON SCREEN: "..."]
End with: "Follow for Saudi property & business guides."
Max 120 words.
```

---

## Regulation Update Prompt

```
Saudi Gateway needs a 10-minute update video on a regulatory change.

CHANGE: [describe the new MISA/REGA/RHQ/Premium Residency update]
SOURCE: [link to official announcement]
PREVIOUS RULE: [what changed from]
AUDIENCE IMPACT: [who this affects among foreign investors]

Write an AI voiceover script that:
1. Opens with "If you're [audience], this affects you."
2. Explains old vs new rule in plain English
3. Gives 3 actionable steps for affected foreigners
4. Notes what has NOT changed (avoid confusion)
5. Includes disclaimer and source citation
6. Under 1,800 words
```

---

## Content Calendar Batch Prompt

```
Generate a 4-week YouTube content calendar for Saudi Gateway (2 long-form/week + 3 Shorts/week).

PILLAR MIX: 60% property, 40% business
AUDIENCE: Foreign buyers and founders
CONSTRAINT: Every title must target a specific Google/YouTube search query foreigners use.

Output as a table: Day | Type | Title | Pillar | Target Keyword

Avoid duplicate topics from this list: [paste existing calendar titles]
Prioritize high-intent keywords with low English-language competition.
```

---

## Script-to-Voiceover Conversion Prompt

```
Convert this YouTube script to clean AI voiceover text for ElevenLabs.

RULES:
- Remove all markdown formatting, headers, timestamps, production notes
- Remove [VISUAL: ...] tags but keep [PAUSE] where a 1-second beat helps
- Expand abbreviations on first use (CR → Commercial Registration, then CR is fine)
- Write numbers under 10 as words ("four pathways" not "4 pathways")
- Remove "I'm [Name] from Saudi Gateway" — replace with "Welcome to Saudi Gateway"
- Keep disclaimer language verbatim
- Output plain text only, paragraph per chapter, separated by "---"
```

---

## Quality Review Prompt (Run Before Production)

```
Review this Saudi Gateway script for factual and compliance risks.

Check:
1. Any claim about foreign property ownership that overstates rights?
2. Any specific fee, threshold, or timeline stated without "verify current" caveat?
3. Missing disclaimer?
4. Sectors where foreign ownership is restricted but not mentioned?
5. Outdated pre-2024 rules presented as current?
6. Anything that could be construed as legal or investment advice?

Script:
[paste script]

Output: PASS or FAIL with specific line-by-line fixes needed.
```
