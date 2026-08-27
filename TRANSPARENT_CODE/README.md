# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# TRANSPARENT_CODE — Transparent Code & Supply Chain (100-control framework)

Türkçe not: Güvenli SDLC, SBOM, provenance (SLSA) 100-kontrol çerçevesi. Additive; MODE=ASSESS-ONLY.

> ⚠️ Standard values reproduced for scaffolding — **verify against official source before production**.

## Scope
- Secure coding standards (ASVS)
- Dependency transparency & pinning
- SBOM generation
- Build provenance / SLSA v1.0
- Artifact signing & verification

## Control row schema (mandatory — see `.cursor/rules/20-control-mapping.mdc`)
Each of the 100 controls MUST carry all fields below. CIS/OWASP where applicable.

| id | ad | NIST_CSF (2.0) | 800-53 Rev.5 | ISO27001:2022 | CIS v8.1 | OWASP ASVS 5.0.0 | doğrulama_yöntemi | savunma_gerekçesi |
|---|---|---|---|---|---|---|---|---|
| TC-001 | SBOM per build | ID.AM* | SA-15* | A.8.28* | CIS 2* | — | SBOM artifact present | supply-chain visibility |
| TC-002 | Signed artifacts | PR.DS* | SA-10* | A.8.28* | CIS 2* | — | signature verification log | integrity / anti-tamper |

`*` = verify id/version against official docs. Rows above are **TEMPLATE examples**, not the final set.

## Note
Do NOT enumerate all 100 controls here in scaffold. Generate in batches via `/kontrol-uret`; keep the stable header. Full content is produced in phased runs. Detections may cite MITRE ATT&CK ids **only** to justify a D3FEND countermeasure.
