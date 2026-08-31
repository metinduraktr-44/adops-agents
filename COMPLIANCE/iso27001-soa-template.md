# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# ISO/IEC 27001:2022 — Statement of Applicability (SoA) template (stub)

Türkçe not: SoA şablonu. Annex A kontrolleri (93 kontrol, 4 tema) buradan doldurulur. Gerçek değerler resmi standarttan doğrulanmalı.

> ⚠️ **Verify against the official ISO/IEC 27001:2022 standard before production.** Annex A 2022 = 93 controls across 4 themes: Organizational (A.5), People (A.6), Physical (A.7), Technological (A.8).

## SoA table (fill per control)
| annex_ref | control adı | uygulanabilir? (E/H) | gerekçe (justification) | durum (planlı/uygulandı/kısmi) | delil işaretçisi (evidence pointer) | ilgili iç kontrol (LAY/FW/ENC/…) |
|---|---|---|---|---|---|---|
| A.5.1 | Policies for information security | E | (template) yönetişim gereği | planlı | araştırılacak | — |
| A.8.20 | Networks security | E | (template) segmentasyon | planlı | LAYERS/README.md · FW-001 | LAY-001, FW-001 |
| A.8.24 | Use of cryptography | E | (template) veri koruma | planlı | ENCRYPTION/README.md | ENC-001, ENC-002 |

`(template)` rows are examples — replace with real, verified entries. No secrets in evidence pointers.

## Notes
- Applicability decisions and justifications must be reviewed by GRC before certification.
- Evidence pointers reference repo artifacts or external systems by name only — never inline credentials.
