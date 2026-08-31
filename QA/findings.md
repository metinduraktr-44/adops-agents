# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# QA — Security Findings (skeleton)

Türkçe not: Güvenlik-yönetişim OS için QA bulguları. Yaratıcı-ajans `QA/QA_REPORT.md`'den ayrı, additive. `/etik-denetim` ve `security-qa` skill buraya yazar.

## Audit log format
`YYYY-MM-DD | check | verdict (PASS/PARTIAL/FAIL) | REDACTED pointer | remediation`

## Checks tracked
- defense-only (no offense/exploit/weaponization)
- secret hygiene (no plaintext/realistic secrets; only `${VAR}`/`vault://`/`op://`/`<REDACTED>`)
- standard-mapping completeness + verify-banner present
- no fabricated facts/URLs

## Entries
- _(none yet — `/etik-denetim` appends dated verdicts. Never echo a secret value; reference `QA/secret-scan.log` / `QA/ethics-check.log` which are gitignored `*.log`.)_
