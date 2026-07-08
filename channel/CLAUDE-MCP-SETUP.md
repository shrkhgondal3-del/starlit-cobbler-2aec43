# Copy everything below this line and paste into Claude (Computer Use / Chrome)

---

You are helping me complete **MCP sign-in** for my **Saudi Gateway** YouTube channel in **Cursor**. Use **Google Chrome** and/or the **Cursor desktop app** on my computer. Complete every step you can. Only stop me for login password, 2FA, or payment.

## Goal

Connect these two MCP servers so my Cursor Cloud Agent can make videos:

| Server | MCP URL |
|--------|---------|
| **Heygen** | `https://mcp.heygen.com/mcp/v1/` |
| **Higgsfield** | `https://mcp.higgsfield.ai/mcp` |

**Do NOT use API keys.** Use MCP OAuth sign-in only (original plan).

ElevenLabs is already working. I only need HeyGen + Higgsfield MCP connected + Charlotte avatar created.

---

## IMPORTANT — Where Connect actually is

The **Team MCP Servers** table on Cursor dashboard does **NOT** have a Connect button. That page only adds servers (already done).

Sign-in happens in one of these places (try in order):

1. **Cursor Marketplace** (browser)
2. **Cursor Desktop → Tools & MCP** (app)
3. **Cursor Plugins page** (click into each plugin card)

---

## STEP 1 — HeyGen MCP sign-in (Marketplace)

1. Open Chrome → **https://cursor.com/marketplace/heygen**
2. If not logged into Cursor, wait for me to log in as **shrkhgondal3@gmail.com**
3. Click **Add to Cursor** or **Install**
4. When browser opens for HeyGen OAuth → complete sign-in with my HeyGen account (Creator plan)
5. Confirm success: HeyGen shows **Connected** or **Installed + authenticated**

**Alternate if Step 1 fails:**
- Open **Cursor desktop app**
- Press **Ctrl+Shift+P** (Windows) or **Cmd+Shift+P** (Mac)
- Type **Tools & MCP** → open it
- Find **Heygen** → click **Connect** (or click text **Needs authentication** under the name)
- Complete HeyGen sign-in in browser

---

## STEP 2 — Higgsfield MCP sign-in

1. Open Chrome → **https://higgsfield.ai/mcp**
2. Follow page instructions to add Higgsfield to **Cursor**
3. Or open **https://cursor.com** → **Plugins** → click **Higgsfield** card (not just "Installed")
4. Click **Connect** / **Authenticate** / **Sign in**
5. Complete Higgsfield OAuth in browser (Plus plan account)
6. Confirm **Connected**

**Alternate:**
- Cursor Desktop → **Tools & MCP** → **Higgsfield** → **Connect** → sign in

---

## STEP 3 — Verify Team MCP servers exist (optional check)

1. Open **https://cursor.com/dashboard/integrations**
2. Scroll to **Team MCP Servers**
3. Confirm both are listed:

```
Higgsfield   https://mcp.higgsfield.ai/mcp        HTTP
Heygen       https://mcp.heygen.com/mcp/v1/       HTTP
```

If missing, click **Add** and enter the URLs above. No OAuth on this page — that's normal.

**Ignore console errors** like `401 get-directory-groups` — they are Cursor dashboard glitches, not HeyGen/Higgsfield errors.

---

## STEP 4 — Create Charlotte Hayes avatar in HeyGen (one time)

1. Open Chrome → **https://app.heygen.com**
2. Wait for me to log in if needed
3. Left menu → **Avatars** → **Photo Avatar** → **Create**
4. Upload 8 photos OR use HeyGen AI to generate:
   - Professional British woman, modest dress, studio background
5. Name avatar: **Charlotte Hayes - Saudi Gateway**
6. Finish creation → copy **Avatar ID** if visible
7. Save Avatar ID in a note for me

**Do NOT use** broken URL `app.heygen.com/settings/api` — use profile → Settings → API only if needed later.

---

## STEP 5 — Start new Cloud Agent to test

1. Open **https://cursor.com/agents**
2. Click **New Agent**
3. Repository: **shrkhgondal3-del/starlit-cobbler-2aec43**
4. Send this message:

```
HeyGen and Higgsfield MCP connected. Charlotte avatar trained.
Please verify MCP tools and produce Video 01 end-to-end.
```

---

## STEP 6 — Report back to me

When done, tell me:

```
SETUP COMPLETE
- HeyGen MCP: Connected (yes/no)
- Higgsfield MCP: Connected (yes/no)  
- Charlotte avatar: Created (yes/no)
- Avatar ID: [paste if found]
- New Cloud Agent started: (yes/no)
```

If anything failed, say which step and what you saw on screen.

---

## Rules for you (Claude)

- Use Chrome + Cursor Desktop as needed
- Do not ask me to find "Secrets" or "Environments" — we use MCP only
- Do not use API keys unless MCP sign-in completely fails after all alternates
- Do not close browser tabs until sign-in shows Connected
- Only stop for: Cursor login, HeyGen login, Higgsfield login, 2FA, payment

---

## My accounts

| Service | Email / account |
|---------|-----------------|
| Cursor | shrkhgondal3@gmail.com |
| GitHub repo | shrkhgondal3-del/starlit-cobbler-2aec43 |
| HeyGen | Creator plan |
| Higgsfield | Plus plan |

---

## Troubleshooting

| Problem | Try |
|---------|-----|
| No Connect button on Team MCP table | Expected — use Marketplace or Desktop Tools & MCP |
| Connect button does nothing | Click **Needs authentication** text under server name instead |
| 401 errors in browser console on dashboard | Ignore — log out/in to cursor.com and continue |
| Only have phone | Must use a computer for MCP sign-in |

---

*End of prompt — paste everything above into Claude with Computer Use enabled*
