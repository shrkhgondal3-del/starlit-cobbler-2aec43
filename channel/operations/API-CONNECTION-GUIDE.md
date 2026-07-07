# Saudi Gateway — Connect All APIs to Your Agent

One-time setup so the agent handles ElevenLabs, HeyGen, and Higgsfield **without you using their websites per video**.

> **Cloud Agent users:** If MCP Connect keeps failing, use **[SIMPLE-API-SETUP.md](SIMPLE-API-SETUP.md)** instead — paste API keys into Cloud Agent Secrets. No OAuth.

---

## Quick shopping list

| # | Service | Plan to buy | Monthly cost | Connect method |
|---|---------|-------------|--------------|----------------|
| 1 | **ElevenLabs** | [Creator](https://elevenlabs.io/pricing) | $22/mo | API key → Cursor secrets |
| 2 | **HeyGen** | [Creator](https://www.heygen.com/pricing) | $29/mo | MCP (no API key) |
| 3 | **Higgsfield** | [Plus](https://higgsfield.ai/pricing) | $49/mo | MCP (no API key) |

**Total: ~$100/month**

---

## 1. ElevenLabs — Voice (API key required)

### Buy this plan
| | Link |
|---|------|
| **Pricing page** | https://elevenlabs.io/pricing |
| **Plan to choose** | **Creator — $22/month** |
| **Direct signup** | https://elevenlabs.io/app/sign-up |

**Why Creator (not Starter $6):** Creator includes **Professional Voice Cloning** for Charlotte Hayes + enough credits (~121k/mo) for 8–10 long videos.

### Get API key
| Step | Link / action |
|------|----------------|
| 1 | Log in → https://elevenlabs.io/app/settings/api-keys |
| 2 | Click **Create API Key** |
| 3 | Name it: `Saudi Gateway - Cursor Agent` |
| 4 | Copy the key (shown once) |

### Connect to agent
Add to **Cursor → your Cloud Agent environment secrets**:

```
ELEVENLABS_API_KEY=sk_xxxxxxxxxxxxxxxx
```

Optional (after you clone Charlotte's voice):
```
ELEVENLABS_VOICE_ID=your_cloned_voice_id
```

**Agent uses:** `channel/automation/elevenlabs_generate.py`

---

## 2. HeyGen — Charlotte Hayes avatar (MCP recommended)

### Buy this plan
| | Link |
|---|------|
| **Pricing page** | https://www.heygen.com/pricing |
| **Plan to choose** | **Creator — $29/month** (or $24/mo annual) |
| **Direct signup** | https://app.heygen.com/login |

**Why Creator:** Unlimited Photo Avatars, voice cloning, 1080p, no watermark, 600 credits/mo.

### API (optional — MCP is easier)
| | Link |
|---|------|
| API pricing (pay-as-you-go wallet) | https://www.heygen.com/api-pricing |
| API key (if not using MCP) | https://app.heygen.com/settings/api |
| Developer docs | https://developers.heygen.com/docs/api-key |

**Note:** HeyGen API wallet is **separate** from web plan credits (min ~$5 top-up). **Prefer MCP below** — uses your Creator plan credits, no API key.

### Connect to agent — MCP (recommended)
| Step | Action |
|------|--------|
| 1 | Open **Cursor → Settings → MCP** |
| 2 | **Add connector** OR install from marketplace |
| 3 | **Marketplace (1-click):** https://cursor.com/marketplace/heygen |
| 4 | **Manual URL:** `https://mcp.heygen.com/mcp/v1/` |
| 5 | Click **Connect** → sign in to HeyGen (OAuth) |
| 6 | Confirm HeyGen shows **green / connected** in MCP list |

**No API key needed** for MCP.

### Train Charlotte once (after signup)
| Step | Link |
|------|------|
| 1 | Generate 8 photos using `content/ai-prompts/AVATAR-REFERENCE-PROMPTS.md` |
| 2 | HeyGen → Avatars → Photo Avatar → upload images |
| 3 | Name: `Charlotte Hayes - Saudi Gateway` |
| 4 | Tell agent: *"Charlotte avatar is trained"* |

**Agent uses:** HeyGen MCP tools to generate `hook.mp4`, `bridge-*.mp4`, `close.mp4`

---

## 3. Higgsfield — B-roll + thumbnails (MCP)

### Buy this plan
| | Link |
|---|------|
| **Pricing page** | https://higgsfield.ai/pricing |
| **Plan to choose** | **Plus — $49/month** ($39/mo if annual) |
| **Signup / MCP landing** | https://higgsfield.ai/mcp |
| **Your invite link** | https://higgsfield.ai/mcp?utm_source=yt&utm_medium=video&utm_category=prd&utm_campaign=MCP&utm_creator=HiggsfieldAI&utm_content_type=de&utm_post=DvFoyk&fpr=higgsfieldai&invite_code=mcp-higgsfieldai-DvFoyk |

**Why Plus:** Unlocks **Veo 3.1, Kling 3.0, Sora 2**, Soul Character training, Personal Clipper (Shorts). Starter ($15) does **not** include Veo 3.

### Connect to agent — MCP
| Step | Action |
|------|--------|
| 1 | Open **Cursor → Settings → MCP → Add custom connector** |
| 2 | Name: `Higgsfield` |
| 3 | URL: `https://mcp.higgsfield.ai/mcp` |
| 4 | Click **Connect** → sign in to Higgsfield (OAuth) |
| 5 | Confirm Higgsfield shows **connected** in MCP list |

**No API key needed** for MCP.

**Agent uses:** `generate_video`, `generate_image`, `create_character`, Personal Clipper for Shorts

---

## 4. Cursor environment — summary

After all signups, your Cursor setup should have:

### MCP connectors (Settings → MCP)
| Connector | URL |
|-----------|-----|
| HeyGen | `https://mcp.heygen.com/mcp/v1/` |
| Higgsfield | `https://mcp.higgsfield.ai/mcp` |

### Environment secrets (Cloud Agent settings)
| Secret | Value |
|--------|-------|
| `ELEVENLABS_API_KEY` | Your ElevenLabs API key |
| `ELEVENLABS_VOICE_ID` | Charlotte voice clone ID (after created) |

---

## 5. One message to send the agent when done

Copy-paste this after you've completed signup + connections:

```
All tools connected:
- ElevenLabs Creator — API key added to environment
- HeyGen Creator — MCP connected, Charlotte Hayes avatar trained
- Higgsfield Plus — MCP connected

Please produce Video 01 end-to-end and deliver final.mp4.
```

---

## What you never touch again

| Portal | After setup |
|--------|-------------|
| ElevenLabs website | Agent runs API |
| HeyGen website | Agent runs MCP (except one-time avatar training) |
| Higgsfield website | Agent runs MCP |
| CapCut | **Not needed** — agent uses FFmpeg |
| Canva | **Not needed** |

## What you still do (~10 min/video)

1. Approve `final.mp4` before publish  
2. Upload to YouTube (until we add YouTube API)

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| HeyGen MCP not in Cursor | Use https://cursor.com/marketplace/heygen |
| Higgsfield MCP auth fails | Re-connect at https://higgsfield.ai/mcp |
| ElevenLabs "insufficient credits" | Upgrade to Pro ($99) or wait for monthly reset |
| HeyGen out of credits | 600 credits/mo on Creator — agent batches efficiently |
| Agent can't see MCP tools | Restart Cursor after adding connectors |

---

*Last updated: July 2026*
