# CALENDAR — Security monthly loop

> HAND_AUTHORED · damga: 2026-08-27T12:55:00Z · MODE=ASSESS-ONLY

## Rhythm
| Cadence | Command / script | Output |
|---|---|---|
| Daily | Agency `daily_ops` (existing) | Standup — security note optional |
| Weekly | `.github/workflows/security-audit.yml` | validate + SARIF |
| Monthly | `/sec-aylik-dongu` | Expert queue refresh + research note |
| On demand | `/sec-devam` | Advance incomplete ASSESS phases |

## Monthly loop stub (checklist)
1. [ ] Read `SECURITY_STATE.md` — confirm MODE
2. [ ] Append timestamped note under `SECURITY_RESEARCH/`
3. [ ] Review `EXPERTS/*/pending_research.json` — fill **only** when sourced URL exists
4. [ ] Sample 10 control mappings for expert review flags
5. [ ] Refresh inventory if repo surfaces changed
6. [ ] Run `secret_scan.py` + `ethics_check.py` + `validate.py`
7. [ ] Stamp `AUDIT_LOG.jsonl` + `BILGI_TABANI.md`

## Next scheduled marker
- Target: first monthly pass after owner Cursor restart + PR merge decision
- Command: `/sec-aylik-dongu`
