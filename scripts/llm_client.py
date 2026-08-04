#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ortak LLM istemcisi — sağlayıcı-bağımsız.
Öncelik: OpenRouter (OpenAI-uyumlu) → Anthropic. İkisi de yoksa None döner (deterministik iskelet).
Env:
  OPENROUTER_API_KEY  (+ opsiyonel OPENROUTER_MODEL, vars. bedava bir model)
  ANTHROPIC_API_KEY   (+ opsiyonel ANTHROPIC_MODEL)
Kural: hiçbir sağlayıcı zorunlu değil; hata/kredi yoksa sessizce None (döngü kırılmaz).
"""
import os, json, urllib.request, urllib.error

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
DEFAULT_OR_MODEL = "meta-llama/llama-3.3-70b-instruct:free"
DEFAULT_ANT_MODEL = "claude-sonnet-4-5"


def provider():
    if os.environ.get("OPENROUTER_API_KEY", "").strip():
        return "openrouter"
    if os.environ.get("ANTHROPIC_API_KEY", "").strip():
        return "anthropic"
    return None


def _openrouter(prompt, max_tokens, model):
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not key:
        return None
    model = model or os.environ.get("OPENROUTER_MODEL", DEFAULT_OR_MODEL)
    body = json.dumps({"model": model, "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request(OPENROUTER_URL, data=body, headers={
        "Authorization": "Bearer " + key, "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/metinduraktr-44/adops-agents",
        "X-Title": "adops-agents"})
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.loads(r.read())
    return "".join(c.get("message", {}).get("content", "") for c in d.get("choices", []))


def _anthropic(prompt, max_tokens, model):
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        return None
    model = model or os.environ.get("ANTHROPIC_MODEL", DEFAULT_ANT_MODEL)
    body = json.dumps({"model": model, "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request(ANTHROPIC_URL, data=body, headers={
        "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.loads(r.read())
    return "".join(b.get("text", "") for b in d.get("content", []))


def complete(prompt, max_tokens=1200, model=None):
    """Metin döndür veya None. Sağlayıcı sırası: OpenRouter → Anthropic."""
    order = []
    if os.environ.get("OPENROUTER_API_KEY", "").strip():
        order.append(_openrouter)
    if os.environ.get("ANTHROPIC_API_KEY", "").strip():
        order.append(_anthropic)
    for fn in order:
        try:
            out = fn(prompt, max_tokens, model)
            if out and out.strip():
                return out
        except urllib.error.HTTPError as e:
            print(f"LLM {fn.__name__[1:]} HTTP{e.code}:", e.read().decode()[:160])
        except Exception as e:
            print(f"LLM {fn.__name__[1:]} skipped:", type(e).__name__, str(e)[:140])
    return None


if __name__ == "__main__":
    p = provider()
    print("provider:", p or "(yok — deterministik)")
    if p:
        out = complete("Reply with exactly: OK", max_tokens=8)
        print("test:", (out or "").strip()[:60] or "(boş/başarısız)")
