# 7/24 Workflows

> Damga: 2026-11-15T10:02:04Z · scaffold · Cloud Agent + cron · no always-on without owner

## Rhythm
| Cadence | Script / command | Output |
|---|---|---|
| Daily | `scripts/daily_ops.py` | `gundem/`, `makaleler/`, `IS_LISTESI.md` |
| Nightly | `scripts/nightly.sh` | AUDIT + distill |
| Nightly holding | `scripts/nightly_holding_research.py` | `data/arsiv/holding/*/snapshot-*.json` |
| Holding research | `scripts/holding_research.py` | `arsiv/holding/YYYY-MM-DD.md` |
| Mid-cycle research | `scripts/research_loop_continue.py` | `data/arsiv/YYYY-MM/LOOP.json` |
| Monthly | `scripts/monthly_research_refresh.py` | archive + queues |
| Weekly board | `scripts/weekly_board.py [--board]` | `toplantilar/` |
| LATOS expand | `/latos-devam` | JOB_CARDS / PROMPTS / FORECASTS progressive |
| Security | `/sec-devam` ASSESS-ONLY | SECURITY_* |

## On-call principles
- Signal over length; stamp AUDIT_LOG + BILGI_TABANI
- K-003: no 900M prompts; no invented people; family mini-agency not live-all-skills
- Secrets: `${VAR}` / vault / `<REDACTED>` only
- Canva default BRIEF-ONLY; Security MODE=ASSESS-ONLY

## Gaps
- Owner CONTEXT/INBOX empty → LATOS job-card stay sample
- Exa/web MCP auth optional for sourced expert deltas
- Domain TF apply blocked without vault+cluster
