---
name: secret-hygiene
description: Use when auditing or preventing secret leakage across the repo/pipelines (scan, redact, rotate guidance).
icon: shield
---

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# Secret Hygiene

## Instructions
1. Detect and redact secrets; never write plaintext or realistic-format fake secrets.
2. Reference `${VAR}`/`vault://`/`op://` only; recommend rotation on exposure.
3. Use `scripts/secret_scan.py` outputs; log REDACTED findings only.

## References
- `references/OUTLINE.md` — depth outline (filled in phases).

## Note
Full ~20k-char content is produced later in phases. This is the discoverable skeleton.
