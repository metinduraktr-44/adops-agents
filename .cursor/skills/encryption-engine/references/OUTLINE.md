# Encryption Engine — Outline (skeleton)

GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok. Standard values: verify against official source before production.

## Scope
- TLS / in-transit (modern ciphers only)
- At-rest encryption (disk, DB, object)
- Key management: generation, storage, rotation, revocation
- PQC migration readiness (FIPS 203 ML-KEM / 204 ML-DSA / 205 SLH-DSA — verify)
- Crypto inventory (→ crypto-agility)

## Example template rows (TEMPLATES — verify)
- `ENC-001 | TLS 1.2+ enforced | PR.DS | SC-8 | A.8.24 (verify) | CIS 3 (verify) | ASVS V9 (verify) | scan negotiated protocols | protects data in transit`
- `ENC-002 | Key rotation policy | PR.DS | SC-12 | A.8.24 (verify) | CIS 3 (verify) | — | KMS rotation logs | limits key-compromise blast radius`

## TODO (phased)
- [ ] Expand to full content in phased runs.
- [ ] Verify every standard id/version against official docs.
