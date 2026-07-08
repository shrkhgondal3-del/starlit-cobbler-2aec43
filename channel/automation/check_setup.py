#!/usr/bin/env python3
"""Verify Saudi Gateway API connections (ElevenLabs, HeyGen, Higgsfield)."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

import api_config

api_config.load_env_files()

OK = "✓"
FAIL = "✗"


def check_env(name: str) -> str | None:
    val = os.environ.get(name, "").strip()
    return val if val else None


def http_get(url: str, headers: dict[str, str]) -> tuple[int, dict]:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.status, json.loads(resp.read().decode())


def http_post(url: str, headers: dict[str, str], body: dict) -> tuple[int, dict]:
    data = json.dumps(body).encode()
    h = {**headers, "Content-Type": "application/json"}
    req = urllib.request.Request(url, data=data, headers=h, method="POST")
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.status, json.loads(resp.read().decode())


def check_elevenlabs() -> bool:
    key = check_env("ELEVENLABS_API_KEY")
    if not key:
        print(f"{FAIL} ElevenLabs — ELEVENLABS_API_KEY not set")
        return False
    try:
        status, _ = http_get(
            "https://api.elevenlabs.io/v1/user",
            {"xi-api-key": key},
        )
        voice = check_env("ELEVENLABS_VOICE_ID") or "(default)"
        print(f"{OK} ElevenLabs — API key valid (HTTP {status}), voice: {voice}")
        return True
    except urllib.error.HTTPError as e:
        print(f"{FAIL} ElevenLabs — HTTP {e.code}")
        return False
    except Exception as e:
        print(f"{FAIL} ElevenLabs — {e}")
        return False


def check_heygen() -> bool:
    key = check_env("HEYGEN_API_KEY")
    if not key:
        print(f"{FAIL} HeyGen — HEYGEN_API_KEY not set")
        print("    Get key: https://app.heygen.com/settings?nav=API")
        print("    Or skip keys: python3 produce_video.py  (see ../FIX-API-KEYS.md)")
        return False

    # Detect common paste mistakes
    if key.startswith("sk_V2_") and len(key) < 40:
        print(f"{FAIL} HeyGen — key looks truncated or wrong type")
        print("    Create a new API key (not Agent key) at app.heygen.com/settings?nav=API")
        return False

    endpoints = [
        "https://api.heygen.com/v1/user/me",
        "https://api.heygen.com/v2/avatars",
    ]
    last_err = ""
    for url in endpoints:
        try:
            status, data = http_get(url, {"X-Api-Key": key})
            avatar_id = check_env("HEYGEN_AVATAR_ID")
            avatar_note = (
                f", Charlotte avatar: {avatar_id}"
                if avatar_id
                else ", HEYGEN_AVATAR_ID not set (optional — uses Video Agent)"
            )
            code = data.get("code")
            if code == 100 or status == 200:
                print(f"{OK} HeyGen — API key valid ({url}){avatar_note}")
                return True
            print(f"{OK} HeyGen — API key valid (HTTP {status}){avatar_note}")
            return True
        except urllib.error.HTTPError as e:
            last_err = e.read().decode()[:300] if e.fp else str(e)
            if e.code != 401:
                break

    print(f"{FAIL} HeyGen — HTTP 401 Unauthorized")
    print(f"    Response: {last_err}")
    print("    FIX:")
    print("      1. Open https://app.heygen.com/settings?nav=API")
    print("      2. Delete old key → Create new API key (type: API, not Agent)")
    print("      3. Top up API wallet: https://www.heygen.com/api-pricing")
    print("      4. Paste into Cursor Secrets as HEYGEN_API_KEY")
    print("      5. Start a NEW Cloud Agent")
    print("    OR skip HeyGen: python3 produce_video.py  (see channel/FIX-API-KEYS.md)")
    return False


def check_higgsfield() -> bool:
    api_key = check_env("HIGGSFIELD_API_KEY")
    api_secret = check_env("HIGGSFIELD_API_SECRET")
    if not api_key or not api_secret:
        print(f"{FAIL} Higgsfield — HIGGSFIELD_API_KEY and HIGGSFIELD_API_SECRET required")
        print("    Get keys: https://platform.higgsfield.ai")
        return False
    auth = f"Key {api_key}:{api_secret}"
    try:
        status, _ = http_get(
            "https://platform.higgsfield.ai/v1/models",
            {"Authorization": auth},
        )
        print(f"{OK} Higgsfield — API credentials valid (HTTP {status})")
        return True
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            print(f"{FAIL} Higgsfield — HTTP {e.code} (check key + secret)")
            return False
        # Some endpoints may 404; try a lightweight POST probe
        try:
            status, _ = http_post(
                "https://platform.higgsfield.ai/v1/text2image/soul",
                {"Authorization": auth},
                {"prompt": "test", "batch_size": 1},
            )
            print(f"{OK} Higgsfield — API reachable (HTTP {status})")
            return True
        except urllib.error.HTTPError as e2:
            if e2.code in (400, 402, 422):
                print(f"{OK} Higgsfield — API auth OK (HTTP {e2.code} on test — expected)")
                return True
            print(f"{FAIL} Higgsfield — HTTP {e2.code}")
            return False
    except Exception as e:
        print(f"{FAIL} Higgsfield — {e}")
        return False


def main() -> int:
    print("Saudi Gateway — API connection check\n")
    results = [
        check_elevenlabs(),
        check_heygen(),
        check_higgsfield(),
    ]
    print()
    if all(results):
        print("All systems ready. Agent can produce Video 01 with premium APIs.")
        return 0
    print()
    print("API keys not fully working — you can still produce Video 01:")
    print("  cd channel/automation && python3 produce_video.py")
    print()
    print("Fix keys: python3 setup_api_keys.py")
    print("Guide:   channel/FIX-API-KEYS.md")
    print("Then start a NEW Cloud Agent.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
