# GIGA Agency Bootstrap — Kullanım + K-003 Eşlemesi

> TR kısa not · Damga: 2026-08-27T00:35:00Z

## Paste iptal — in-repo apply

Claude Code'a master prompt **yapıştırılmaz**. Bu bootstrap repoda uygulandı:
- Ana referans: `docs/CURSOR-GIGA-MASTER-PROMPT.md`
- Kanıt: `STATE.md` faz 0 = DONE
- Yeniden doğrula: `python3 scripts/validate.py && python3 scripts/spec_validate.py`

## Hızlı başlangıç

```bash
# 1. STATE oku
cat STATE.md

# 2. Brief-only modda brief üret
# Cursor: /brief-uret

# 3. Spec doğrula
python3 scripts/spec_validate.py MATRIX/

# 4. Gate
python3 scripts/validate.py
```

## K-003 eşlemesi

| Sahip talebi | 🚩 | Bu pakette |
|---|---|---|
| 900B char tek prompt | imkânsız | `docs/CURSOR-GIGA-MASTER-PROMPT.md` + phased files |
| Her title top-100 kişi | uydurma | `EXPERTS/{title}/seed.json` + `pending_research.json` |
| Canva autofill herkese | Enterprise-only | `canva-autofill` skill + doc notu |
| OAuth repoda | secret risk | `.cursor/mcp.json` URL only; owner Authorize |
| Tüm skill live | ölçek | `agency-workflow` + family router |

## Canva Dual-Mode

| Mod | Ne zaman |
|---|---|
| `BRIEF-ONLY` | Varsayılan — brief, matrix, manifest |
| `FULL` | OAuth sonrası — Canva MCP create/export |

**Autofill:** Canva Enterprise plan gerektirir; BRIEF-ONLY modda autofill çağrılmaz.

## Owner checklist (P0)

1. [ ] Cursor → MCP → Canva → Authorize (OAuth)
2. [ ] Cursor restart
3. [ ] `CANVA_MODE=BRIEF-ONLY` ile `/brief-uret` + `/spec-dogrula` dene
4. [ ] FULL moda geçmeden brand kit onayı

## İlgili dosyalar

- Rules: `.cursor/rules/00-agency-core.mdc` … `40-canva-ops.mdc`
- Plan: `.cursor/plans/master-plan.md`
- MCP: `.cursor/mcp.json`
