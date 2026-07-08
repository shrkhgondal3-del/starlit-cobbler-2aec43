# Saudi Gateway — Visual Setup Guide (Original Plan)

**Goal:** Connect HeyGen + Higgsfield via MCP. ElevenLabs is already working.

**Time:** ~15 minutes  
**You need:** Cursor Desktop app on your computer

---

## STEP 1 — Open Cursor on your computer

1. Download/install if needed: https://cursor.com
2. Open the **Cursor** app (not just cursor.com in browser)
3. Make sure you are logged in as **shrkhgondal3@gmail.com**

**Keyboard shortcut to open settings:**

| Mac | Windows / Linux |
|-----|-----------------|
| `Cmd + Shift + J` | `Ctrl + Shift + J` |

![Step 1](/opt/cursor/artifacts/assets/step1-open-cursor-settings.png)

---

## STEP 2 — Go to Tools & MCP

1. After pressing the shortcut, a **Settings** panel opens
2. Click **Tools & MCP** in the **left sidebar**
3. You should see a list including **Heygen** and **Higgsfield**

![Step 2](/opt/cursor/artifacts/assets/step2-tools-and-mcp.png)

**If Heygen/Higgsfield are missing:**
- Click **Browse Marketplace** or go to https://cursor.com/marketplace
- Install **HeyGen** and **Higgsfield** plugins
- Come back to Tools & MCP

---

## STEP 3 — Connect HeyGen

1. Find **Heygen** in the list
2. Click the **Connect** button
3. A browser tab opens → **sign in** to HeyGen
4. Wait until status shows **Connected** (green dot)

![Step 3](/opt/cursor/artifacts/assets/step3-heygen-connect.png)

**HeyGen account needed:** Creator plan (~$29/mo)  
https://www.heygen.com/pricing

---

## STEP 4 — Connect Higgsfield

1. Find **Higgsfield** in the same list
2. Click **Connect**
3. Browser opens → **sign in** to Higgsfield
4. Wait until status shows **Connected** (green dot)

![Step 4](/opt/cursor/artifacts/assets/step4-higgsfield-connect.png)

**Higgsfield account needed:** Plus plan (~$49/mo)  
https://higgsfield.ai/pricing

---

## STEP 5 — Start a new Cloud Agent

1. Open agent chat in Cursor
2. At the top of the message box, change dropdown from **Local** to **Cloud**
3. Select repo: `shrkhgondal3-del/starlit-cobbler-2aec43`
4. Type and send:

```
HeyGen and Higgsfield connected. Please verify MCP and produce Video 01.
```

![Step 5](/opt/cursor/artifacts/assets/step5-cloud-agent.png)

**Important:** Start a **new** agent after connecting — old agents may not see the new auth.

---

## STEP 6 — Create Charlotte avatar (one time)

1. Open https://app.heygen.com in Chrome
2. Click **Avatars** (left menu)
3. Click **Photo Avatar** → **Create**
4. Upload 8 photos OR use HeyGen AI to generate them
   - Professional British woman, modest dress, studio look
5. Name: `Charlotte Hayes - Saudi Gateway`
6. Click **Create** / **Finish**
7. Tell your agent: `Charlotte avatar is trained`

![Step 6](/opt/cursor/artifacts/assets/step6-charlotte-avatar.png)

---

## Checklist

- [ ] Cursor Desktop installed
- [ ] Tools & MCP opened (`Ctrl+Shift+J`)
- [ ] Heygen → Connected (green)
- [ ] Higgsfield → Connected (green)
- [ ] New Cloud Agent started
- [ ] Charlotte avatar created in HeyGen

---

## If you get stuck

Reply with the **step number** and what you see on screen.

Example: `Step 3 — no Connect button` or `Step 2 — can't find Tools & MCP`

---

## What we are NOT doing

- ❌ API keys
- ❌ Cursor Secrets / Environments
- ❌ MCP on cursor.com website only
- ❌ CapCut or manual editing
