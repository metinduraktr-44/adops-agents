# Firewall Engine — Outline (skeleton)

GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok. Standard values: verify against official source before production.

## Scope
- Network ACL / segmentation policy
- Host-based firewall baselines
- WAF rules (OWASP ASVS 5.0.0 aligned — verify)
- Cloud SG / NSG least-exposure
- Egress filtering & allowlists

## Example template rows (TEMPLATES — verify)
- `FW-001 | Default-deny ingress | PR.IR | SC-7 | A.8.20 (verify) | CIS 4 (verify) | — | ruleset review + connectivity test | minimizes exposed surface`
- `FW-002 | Egress allowlist | DE.CM | SC-7(5) | A.8.20 (verify) | CIS 4 (verify) | — | egress log review | curbs C2/exfil channels (detective/defensive)`

## TODO (phased)
- [ ] Expand to full content in phased runs.
- [ ] Verify every standard id/version against official docs.
