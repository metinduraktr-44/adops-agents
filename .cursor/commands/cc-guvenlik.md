---
description: Claude Code / Cursor security warnings checklist (defense-only).
---
# /cc-guvenlik

Objective: apply owner security warnings without paste; scanners only.

```bash
python3 scripts/prompt_injection_guard.py
python3 scripts/secret_scan.py .
python3 scripts/ethics_check.py .
python3 scripts/validate.py
```

Requirements:
- Defense-only. No exploit/PoC. No plaintext secrets.
- Do not delete Security GIGA / LATOS / Canva hooks.
- Report: GEÇTİ/KALDI + owner-gated leftovers from `docs/CLAUDE-CODE-GUVENLIK-UYGULAMA.md`.

Output: stamp `AUDIT_LOG.jsonl` + one line in `BILGI_TABANI.md`.
