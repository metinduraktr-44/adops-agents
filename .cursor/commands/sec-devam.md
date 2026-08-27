---
name: sec-devam
description: Continue the Security Governance OS from the first unchecked item in the security master plan.
---

# /sec-devam (DEVAM — Security)

## Objective
Resume security work from the current phase without restarting completed phases.

## Requirements
- Read `SECURITY_STATE.md` (source of truth), then `.cursor/plans/security-master-plan.md`.
- Continue from the first unchecked `- [ ]` item in the current phase.
- Keep `MODE=ASSESS-ONLY`; defense-only; no secrets/accounts/network.
- Write outputs to the phase's Bölüm 12 folder; append/version, never overwrite.

## Output
- Advanced plan items + artifacts in their folders.
- Updated `SECURITY_STATE.md`.
- Status line: phase, MODE, next action.
