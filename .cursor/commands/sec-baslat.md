---
name: sec-baslat
description: Cold-start the Security Governance OS from Faz 0 of the security master plan (MODE=ASSESS-ONLY).
---

# /sec-baslat (BAŞLAT — Security)

## Objective
Cold-start the Security Governance OS from `Faz 0` and drive the phase plan forward in `MODE=ASSESS-ONLY` unless told otherwise.

## Requirements
- Read `.cursor/plans/security-master-plan.md` and `SECURITY_STATE.md`.
- If `SECURITY_STATE.md` shows a phase past Faz 0, confirm the owner wants a fresh start before resetting.
- Honor `MODE=ASSESS-ONLY` (assess/model/map/document; no live changes, no network, no secrets). MCP servers stay OFF unless the owner enabled them in Settings.
- Ensure Bölüm 12 security folders exist; create missing skeleton files, never overwrite.
- Defense-only: refuse offensive/exploit work; redact secrets to `<REDACTED>`.

## Output
- Updated `SECURITY_STATE.md` (phase, MODE, timestamp).
- First-phase artifacts written to their Bölüm 12 folders (`SECURITY_CONTEXT/`, …).
- Short status line: current phase, MODE, next action.
