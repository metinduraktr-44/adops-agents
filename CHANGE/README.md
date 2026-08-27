# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# CHANGE — Change & Configuration Protocol (100-control framework)

Türkçe not: Değişiklik/konfig yönetimi, CI/CD kapıları, IaC 100-kontrol çerçevesi. Additive; MODE=ASSESS-ONLY.

> ⚠️ Standard values reproduced for scaffolding — **verify against official source before production**.

## Scope
- Change approval & SoD
- Config baselines & drift detection
- CI/CD security gates
- IaC policy-as-code review
- Rollback / recovery

## Control row schema (mandatory — see `.cursor/rules/20-control-mapping.mdc`)
Each of the 100 controls MUST carry all fields below. CIS/OWASP where applicable.

| id | ad | NIST_CSF (2.0) | 800-53 Rev.5 | ISO27001:2022 | CIS v8.1 | OWASP ASVS 5.0.0 | doğrulama_yöntemi | savunma_gerekçesi |
|---|---|---|---|---|---|---|---|---|
| CHG-001 | Peer-reviewed change | PR.PS* | CM-3* | A.8.32* | CIS 4* | — | PR review evidence | prevents unauthorized/unsafe change |
| CHG-002 | Secret scanning in CI | PR.PS* | SA-11* | A.8.28* | CIS 16* | ASVS V14 | pipeline scan logs | stops secret leakage |

`*` = verify id/version against official docs. Rows above are **TEMPLATE examples**, not the final set.

## Note
Do NOT enumerate all 100 controls here in scaffold. Generate in batches via `/kontrol-uret`; keep the stable header. Full content is produced in phased runs. Detections may cite MITRE ATT&CK ids **only** to justify a D3FEND countermeasure.
