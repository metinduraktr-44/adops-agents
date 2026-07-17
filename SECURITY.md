# Security Policy

## Component security model (5 rules + 6 layers)
Every component in this repo passes: (1) official-source priority, (2) executable-script
caution, (3) no recency fallacy, (4) canonical-org-only installs, (5) marketplace-first —
enforced by a 6-layer validation: structural, integrity/SHA256 (`VERSIONS.md`),
semantic/injection, reference/SSRF, known-patterns, independent review.
Weekly SARIF audit: `.github/workflows/security-audit.yml` → Security → Code scanning (category `ajans-audit`).

## Reporting a vulnerability
Open a private security advisory (Security → Advisories → Report a vulnerability)
or email **metindurak.tr@gmail.com**. Response target: 72h. Please do not open public
issues for exploitable findings.

**TR:** Güvenlik bulgusu için private advisory ya da e-posta; kamuya açık issue açma. Yanıt hedefi 72 saat.
