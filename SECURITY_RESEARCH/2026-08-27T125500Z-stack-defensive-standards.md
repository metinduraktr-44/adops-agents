# Research note — Stack-relevant defensive standards (ASSESS-ONLY)

> Damga: 2026-08-27T12:55:00Z · defense guidance only · no PoCs · no exploit steps

## Scope
Map public standards to this repo’s stack (Markdown/JSON component pack, Python stdlib gates, GitHub Actions, Cursor MCP, optional Terraform observability).

## Sources (cited)

| # | Source | URL | Use |
|---|---|---|---|
| 1 | NIST CSF 2.0 (CSWP 29) | https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final | Govern→Recover outcome taxonomy |
| 2 | NIST CSF 2.0 PDF | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf | Primary text |
| 3 | CISA Zero Trust Maturity Model v2.0 | https://www.cisa.gov/sites/default/files/2023-04/zero_trust_maturity_model_v2_508.pdf | Pillar maturity (Identity…Data) |
| 4 | CISA ZTMM v2 alert | https://www.cisa.gov/news-events/alerts/2023/04/11/cisa-releases-zero-trust-maturity-model-version-2 | Publication context |
| 5 | SLSA v1.0 specification | https://slsa.dev/spec/v1.0/ | Build provenance levels (pinned) |
| 6 | SLSA v1.0 levels | https://slsa.dev/spec/v1.0/levels | L1–L3 build guarantees |

## Defensive takeaways (repo-mapped)

### NIST CSF 2.0
- Use **Govern** for MODE flags, expert queues, and SoA ownership (`SECURITY_STATE.md`, COMPLIANCE).
- **Identify**: inventory + attack-surface (this pack’s Faz 1).
- **Protect**: hooks, secret placeholders, branch/CI permissions — map to LAYERS/ENC/COND drafts.
- **Detect / Respond / Recover**: scanner stubs + IR skill playbooks; no live response until MODE=IMPLEMENT + owner criteria.

### CISA ZTMM 2.0
- Score this repo as mostly **Traditional→Initial** on Identity (env tokens, Actions OIDC opportunity) and Applications/Workloads (Actions runners).
- Devices/Networks largely out of band (developer laptops / GitHub SaaS) — document as inherited control assumptions.
- Cross-cutting: Visibility (AUDIT_LOG), Automation (hooks/CI), Governance (ASSESS-ONLY default).

### SLSA (pin v1.0 Build track)
- Current state: provenance **not** produced for script pack → gap vs Build L1 (“provenance exists”).
- ASSESS recommendation: define provenance stub format under `TRANSPARENT_CODE/` evidence; IMPLEMENT only after MODE flip.
- Upstream SLSA v1.2 Source track exists — pin decision recorded in matrix G-MAT-05; do not silently retarget.

### CI / supply chain (defensive)
- Keep workflow `permissions:` least privilege (security-audit already uses contents:read + security-events:write).
- Prefer pinned action SHAs over floating tags when IMPLEMENT hardening begins.
- Refuse: pipe-to-shell installers, root wipe patterns (hooks already block common idioms).

## CVE posture note (defensive, non-exploitative)
- No application runtime dependency tree (stdlib Python + Actions). Priority is **Actions ecosystem** and **secret hygiene**, not classic app CVE farming.
- Process: watch GitHub Advisory / action maintainer channels; triage via `vulnerability-management` skill; record in ASSESSMENTS — never publish exploit reproduction.

## Outputs linked
- `SECURITY_CONTEXT/inventory.md`
- `SECURITY_MATRIX/matrix.md`
- `ASSESSMENTS/gap-2026-08-27.md`
- `COMPLIANCE/soa-iso27001-draft.md`

## Ethics
Defense-only. Refuse weaponization and exploit how-to content.
