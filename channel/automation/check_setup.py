#!/usr/bin/env python3
"""Verify Saudi Gateway API connections (ElevenLabs, HeyGen, Higgsfield)."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

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
        print("    Get key: https://app.heygen.com/settings/api")
        return False
    try:
        status, data = http_get(
            "https://api.heygen.com/v2/avatars",
            {"X-Api-Key": key},
        )
        avatar_id = check_env("HEYGEN_AVATAR_ID")
        avatar_note = f", Charlotte avatar: {avatar_id}" if avatar_id else ", HEYGEN_AVATAR_ID not set (train Charlotte first)"
        count = len(data.get("data", {}).get("avatars", data.get("data", [])))
        print(f"{OK} HeyGen — API key valid (HTTP {status}), {count} avatars visible{avatar_note}")
        return True
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:200] if e.fp else ""
        print(f"{FAIL} HeyGen — HTTP {e.code}: {body}")
        return False
    except Exception as e:
        print(f"{FAIL} HeyGen — {e}")
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
        print("All systems ready. Agent can produce Video 01.")
        return 0
    print("Fix missing secrets at: https://cursor.com/dashboard/cloud-agents → Secrets")
    print("Then start a NEW Cloud Agent and run this check again.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
