# prompt-engine — Workflow

1. Read `LATOS_STATE.md` + `ROSTER/TITLE_INVENTORY.md`
2. Execute phase steps from master prompt
3. Write outputs to canonical paths (see `30-latos-file-structure.mdc`)
4. Run `python3 scripts/qa_check.py` + `citation_check.py`
5. Append AUDIT_LOG.jsonl + BILGI_TABANI.md
6. Stop; owner types `/latos-devam` or `/devam`

Damga: 2026-08-27T20:16:49Z
