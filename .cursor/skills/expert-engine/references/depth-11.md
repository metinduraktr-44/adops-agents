# expert-engine depth module 11 — cloud-posture-baselines

> progressive disclosure · defense-only · damga: 2026-08-27T12:59:19Z

## Purpose
Deepen ASSESS-ONLY coverage for `expert-engine` on topic **cloud-posture-baselines**.
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
- [ ] cloud-posture-baselines item 11.01: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.02: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.03: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.04: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.05: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.06: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.07: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.08: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.09: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.10: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.11: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.12: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.13: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.14: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.15: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.16: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.17: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.18: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.19: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.20: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.21: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.22: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.23: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.24: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.25: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.26: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.27: verify evidence exists; if missing, open gap; document owner; no offensive steps.
- [ ] cloud-posture-baselines item 11.28: verify evidence exists; if missing, open gap; document owner; no offensive steps.

## Mapping hint
| Framework | Draft pin |
|---|---|
| NIST CSF 2.0 | RS.MA |
| NIST SP 800-53 Rev.5 | SC-10 |
| ISO/IEC 27001:2022 | A.8.25 |
| CIS Controls v8.1 | CIS-12 |
| OWASP ASVS 5.0.0 | V12 |

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

## Scenario notes (cloud-posture-baselines)
For AdOps Agents (markdown/Python component pack + GitHub Actions):
- Map `cloud-posture-baselines` to repo surfaces: `.github/workflows/`, `scripts/`, `.cursor/`, `data/`.
- Holding OpCos inherit shared controls; country LLM agencies need privacy overlays.
- Canva/creative GIGA files coexist — do not delete; security uses `SECURITY_STATE.md`.
- MCP security catalog stays **off** until owner Authorize with `${VAR}` only.

## Review flags
- status: draft · needs_expert_review
- MODE: ASSESS-ONLY unless owner flips `SECURITY_STATE.md`
