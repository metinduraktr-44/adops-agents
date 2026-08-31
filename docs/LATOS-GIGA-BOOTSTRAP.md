# LATOS GIGA Bootstrap Runbook

> Damga: 2026-08-27 · TR: LATOS paket kurulum ve operasyon kılavuzu

## Quick start

```bash
# 1. Generate / refresh scaffold
python3 scripts/generate_latos_giga_pack.py --git-scan

# 2. Validate
python3 scripts/validate.py
python3 scripts/qa_check.py
python3 scripts/citation_check.py

# 3. Restart Cursor (skill discovery)
# 4. New Agent chat → /latos-devam
```

## Phase order

1. **Faz 0** — Bootstrap (done in-repo)
2. **Faz 1** — Title inventory 600 + git scan
3. **Faz 2** — Research stubs + MASTER_TASKS
4. **Faz 3–9** — Expand via `/latos-devam` batches

See `.cursor/plans/latos-master-plan.md` for checklist.

## CONTEXT / INBOX

Cursor cannot read old chat logs as files. Feed context via:
- `@file` / `@folder` in chat
- Drop exports into `CONTEXT/INBOX/`
- Prior docs: `CLAUDE.md`, `BILGI_TABANI.md`, `data/arsiv/`

## Git recovery (read-only first)

```bash
git rev-parse --is-inside-work-tree
git log --all --diff-filter=D --summary
git log --all --full-history -- '**/*role*' '**/*title*' '**/*agent*'
git show <commit>^:<path>          # read deleted content
# git restore --source=<commit>~1 -- <path>  # HUMAN APPROVAL REQUIRED
```

Document in `ROSTER/TITLE_INVENTORY.md`. Never `git push --force`.

## Commands (13)

| Command | Purpose |
|---|---|
| `/latos-baslat` | Start / bootstrap |
| `/latos-devam` | Continue next batch |
| `/latos-resume` | Session resume from STATE |
| `/latos-faz-raporu` | Phase QA report |
| `/latos-title-kesif` | Refresh inventory |
| `/latos-is-karti` | Expand one job card |
| `/latos-uzman-guncelle` | Expert queue update |
| `/latos-yetenek-guncelle` | Talent taxonomy |
| `/latos-roadmap` | OKR / roadmap |
| `/latos-prompt-uret` | Prompt batch |
| `/latos-tahmin` | Daily forecasts |
| `/latos-aylik-dongu` | Monthly loop |
| `/latos-arsivle` | Archive snapshot |

## Hooks (coexist security)

`.cursor/hooks.json` merges:
- Security: secret_scan, ethics_check, block-dangerous, redact-secrets
- LATOS: qa_check (JOB_CARDS), citation_check (EXPERTS/RESEARCH/FORECASTS)
- Stop: phase-audit.sh + phase-audit-latos.sh

Verify: Cmd+Shift+P → Hooks output channel after restart.

## K-003 compliance

- No literal 900M-char prompt file
- No invented top-100 expert lists
- 600 titles inventoried; cards expand progressively
- 200 forecasts/day = workflow template, not bulk invention

## Owner next steps

1. **Restart Cursor** after this PR merge
2. Put any prior chat exports in `CONTEXT/INBOX/`
3. Run `/latos-devam` for Faz 2+ expansion
4. Human-review all `unverified` / `pending_research` slots before publish
5. Security pack: keep `MODE=ASSESS-ONLY` until explicit owner flip

## Related docs

- Master prompt: `docs/CURSOR-LATOS-GIGA-MASTER-PROMPT.md`
- State: `LATOS_STATE.md`
- Skill map: `ORG/SKILL_MATRIX.md`
- Activation: `docs/AKTIVASYON-DURUM.md`
