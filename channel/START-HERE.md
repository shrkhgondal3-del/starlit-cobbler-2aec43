# Saudi Gateway — START HERE

## Your video is already done

**Watch / download:** `channel/deliverables/VIDEO-LINK.md`

**Stuck on API keys?** Read `channel/FIX-API-KEYS.md` — you can skip them entirely.

---

## Make another video (one command)

```bash
cd channel/automation
python3 produce_video.py
```

No HeyGen/Higgsfield keys required.

---

## Optional: premium APIs (only if you want automation)

Do these steps in order. **Ignore MCP / Connect buttons** — they don't work reliably on Cloud Agents.

---

## STEP 1 — Buy accounts (if you haven't)

1. HeyGen Creator → https://www.heygen.com/pricing → Sign up
2. Higgsfield Plus → https://higgsfield.ai/pricing → Sign up
3. ElevenLabs Creator → https://elevenlabs.io/pricing → Sign up

---

## STEP 2 — Copy your API keys

### HeyGen
1. Open https://app.heygen.com/settings?nav=API
2. Click **Create API Key**
3. Copy the key
4. Top up API wallet (~$5 minimum) if asked

### Higgsfield
1. Open https://platform.higgsfield.ai
2. Go to **API** section
3. Copy **Key ID** and **Secret**

### ElevenLabs (if not done)
1. Open https://elevenlabs.io/app/settings/api-keys
2. Create key → copy it

---

## STEP 3 — Paste keys into Cursor

1. Open https://cursor.com/dashboard/cloud-agents
2. Click **Secrets** tab
3. Click **Add secret** for each row:

| Name | Paste this |
|------|------------|
| `ELEVENLABS_API_KEY` | your ElevenLabs key |
| `ELEVENLABS_VOICE_ID` | `Xb7hH8MSUJpSbSDYk0k2` |
| `HEYGEN_API_KEY` | your HeyGen key |
| `HIGGSFIELD_API_KEY` | your Higgsfield Key ID |
| `HIGGSFIELD_API_SECRET` | your Higgsfield Secret |

4. Click **Save** after each one

---

## STEP 4 — Create Charlotte avatar in HeyGen (one time)

1. Open https://app.heygen.com
2. Click **Avatars** → **Photo Avatar** → **Create**
3. Upload 8 photos of a professional British woman (modest dress)
4. Name: `Charlotte Hayes - Saudi Gateway`
5. Copy the **Avatar ID**
6. Go back to Cursor Secrets → Add:
   - Name: `HEYGEN_AVATAR_ID`
   - Value: the Avatar ID you copied

---

## STEP 5 — Start fresh agent

1. Open https://cursor.com/agents
2. Click **New Agent**
3. Pick repo: `starlit-cobbler-2aec43`
4. Send this message:

```
Keys added. Produce Video 01 end-to-end.
```

---

## Done

The agent will make the video. You only upload to YouTube when it's ready.

**Do NOT use:** MCP Connect, Plugins Connect, or Team MCP OAuth — skip all of that.
