# Change Protocol Engine — Outline (skeleton)

GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok. Standard values: verify against official source before production.

## Scope
- Change approval & segregation of duties
- Config baselines & drift detection
- CI/CD security gates (SAST/SCA/secret-scan)
- IaC policy-as-code (OPA) review
- Rollback / recovery

## Example template rows (TEMPLATES — verify)
- `CHG-001 | Peer-reviewed change | PR.PS | CM-3 | A.8.32 (verify) | CIS 4 (verify) | — | PR review evidence | prevents unauthorized/unsafe change`
- `CHG-002 | Secret scanning in CI | PR.PS | SA-11 | A.8.28 (verify) | CIS 16 (verify) | ASVS V14 (verify) | pipeline scan logs | stops secret leakage`

## TODO (phased)
- [ ] Expand to full content in phased runs.
- [ ] Verify every standard id/version against official docs.
