# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# ENCRYPTION — Encryption & Key Management (100-control framework)

Türkçe not: Şifreleme (rest/transit), anahtar yönetimi, PQC 100-kontrol çerçevesi. Additive; MODE=ASSESS-ONLY.

> ⚠️ Standard values reproduced for scaffolding — **verify against official source before production**.

## Scope
- TLS / in-transit (modern ciphers)
- At-rest encryption (disk/DB/object)
- Key mgmt: rotation/revocation
- HSM/KMS usage
- PQC readiness (FIPS 203/204/205)

## Control row schema (mandatory — see `.cursor/rules/20-control-mapping.mdc`)
Each of the 100 controls MUST carry all fields below. CIS/OWASP where applicable.

| id | ad | NIST_CSF (2.0) | 800-53 Rev.5 | ISO27001:2022 | CIS v8.1 | OWASP ASVS 5.0.0 | doğrulama_yöntemi | savunma_gerekçesi |
|---|---|---|---|---|---|---|---|---|
| ENC-001 | TLS 1.2+ enforced | PR.DS* | SC-8* | A.8.24* | CIS 3* | ASVS V9 | scan negotiated protocols | protects data in transit |
| ENC-002 | Key rotation policy | PR.DS* | SC-12* | A.8.24* | CIS 3* | — | KMS rotation logs | limits key-compromise blast radius |

`*` = verify id/version against official docs. Rows above are **TEMPLATE examples**, not the final set.

## Note
Do NOT enumerate all 100 controls here in scaffold. Generate in batches via `/kontrol-uret`; keep the stable header. Full content is produced in phased runs. Detections may cite MITRE ATT&CK ids **only** to justify a D3FEND countermeasure.
