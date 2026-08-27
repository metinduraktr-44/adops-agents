---
name: incident-response
description: Use when building incident-response runbooks or triage flows (NIST 800-61 lifecycle), defense-only.
icon: shield
---

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# Incident Response

## Instructions
1. Produce IR runbooks: prepare → detect/analyze → contain → eradicate → recover → post-incident (NIST 800-61 — verify).
2. Reference detections (→ detection-engineering); redact any secret/IoC credential to `<REDACTED>`.
3. MODE=ASSESS-ONLY: artifacts only, no live actions.

## References
- `references/OUTLINE.md` — depth outline (filled in phases).

## Note
Full ~20k-char content is produced later in phases. This is the discoverable skeleton.
