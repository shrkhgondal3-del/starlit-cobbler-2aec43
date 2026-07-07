# Saudi Gateway — Proper Setup (No MCP / No OAuth)

**If MCP Connect keeps failing on Cloud Agents, use this instead.**  
Same quality (HeyGen avatar + Higgsfield B-roll). You only paste API keys once.

---

## What you do (10 minutes, one time)

### Step 1 — Get your API keys

| Service | Where to get the key | Link |
|---------|---------------------|------|
| **ElevenLabs** | Settings → API Keys | https://elevenlabs.io/app/settings/api-keys |
| **HeyGen** | Settings → API | https://app.heygen.com/settings/api |
| **Higgsfield** | Platform dashboard → API | https://platform.higgsfield.ai |

**HeyGen note:** API uses a separate wallet (~$5 minimum top-up). Your Creator plan credits are for the website; API is pay-as-you-go.

**Higgsfield note:** You get a **Key ID** and **Secret** (format `KEY_ID:KEY_SECRET`).

---

### Step 2 — Paste keys into Cloud Agent Secrets

1. Open: **https://cursor.com/dashboard/cloud-agents**
2. Click the **Secrets** tab
3. Add these secrets (click **Add secret** for each):

| Secret name | Value |
|-------------|-------|
| `ELEVENLABS_API_KEY` | Your ElevenLabs key (starts with `sk_`) |
| `ELEVENLABS_VOICE_ID` | `Xb7hH8MSUJpSbSDYk0k2` (Alice, British) |
| `HEYGEN_API_KEY` | Your HeyGen API key |
| `HIGGSFIELD_API_KEY` | Your Higgsfield Key ID |
| `HIGGSFIELD_API_SECRET` | Your Higgsfield Secret |

4. **Save** each secret

---

### Step 3 — Train Charlotte Hayes in HeyGen (one time, ~15 min)

1. Log in to https://app.heygen.com
2. Go to **Avatars → Photo Avatar → Create**
3. Upload 8 reference photos (use prompts in `content/ai-prompts/AVATAR-REFERENCE-PROMPTS.md`)
4. Name: **Charlotte Hayes - Saudi Gateway**
5. Copy the **Avatar ID** from HeyGen
6. Add to Cloud Agent Secrets:

| Secret name | Value |
|-------------|-------|
| `HEYGEN_AVATAR_ID` | Your Charlotte avatar ID |

---

### Step 4 — Tell the agent

Start a **new** Cloud Agent and send:

```
API keys added to Cloud Agent secrets. Charlotte avatar trained.
Please run check_setup.py, then produce Video 01 end-to-end.
```

---

## How the agent verifies

```bash
cd channel/automation
python3 check_setup.py
```

You want all green:

```
✓ ElevenLabs
✓ HeyGen
✓ Higgsfield
```

---

## Why this works when MCP doesn't

| Method | Works on Cloud Agents? | Your effort |
|--------|------------------------|-------------|
| MCP OAuth (Connect button) | Often fails on mobile/cloud agents | Click Connect, sign in — frustrating |
| **API keys in Secrets** | **Always works** | Paste 5 values once |

The agent calls HeyGen and Higgsfield APIs directly — no OAuth, no MCP dropdown.

---

## Costs (same as before)

| Service | Plan | ~Monthly |
|---------|------|----------|
| ElevenLabs Creator | Voice | $22 |
| HeyGen Creator + API wallet | Avatar | $29 + ~$5–20 API |
| Higgsfield Plus | B-roll | $49 |
| **Total** | | **~$100–110** |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `check_setup.py` says HeyGen missing | Add `HEYGEN_API_KEY` to Secrets, restart agent |
| HeyGen 401 | Regenerate API key at app.heygen.com/settings/api |
| HeyGen insufficient credits | Top up API wallet at heygen.com/api-pricing |
| Higgsfield 401 | Check both `HIGGSFIELD_API_KEY` and `HIGGSFIELD_API_SECRET` |
| Secrets not visible to agent | Start a **new** Cloud Agent after adding secrets |

---

*This is the recommended path for Cloud Agent users who cannot get MCP OAuth working.*
