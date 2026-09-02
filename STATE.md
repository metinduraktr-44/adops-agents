# STATE — Creative Agency OS

Türkçe not: `DEVAM`/`RESUME` bu dosyayı okur. Kaynak-doğruluk (source of truth) burasıdır.

| Field | Value |
|---|---|
| current_phase | Faz 0 — Bootstrap & Context |
| canva_mode | CANVA:BRIEF-ONLY |
| last_completed_phase | (none) |
| last_update | 2026-08-27T00:00:00Z (scaffold init) |
| oauth_status | not started (user action) |

## Flags
- `CANVA:BRIEF-ONLY` = true (dry-run; no Canva API calls, no secrets, no network side-effects)
- `CANVA:ON` = false (enable only after the user completes Canva OAuth)

## Resume notes
- Scaffold committed. Next action: fill `CONTEXT/CONTEXT_BRIEF.md` (Faz 0), then advance
  `.cursor/plans/master-plan.md` in order.
- Do NOT enable `CANVA:ON` autonomously. Do NOT run always-on/live loops.

## Security GIGA state (separate)
Security mode and phases live in **`SECURITY_STATE.md`** (default `MODE=ASSESS-ONLY`).
Do not overwrite security MODE here.

| Pack | State file |
|---|---|
| Security GIGA | `SECURITY_STATE.md` |
| Creative Canva GIGA | `STATE.md` (this file) |
