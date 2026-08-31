# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# CONDITIONAL — Conditional Access & Policy-as-Code (100-control framework)

Türkçe not: Koşullu erişim, risk-tabanlı authZ, zero-trust 100-kontrol çerçevesi. Additive; MODE=ASSESS-ONLY.

> ⚠️ Standard values reproduced for scaffolding — **verify against official source before production**.

## Scope
- Conditional / risk-based access
- Context signals (device/location/posture)
- Policy-as-code (OPA/Rego)
- Continuous verification (ZT, 800-207)
- Step-up authentication

## Control row schema (mandatory — see `.cursor/rules/20-control-mapping.mdc`)
Each of the 100 controls MUST carry all fields below. CIS/OWASP where applicable.

| id | ad | NIST_CSF (2.0) | 800-53 Rev.5 | ISO27001:2022 | CIS v8.1 | OWASP ASVS 5.0.0 | doğrulama_yöntemi | savunma_gerekçesi |
|---|---|---|---|---|---|---|---|---|
| CND-001 | Device-posture gate | PR.AA* | AC-3* | A.8.5* | CIS 6* | — | policy test cases | blocks non-compliant devices |
| CND-002 | Risk-based step-up MFA | PR.AA* | IA-2* | A.8.5* | CIS 6* | ASVS V2 | auth event review | mitigates credential misuse |

`*` = verify id/version against official docs. Rows above are **TEMPLATE examples**, not the final set.

## Note
Do NOT enumerate all 100 controls here in scaffold. Generate in batches via `/kontrol-uret`; keep the stable header. Full content is produced in phased runs. Detections may cite MITRE ATT&CK ids **only** to justify a D3FEND countermeasure.
