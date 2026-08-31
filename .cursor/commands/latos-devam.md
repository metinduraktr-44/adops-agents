---
description: Continue LATOS next phase batch — read STATE, execute, stop ≤10 lines.
---
# /latos-devam (alias /devam)

1. Read `LATOS_STATE.md` — note current faz + next task from `TASKS/MASTER_TASKS.md`
2. Execute next batch (job cards, experts, prompts, forecasts)
3. Run `python3 scripts/qa_check.py` + `citation_check.py`
4. Update `LATOS_STATE.md` + append AUDIT_LOG
5. Report ≤10 lines; wait for next `/latos-devam`
