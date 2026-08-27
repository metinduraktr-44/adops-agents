# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# Security Master Plan — Security Governance OS (Bölüm 13)

Türkçe not: Faz 0..8 yürütme planı. `/sec-devam` / `/sec-resume` bu listedeki ilk işaretlenmemiş maddeden devam eder. Varsayılan mod: **MODE=ASSESS-ONLY** (savunma-only, yan etki yok). Yaratıcı-ajans `master-plan.md`'den ayrıdır.

Current mode: `MODE=ASSESS-ONLY` · defense-only · See `SECURITY_STATE.md` for live state.

## Faz 0 — Context & Bootstrap
- [ ] Confirm scaffold present (`.cursor/` security rules/commands/skills/agents/hooks, `tools/security-scanners/`, Bölüm 12 folders).
- [ ] Fill `SECURITY_CONTEXT/inventory.md` (assets, data classes, dependencies — no secrets).
- [ ] Fill `SECURITY_CONTEXT/attack-surface.md` (defensive surface map).

## Faz 1 — Research & Standards Watch
- [ ] `SECURITY_RESEARCH/standards-watch.md` — NIST CSF 2.0, 800-53 Rev.5, ISO 27001:2022, CIS v8.1, OWASP ASVS 5.0.0, PQC (FIPS 203/204/205), SLSA v1.0, 800-207/ZTMM 2.0 (each with verify-banner).
- [ ] `SECURITY_RESEARCH/threat-landscape.md` — defensive trends (no offensive TTP recipes).

## Faz 2 — Org & Roles
- [ ] `ORG/ROLES/README.md` — 40+ security roles (Bölüm 5, C-level → SOC). Map roles → skills.

## Faz 3 — Experts Engine
- [ ] `EXPERTS/SECURITY_DIGEST.md` — seed roster + monthly loop (READ→DELTA→DIFF→WRITE→DIGEST).
- [ ] Mark all unsourced claims `araştırılacak / URL doğrulanmalı`. Dan Kaminsky = historical (2021).

## Faz 4 — 6×100 Control Frameworks
- [ ] `LAYERS/` `FIREWALLS/` `ENCRYPTION/` `CHANGE/` `TRANSPARENT_CODE/` `CONDITIONAL/` — generate controls in batches via `/kontrol-uret`.
- [ ] Every control mapped (id, ad, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi) with verify-banner.

## Faz 5 — Cross-Map Matrix
- [ ] `SECURITY_MATRIX/matrix.md` — cross-standard map populated from framework folders.

## Faz 6 — Implementation Artifacts
- [ ] `IMPLEMENTATION/hardening|detections|runbooks|policies` — defensive artifacts (Sigma/YARA/EDR, IR runbooks, OPA policies).
- [ ] Detections cite ATT&CK ids **only** to justify a D3FEND countermeasure.

## Faz 7 — Assessments & Gap Analysis
- [ ] `ASSESSMENTS/` — gap analysis (`/gap-analizi`), threat models, posture reviews.

## Faz 8 — Compliance Package
- [ ] `COMPLIANCE/` — ISO 27001:2022 SoA + evidence package (`/compliance-paket`), verify-banners.
- [ ] `python3 scripts/validate.py` → `VALIDATION: GECTI`. Ethics + secret audit clean (`/etik-denetim`).

## Global guardrails (every phase)
- MODE=ASSESS-ONLY; defense-only; no secrets/accounts/network; MCP default OFF.
- Additive only — never touch `components/**` or `data/**`.
