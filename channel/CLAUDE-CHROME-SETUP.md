# Copy everything below this line and paste into Claude (with Computer Use / Chrome)

---

You are helping me complete a one-time setup for my **Saudi Gateway** YouTube channel. Use **Google Chrome** on my computer. Take control of the browser and complete every step below. Do not ask me to click things unless login/password/2FA is required.

## Goal

Add these API keys to **Cursor Cloud Agent Secrets** so my Cursor Cloud Agent can produce videos:

- `ELEVENLABS_API_KEY`
- `ELEVENLABS_VOICE_ID` = `Xb7hH8MSUJpSbSDYk0k2`
- `HEYGEN_API_KEY`
- `HEYGEN_AVATAR_ID` (after creating Charlotte avatar)
- `HIGGSFIELD_API_KEY`
- `HIGGSFIELD_API_SECRET`

**Ignore MCP / Connect / OAuth in Cursor Plugins** — that path failed. Use API keys only.

---

## STEP 1 — ElevenLabs API key

1. Open Chrome → https://elevenlabs.io/app/settings/api-keys
2. If not logged in, wait for me to log in
3. Click **Create API Key** → name it `Saudi Gateway`
4. Copy the key (shown once)
5. Keep it in a temporary note — you'll paste it in Step 4

---

## STEP 2 — HeyGen API key

1. Open new tab → https://app.heygen.com/settings/api
2. If not logged in, wait for me to log in (Creator plan required)
3. Click **Create API Key** or **Generate**
4. If prompted to top up API wallet, tell me — minimum ~$5
5. Copy the API key → save for Step 4

---

## STEP 3 — Higgsfield API keys

1. Open new tab → https://platform.higgsfield.ai
2. If that fails, try https://cloud.higgsfield.ai or https://higgsfield.ai → Account → API
3. If not logged in, wait for me to log in (Plus plan required)
4. Find **API** or **Developers** section
5. Copy **Key ID** and **Secret** → save for Step 4

---

## STEP 4 — Paste all keys into Cursor Cloud Agent Secrets

1. Open new tab → https://cursor.com/dashboard/cloud-agents
2. If not logged in, wait for me to log in
3. Click **Secrets** tab
4. Add each secret (click **Add secret** for each):

| Secret name | Value |
|-------------|-------|
| `ELEVENLABS_API_KEY` | (key from Step 1) |
| `ELEVENLABS_VOICE_ID` | `Xb7hH8MSUJpSbSDYk0k2` |
| `HEYGEN_API_KEY` | (key from Step 2) |
| `HIGGSFIELD_API_KEY` | (Key ID from Step 3) |
| `HIGGSFIELD_API_SECRET` | (Secret from Step 3) |

5. Save each one
6. Screenshot the Secrets page (names visible, values hidden) to confirm

---

## STEP 5 — Create Charlotte Hayes avatar in HeyGen

1. Open https://app.heygen.com
2. Go to **Avatars** → **Photo Avatar** → **Create**
3. If I don't have photos ready:
   - Use HeyGen's AI photo generator OR
   - Ask me to upload 8 photos of a professional British woman, modest dress, studio look
4. Name the avatar: `Charlotte Hayes - Saudi Gateway`
5. Finish training / create avatar
6. Copy the **Avatar ID** from avatar settings
7. Go back to https://cursor.com/dashboard/cloud-agents → **Secrets**
8. Add secret:
   - Name: `HEYGEN_AVATAR_ID`
   - Value: (the Avatar ID)

---

## STEP 6 — Verify and report back

Confirm all 6 secrets exist in Cursor:

- [ ] ELEVENLABS_API_KEY
- [ ] ELEVENLABS_VOICE_ID
- [ ] HEYGEN_API_KEY
- [ ] HEYGEN_AVATAR_ID
- [ ] HIGGSFIELD_API_KEY
- [ ] HIGGSFIELD_API_SECRET

Then tell me:

```
Setup complete. All 6 secrets added. Start a new Cursor Cloud Agent and say: Keys added. Produce Video 01.
```

---

## Rules for you (Claude)

- Use Chrome only
- Complete as much as possible without asking me
- Only stop for: login, password, 2FA, payment/card entry
- Do NOT use Cursor MCP Connect / Plugins OAuth — API keys only
- Do NOT close tabs until secrets are saved
- If a URL fails, try the alternate Higgsfield URLs in Step 3

---

## My accounts (fill in if Claude asks)

- Cursor email: shrkhgondal3@gmail.com
- GitHub repo: shrkhgondal3-del/starlit-cobbler-2aec43
- HeyGen plan: Creator
- Higgsfield plan: Plus
- ElevenLabs plan: Creator

---

*End of prompt — paste everything above into Claude*
