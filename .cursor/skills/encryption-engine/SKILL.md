---
name: encryption-engine
description: Use when generating or mapping the ENCRYPTION 100-control framework (data-at-rest/in-transit, key mgmt, PQC).
icon: shield
---

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# Encryption Engine

## Instructions
1. Generate/maintain `ENCRYPTION/` controls: TLS, at-rest encryption, key management/rotation, HSM/KMS, PQC readiness (FIPS 203/204/205 — verify).
2. Never embed keys/secrets — reference `${VAR}`/`vault://`/`op://` only.
3. Map per `20-control-mapping.mdc`; add verify-banner. Defense-only.

## References
- `references/OUTLINE.md` — depth outline (filled in phases).

## Note
Full ~20k-char content is produced later in phases. This is the discoverable skeleton.
