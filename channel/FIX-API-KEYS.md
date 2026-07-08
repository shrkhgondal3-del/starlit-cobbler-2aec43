# Fix API Keys — Or Skip Them Entirely

**If you've been stuck on API keys since yesterday, read this first.**

You have **three paths**. Path A works **right now** with no keys.

---

## Path A — No API keys (recommended until keys work)

The agent already produced Video 01 without HeyGen/Higgsfield.

**One command (agent or local):**
```bash
cd channel/automation
python3 produce_video.py
```

This uses:
- ElevenLabs voice (if `ELEVENLABS_API_KEY` is set — yours works ✓)
- Automated avatar cards (HeyGen not required)
- Stock + branded B-roll (Higgsfield not required)

**Your video is ready:** see `channel/deliverables/VIDEO-LINK.md`

---

## Path B — Drop files in GitHub (bypasses ALL API secrets)

If API keys keep failing, **don't fight them**. Export from HeyGen/Higgsfield/ElevenLabs in your browser, push files to GitHub, and let the agent import.

### Step 1 — Create folders locally

```
channel/automation/incoming/
├── hook.mp4
├── bridge-ch3.mp4
├── bridge-ch4.mp4
├── myth-emphasis.mp4
├── close.mp4
├── voiceovers/          ← 8 chapter MP3s (any names)
└── broll.zip            ← 15+ Higgsfield clips
```

### Step 2 — Push to GitHub

```bash
git add channel/automation/incoming/
git commit -m "Add Video 01 assets"
git push
```

### Step 3 — Tell the agent

```
Run: cd channel/automation && python3 produce_video.py
```

The script auto-imports from `incoming/` then assembles.

**No Cursor Secrets. No MCP. No OAuth.**

---

## Path C — Fix API keys (when you want full automation)

### Where to paste secrets (desktop browser)

1. Open **https://cursor.com/dashboard** (use desktop Chrome/Safari — not mobile app)
2. Click **Cloud Agents** in the left sidebar
3. Click **Secrets** tab at the top
4. Click **Add secret** for each row below
5. **Save** each one
6. Start a **New Agent** (secrets do NOT reload on running agents)

| Secret name | Where to get it |
|-------------|-----------------|
| `ELEVENLABS_API_KEY` | https://elevenlabs.io/app/settings/api-keys |
| `ELEVENLABS_VOICE_ID` | `Xb7hH8MSUJpSbSDYk0k2` |
| `HEYGEN_API_KEY` | https://app.heygen.com/settings?nav=API |
| `HEYGEN_AVATAR_ID` | HeyGen → Avatars → Charlotte → copy ID |
| `HIGGSFIELD_API_KEY` | https://platform.higgsfield.ai |
| `HIGGSFIELD_API_SECRET` | same page (Secret, not Key ID) |

### Can't find Secrets on mobile?

The mobile app often hides Cloud Agent settings. **Use a desktop browser:**
- Go to https://cursor.com/dashboard/cloud-agents
- Or: https://cursor.com/agents → pick your agent → **Environment** / **Secrets**

---

## HeyGen 401 Unauthorized — most common fixes

Your key is set but returns **401**. This means the key itself is wrong, not Cursor.

| Mistake | Fix |
|---------|-----|
| Wrong URL | Use **https://app.heygen.com/settings?nav=API** (NOT `/settings/api`) |
| Wrong key type | Create **API** key, not "Agent" key |
| Key pasted in chat | **Rotate the key** — it's compromised |
| Old/expired key | Delete old key → Create new → Update Cursor Secret |
| No API wallet | Top up at https://www.heygen.com/api-pricing (~$5 min) |
| Secret not reloaded | Add secret → **start NEW Cloud Agent** |

### Test your HeyGen key (run in agent terminal)

```bash
curl -s "https://api.heygen.com/v1/user/me" -H "X-Api-Key: YOUR_KEY_HERE"
```

- `"code": 100` → key works
- `401 Unauthorized` → regenerate key at HeyGen dashboard

---

## Higgsfield — most common fixes

| Mistake | Fix |
|---------|-----|
| Only one value pasted | You need **two** secrets: `HIGGSFIELD_API_KEY` AND `HIGGSFIELD_API_SECRET` |
| Swapped key/secret | Key ID goes in `_API_KEY`, Secret goes in `_API_SECRET` |
| Wrong site | Use **https://platform.higgsfield.ai** (not higgsfield.ai main site) |

---

## MCP / Connect button — skip it

| Method | Cloud Agent? |
|--------|--------------|
| MCP OAuth Connect | ❌ Often fails (especially from mobile) |
| API keys in Secrets | ✅ Works when keys are valid |
| **incoming/ folder + Git push** | ✅ **Always works** |
| **produce_video.py (no keys)** | ✅ **Always works** |

---

## Verify setup

```bash
cd channel/automation
python3 setup_api_keys.py
```

Shows exactly which keys work and which don't.

Then produce:
```bash
python3 produce_video.py
```

---

## Still stuck? Copy-paste this to a new agent

```
Ignore MCP. Run:
cd channel/automation
python3 produce_video.py
Report the output path and VIDEO-LINK.md URLs.
If incoming/ has files, import them first.
```

You do **not** need working HeyGen/Higgsfield keys to publish Video 01.
