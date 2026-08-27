# security-qa depth module 06 — incident-readiness

> progressive disclosure · defense-only · damga: 2026-08-27T12:59:19Z

## Purpose
Deepen ASSESS-ONLY coverage for `security-qa` on topic **incident-readiness**.
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
- [ ] incident-readiness item 6.01: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.02: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.03: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.04: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.05: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.06: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.07: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.08: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.09: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.10: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.11: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.12: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.13: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.14: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.15: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.16: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.17: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.18: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.19: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.20: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.21: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.22: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.23: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.24: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.25: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.26: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.27: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] incident-readiness item 6.28: verify evidence exists; if missing, open gap; document owner; no offensive steps.

## Mapping hint
| Framework | Draft pin |
|---|---|
| NIST CSF 2.0 | PR.DS |
| NIST SP 800-53 Rev.5 | AC-19 |
| ISO/IEC 27001:2022 | A.8.9 |
| CIS Controls v8.1 | CIS-7 |
| OWASP ASVS 5.0.0 | V7 |

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

## Scenario notes (incident-readiness)
For AdOps Agents (markdown/Python component pack + GitHub Actions):
- Map `incident-readiness` to repo surfaces: `.github/workflows/`, `scripts/`, `.cursor/`, `data/`.
- Holding OpCos inherit shared controls; country LLM agencies need privacy overlays.
- Canva/creative GIGA files coexist — do not delete; security uses `SECURITY_STATE.md`.
- MCP security catalog stays **off** until owner Authorize with `${VAR}` only.

## Review flags
- status: draft · needs_expert_review
- MODE: ASSESS-ONLY unless owner flips `SECURITY_STATE.md`
