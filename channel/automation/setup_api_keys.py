#!/usr/bin/env python3
"""
Diagnose API keys and print exact fixes.

Usage:
  python3 setup_api_keys.py          # check all
  python3 setup_api_keys.py --write  # create local.env template

Keys can live in:
  1. Cursor Cloud Agent Secrets (recommended)
  2. channel/automation/local.env (gitignored — paste keys here)
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request

import api_config

TEMPLATE = """# Saudi Gateway API keys — gitignored, never commit
# Get keys then run: python3 setup_api_keys.py

ELEVENLABS_API_KEY=
ELEVENLABS_VOICE_ID=Xb7hH8MSUJpSbSDYk0k2

# https://app.heygen.com/settings?nav=API  (type: API, not Agent)
HEYGEN_API_KEY=
HEYGEN_AVATAR_ID=

# https://platform.higgsfield.ai
HIGGSFIELD_API_KEY=
HIGGSFIELD_API_SECRET=

# FREE alternative for B-roll: https://www.pexels.com/api/
PEXELS_API_KEY=
"""


def http_get(url: str, headers: dict) -> tuple[int, str]:
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status, resp.read().decode()[:400]
    except urllib.error.HTTPError as e:
        return e.code, (e.read().decode()[:400] if e.fp else str(e))


def check_elevenlabs() -> bool:
    key = api_config.get("ELEVENLABS_API_KEY")
    if not key:
        print("✗ ElevenLabs — ELEVENLABS_API_KEY missing")
        return False
    code, body = http_get("https://api.elevenlabs.io/v1/user", {"xi-api-key": key})
    if code == 200:
        print(f"✓ ElevenLabs — OK (voice: {api_config.get('ELEVENLABS_VOICE_ID') or 'default'})")
        return True
    print(f"✗ ElevenLabs — HTTP {code}")
    return False


def check_heygen() -> bool:
    key = api_config.get("HEYGEN_API_KEY")
    if not key:
        print("✗ HeyGen — HEYGEN_API_KEY missing")
        print("  → https://app.heygen.com/settings?nav=API")
        return False
    for url in ("https://api.heygen.com/v1/user/me", "https://api.heygen.com/v3/users/me"):
        code, body = http_get(url, {"X-Api-Key": key})
        if code == 200 and ("code\":100" in body.replace(" ", "") or '"code": 100' in body):
            av = api_config.get("HEYGEN_AVATAR_ID")
            print(f"✓ HeyGen — OK ({url})" + (f", avatar={av}" if av else ", no HEYGEN_AVATAR_ID yet"))
            return True
        if code == 200:
            print(f"✓ HeyGen — OK ({url})")
            return True
    print("✗ HeyGen — 401 Unauthorized (key is INVALID — must regenerate)")
    print("  Your current key starts with:", key[:12] + "...")
    print()
    print("  FIX (5 min):")
    print("  1. https://app.heygen.com/settings?nav=API")
    print("  2. Delete old key")
    print("  3. Create NEW key → choose type **API** (not Agent)")
    print("  4. Top up wallet: https://www.heygen.com/api-pricing")
    print("  5. Update HEYGEN_API_KEY in Cursor Secrets OR local.env")
    print("  6. Test: curl -s https://api.heygen.com/v1/user/me -H \"X-Api-Key: NEW_KEY\"")
    print("  7. Start NEW Cloud Agent")
    return False


def check_higgsfield() -> bool:
    kid = api_config.get("HIGGSFIELD_API_KEY")
    secret = api_config.get("HIGGSFIELD_API_SECRET")
    if not kid or not secret:
        print("✗ Higgsfield — keys missing")
        print("  → https://platform.higgsfield.ai")
        print("  OR use FREE Pexels instead: https://www.pexels.com/api/ → PEXELS_API_KEY")
        return False
    auth = f"Key {kid}:{secret}"
    code, body = http_get("https://platform.higgsfield.ai/v1/models", {"Authorization": auth})
    if code == 200:
        print("✓ Higgsfield — OK")
        return True
    print(f"✗ Higgsfield — HTTP {code}")
    return False


def check_pexels() -> bool:
    key = api_config.get("PEXELS_API_KEY")
    if not key:
        print("○ Pexels — not set (optional FREE B-roll backup)")
        return False
    code, body = http_get(
        "https://api.pexels.com/videos/search?query=riyadh&per_page=1",
        {"Authorization": key},
    )
    if code == 200:
        print("✓ Pexels — OK (free B-roll alternative to Higgsfield)")
        return True
    print(f"✗ Pexels — HTTP {code}")
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Write local.env template")
    args = parser.parse_args()

    if args.write:
        path = api_config.ROOT / "local.env"
        if path.exists():
            print(f"Already exists: {path}")
        else:
            path.write_text(TEMPLATE, encoding="utf-8")
            print(f"Created {path} — paste your keys, then run setup_api_keys.py again")
        return 0

    api_config.load_env_files()
    print("Saudi Gateway — API key diagnostic\n")
    print("Key sources: Cursor Secrets + local.env + .env\n")

    results = {
        "ElevenLabs": check_elevenlabs(),
        "HeyGen": check_heygen(),
        "Higgsfield": check_higgsfield(),
        "Pexels": check_pexels(),
    }

    print()
    ok = sum(1 for v in results.values() if v)
    if results["ElevenLabs"] and (results["HeyGen"] or results["Pexels"]):
        print("✓ Ready for premium production:")
        print("  python3 produce_video.py --premium")
    elif results["ElevenLabs"]:
        print("✓ Ready for standard production (no HeyGen/Higgsfield):")
        print("  python3 produce_video.py")
    else:
        print("Add at least ELEVENLABS_API_KEY to Cursor Secrets or local.env")

    print("\nFull guide: channel/FIX-API-KEYS.md")
    return 0 if results["ElevenLabs"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
