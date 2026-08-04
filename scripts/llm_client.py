#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared LLM client: OpenRouter (preferred) or Anthropic.

Loads secrets from env and optional .env / .env.local (never committed).
TR: Anahtar repoya yazılmaz; sadece lokal env.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_dotenv() -> None:
    for name in (".env.local", ".env"):
        path = ROOT / name
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v


def llm(prompt: str, max_tokens: int = 1600) -> str | None:
    """Return completion text or None if no key / request fails."""
    load_dotenv()
    or_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    anth_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    provider = os.environ.get("LLM_PROVIDER", "").strip().lower()

    if or_key and (provider in ("", "openrouter", "auto") or not anth_key):
        return _openrouter(or_key, prompt, max_tokens)
    if anth_key:
        return _anthropic(anth_key, prompt, max_tokens)
    print("LLM SKIPPED: no OPENROUTER_API_KEY or ANTHROPIC_API_KEY")
    return None


def _openrouter(key: str, prompt: str, max_tokens: int) -> str | None:
    model = os.environ.get("OPENROUTER_MODEL", "anthropic/claude-sonnet-4").strip()
    body = json.dumps(
        {
            "model": model,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }
    ).encode()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/metinduraktr-44/adops-agents",
            "X-Title": "AdOps Agents daily-ops",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.loads(r.read())
        choices = data.get("choices") or []
        if not choices:
            print("LLM SKIPPED: openrouter empty choices", data.get("error"))
            return None
        msg = choices[0].get("message") or {}
        return (msg.get("content") or "").strip() or None
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")[:400]
        print(f"LLM SKIPPED: openrouter HTTP {e.code}: {err}")
        return None
    except Exception as e:
        print("LLM SKIPPED:", e)
        return None


def _anthropic(key: str, prompt: str, max_tokens: int) -> str | None:
    body = json.dumps(
        {
            "model": "claude-sonnet-4-5",
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }
    ).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.loads(r.read())
        return "".join(b.get("text", "") for b in data.get("content", [])) or None
    except Exception as e:
        print("LLM SKIPPED:", e)
        return None


if __name__ == "__main__":
    load_dotenv()
    has_or = bool(os.environ.get("OPENROUTER_API_KEY"))
    has_an = bool(os.environ.get("ANTHROPIC_API_KEY"))
    print(f"openrouter={'set' if has_or else 'missing'} anthropic={'set' if has_an else 'missing'}")
    out = llm("Reply with exactly: PONG", max_tokens=16)
    print("reply:", (out or "")[:80])
