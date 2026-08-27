# LAYERS Engine — Outline (skeleton)

GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok. Standard values: verify against official source before production.

## Layer taxonomy (100-control target)
1. Perimeter / network defense (firewalls handled in FIREWALLS; here: segmentation, NAC).
2. Host / endpoint hardening (EDR, baseline, patching).
3. Application security (secure SDLC, ASVS).
4. Data protection (classification, DLP, encryption pointers → ENCRYPTION).
5. Identity & access (→ iam-hardening, zero-trust-architect).
6. Detection & monitoring (→ detection-engineering).

## Control row schema
`id | ad | NIST_CSF | 800-53 | ISO27001 | CIS | OWASP | doğrulama_yöntemi | savunma_gerekçesi`

## Example template rows (TEMPLATES — replace/verify)
- `LAY-001 | Network segmentation | PR.AA / PR.IR | SC-7 | A.8.20 (verify) | CIS 12 (verify) | — | review VLAN/ACL config + test isolation | limits lateral movement (defense)`
- `LAY-002 | Endpoint baseline hardening | PR.PS | CM-6 | A.8.9 (verify) | CIS 4 (verify) | — | CIS-benchmark scan evidence | reduces exploitable surface (defense)`

## TODO (phased)
- [ ] Enumerate remaining 98 controls in batches via `/kontrol-uret`.
- [ ] Verify every standard id against official docs.
