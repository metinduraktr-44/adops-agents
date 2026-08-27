---
name: sbom-provenance
description: SBOM, SLSA v1.0 provenance, supply-chain attestations.
---

# sbom-provenance

> TR: Savunma-only skill. Keşfedilmezse inline path kullan.
> Damga: 2026-08-27T12:40:00Z

## Guardrail
- **DEFENSE-ONLY** — no exploit, PoC, bypass, phishing, C2, ransomware.
- ATT&CK only for detect/defend mapping; prefer **D3FEND**.
- Secrets: `${VAR}`, `vault://`, `op://`, `<REDACTED>` only.
- K-003: no 900k blob; expand via `references/` + generator.

## If skill not discovered (inline path)
1. Read `docs/CURSOR-SECURITY-GIGA-MASTER-PROMPT.md`
2. Read `SECURITY_STATE.md` (MODE default ASSESS-ONLY)
3. Open `references/` in this skill folder
4. Prefer `/sec-*` commands over free-form offense requests

## Progressive disclosure
- `references/overview.md` — scope + ethics
- `references/control-templates.md` — control field schema
- `references/playbook.md` — operator steps for ASSESS→IMPLEMENT
- `references/standards.md` — version-pinned standards table
- `references/d3fend-map.md` — defense mapping stubs

## Outputs
- ASSESS-ONLY: gap notes under `ASSESSMENTS/`
- IMPLEMENT: only when `SECURITY_STATE.md` MODE=IMPLEMENT (stubs first)
