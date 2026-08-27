# change-protocol-engine depth module 03 — identity-and-least-privilege

> progressive disclosure · defense-only · damga: 2026-08-27T12:40:00Z

## Purpose
Deepen ASSESS-ONLY coverage for `change-protocol-engine` on topic **identity-and-least-privilege**.
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
- [ ] identity-and-least-privilege item 3.01: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.02: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.03: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.04: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.05: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.06: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.07: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.08: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.09: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.10: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.11: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.12: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.13: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.14: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.15: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.16: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.17: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.18: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.19: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] identity-and-least-privilege item 3.20: verify evidence exists; if missing, open gap; document owner; no offensive steps.

## Mapping hint
| Framework | Draft pin |
|---|---|
| NIST CSF 2.0 | ID.AM |
| NIST SP 800-53 Rev.5 | AC-10 |
| ISO/IEC 27001:2022 | A.8.2 |
| CIS Controls v8.1 | CIS-4 |
| OWASP ASVS 5.0.0 | V4 |

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
