# Secret Hygiene — Outline (skeleton)

GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok. Standard values: verify against official source before production.

## Checks
- Repo scan for key/token/credential patterns
- Sensitive filenames (.env, *.pem, *.key, id_rsa, credentials)
- CI/CD secret injection review
- Rotation guidance on exposure

## Rule
- Backs `.cursor/rules/10-secret-hygiene.mdc`.

## TODO (phased)
- [ ] Expand to full content in phased runs.
- [ ] Verify every standard id/version against official docs.
