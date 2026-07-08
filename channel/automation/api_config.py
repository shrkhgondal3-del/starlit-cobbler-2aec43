"""Load and validate Saudi Gateway API credentials."""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).parent


def load_env_files() -> None:
    """Load local.env then .env (gitignored) into os.environ if not already set."""
    for name in ("local.env", ".env"):
        path = ROOT / name
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = val


def get(name: str, default: str = "") -> str:
    load_env_files()
    return os.environ.get(name, default).strip()


def heygen_configured() -> bool:
    return bool(get("HEYGEN_API_KEY"))


def higgsfield_configured() -> bool:
    return bool(get("HIGGSFIELD_API_KEY") and get("HIGGSFIELD_API_SECRET"))


def pexels_configured() -> bool:
    return bool(get("PEXELS_API_KEY"))


def elevenlabs_configured() -> bool:
    return bool(get("ELEVENLABS_API_KEY"))
