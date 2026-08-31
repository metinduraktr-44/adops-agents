# conditional-policy-engine — Control templates

Required fields per control markdown:

| Field | Required |
|---|---|
| id | yes |
| ad | yes |
| açıklama | yes |
| NIST_CSF | yes (draft) |
| 800-53 | yes (draft) |
| ISO27001 | yes (draft) |
| CIS | yes (draft) |
| OWASP | yes (draft) |
| doğrulama_yöntemi | yes |
| savunma_gerekçesi | yes |

All mappings flagged `needs_expert_review` — not production-certified.

## Example stub
```yaml
id: LYR-001
ad: Network segmentation baseline
NIST_CSF: PR.IR
800-53: SC-7
status: draft
```
