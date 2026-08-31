# sbom-provenance depth module 05 — logging-and-detection

> progressive disclosure · defense-only · damga: 2026-08-27T12:40:00Z

## Purpose
Deepen ASSESS-ONLY coverage for `sbom-provenance` on topic **logging-and-detection**.
Produce gap rows and evidence pointers — do **not** auto-remediate production.

## Ethics
- Refuse weaponization, exploit how-to, phishing lure templates, C2 setup.
- Prefer D3FEND-style detect / harden / isolate / recover wording.
- Secrets: `${VAR}` / `vault://` / `<REDACTED>` only.

## Operator steps
1. Read `SECURITY_STATE.md` (MODE default ASSESS-ONLY).
2. Sample related controls in family folders; note draft mapping status.
3. Record gaps in `ASSESSMENTS/` with severity + defense recommendation.
4. Stamp learning to `BILGI_TABANI.md` + `AUDIT_LOG.jsonl` when closing a pass.

## Checklist
- [ ] logging-and-detection item 5.01: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.02: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.03: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.04: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.05: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.06: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.07: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.08: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.09: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.10: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.11: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.12: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.13: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.14: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.15: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.16: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.17: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.18: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.19: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] logging-and-detection item 5.20: verify evidence exists; if missing, open gap; document owner; no offensive steps.

## Mapping hint
| Framework | Draft pin |
|---|---|
| NIST CSF 2.0 | PR.AA |
| NIST SP 800-53 Rev.5 | AC-16 |
| ISO/IEC 27001:2022 | A.8.8 |
| CIS Controls v8.1 | CIS-6 |
| OWASP ASVS 5.0.0 | V6 |

## Evidence examples (non-secret)
- Config screenshot / export path (redact tokens)
- CI job name + run id proving gate ran
- Policy markdown link under `docs/` or control id
- Ticket / CAB id for exceptions

## Negative tests (secure behavior only)
- Confirm unauthorized path is **denied** in staging (no payload crafting).
- Confirm secret scanner hooks fire on staged files.
- Confirm ethics_check.py clean on authored security content.

## Out of scope (forbidden)
Refuse: exploit how-to, credential harvest, auth bypass instructions, malware generation.

## K-003
This is one progressive module — aggregate coverage via many files, never a 900k single prompt.
