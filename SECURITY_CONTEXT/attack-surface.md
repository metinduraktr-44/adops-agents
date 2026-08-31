# Attack Surface — Defense View

> HAND_AUTHORED · Damga: 2026-08-27T12:55:00Z · what to **protect**, not how to attack

## Surfaces (repo-derived)

1. **Source repository** — unauthorized commits, secret commits, dependency confusion on Actions
2. **CI/CD workflows** (14 YAML) — poisoned actions, over-privileged tokens; prefer `${{ secrets.* }}` + least privilege `permissions:`
3. **SARIF / code scanning upload** (`security-audit.yml`) — integrity of validate output; write scope limited to `security-events`
4. **Cursor MCP integrations** — Canva active; security catalog entries must stay off until Authorize; token theft if misconfigured
5. **Hooks** — `afterFileEdit` secret/ethics scans; `beforeShellExecution` blocks dangerous wipe/pipe-to-shell idioms
6. **Generated scripts & nightly writers** — prompt injection into agency components; audit chain tampering
7. **LLM client env keys** (`scripts/llm_client.py`) — key presence in runner env; never commit `.env`
8. **Terraform observability module** — provider credentials (Datadog/Sentry/PagerDuty) if applied outside vaulted CI
9. **Data archives** — `data/arsiv/**` integrity and over-sharing
10. **Holding / country LLM content** — privacy overlay (KVKK/GDPR checklists exist as agents; need evidence linkage)
11. **Creative GIGA coexistence** — accidental overwrite of Canva assets; keep namespaces separate

## Priority controls (map to families)
| Surface | Primary families / skills |
|---|---|
| Secrets / env | ENC · TC · `secret-hygiene` |
| Change integrity | CHANGE · `change-protocol-engine` |
| CI / SBOM / provenance | TRANSPARENT_CODE · `sbom-provenance` |
| Identity to MCP/CI | CONDITIONAL · `iam-hardening` · `conditional-policy-engine` |
| Network egress assumptions | FIREWALLS (policy templates) |
| Defense-in-depth docs | LAYERS · `layers-engine` |
| Detection / IR readiness | `detection-engineering` · `incident-response` |
| Privacy / holding | `privacy-engineering` · COMPLIANCE SoA |

## Observed strengths (ASSESS)
- Hooks run secret_scan + ethics_check on edit
- Security GIGA MODE defaults ASSESS-ONLY
- MCP security examples use `${VAR}` placeholders only
- Weekly security-audit workflow exists

## Observed gaps (ASSESS — no remediations yet)
- No checked-in SBOM / SLSA provenance for script pack
- Expert mapping review still open on 600 draft controls
- Terraform module is reference-only; apply path undocumented in SECURITY_CONTEXT
- Country/OpCo privacy DPIA stubs not yet linked to SoA

## Out of scope here
Exploit development, PoC content, and any weaponization — **forbidden** (defense-only).
