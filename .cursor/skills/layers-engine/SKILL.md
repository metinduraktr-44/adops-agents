---
name: layers-engine
description: Use when generating or mapping the defense-in-depth LAYERS 100-control framework (network, host, app, data, identity layers).
icon: shield
---

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# Layers Engine

## Instructions
Generate/maintain the `LAYERS/` defense-in-depth control set (100 controls target).
1. Follow `.cursor/rules/20-control-mapping.mdc` — every control row carries `id, ad, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi`.
2. Cover layers: perimeter/network, host/endpoint, application, data, identity, monitoring.
3. Reproduce standard values with a "verify against official source before production" banner.
4. Batch output via `/kontrol-uret`; append with a stable header. No secrets, defense-only.

## References
- `references/OUTLINE.md` — full layer taxonomy + 100-control outline (filled in phases).

## Note
Full ~20k-char content is produced later in phases. This is the discoverable skeleton.
