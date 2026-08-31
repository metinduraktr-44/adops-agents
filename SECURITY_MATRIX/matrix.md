# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# SECURITY_MATRIX — Cross-Standard Control Map (Bölüm 8)

Türkçe not: 6×100 kontrolleri standartlara çapraz eşleyen ana matris. MODE=ASSESS-ONLY.

> ⚠️ Standard values reproduced for scaffolding — **verify against official source before production**.

## Standards in scope (Bölüm 8)
| standard | version | scope note (verify) |
|---|---|---|
| NIST CSF | 2.0 | Functions: Govern, Identify, Protect, Detect, Respond, Recover |
| NIST SP 800-53 | Rev.5 | control catalog (~1,189–1,196 controls across families) |
| ISO/IEC 27001 | 2022 | 93 Annex A controls (4 themes) |
| CIS Controls | v8.1 | 18 controls / safeguards |
| OWASP ASVS | 5.0.0 | application security verification requirements |
| PQC (FIPS) | 203 / 204 / 205 | ML-KEM / ML-DSA / SLH-DSA |
| SLSA | v1.0 | supply-chain build provenance levels |
| NIST SP 800-207 / CISA ZTMM | 800-207 / ZTMM 2.0 | zero-trust architecture / maturity model |

## Cross-map schema
| control_id | framework (LAYERS/…/CONDITIONAL) | NIST_CSF 2.0 | 800-53 Rev.5 | ISO27001:2022 | CIS v8.1 | OWASP ASVS 5.0.0 | notes / verify |
|---|---|---|---|---|---|---|---|
| LAY-001 | LAYERS | PR.AA/PR.IR | SC-7 | A.8.20 | CIS 12 | — | template — verify ids |
| ENC-001 | ENCRYPTION | PR.DS | SC-8 | A.8.24 | CIS 3 | ASVS V9 | template — verify ids |

## Rules
- Populate from the framework folders as controls are generated (`/kontrol-uret`); feed `/gap-analizi` and `/compliance-paket`.
- No fabricated ids; mark uncertain mappings `araştırılacak`. No secrets. Defense-only.
