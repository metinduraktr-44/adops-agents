# SECURITY GIGA Bootstrap — Runbook + K-003

> TR kısa not · Damga: 2026-08-27T12:40:00Z

## Paste iptal — in-repo apply

Claude Code'a security master prompt **yapıştırılmaz**. Bu bootstrap repoda uygulandı:

- Ana referans: `docs/CURSOR-SECURITY-GIGA-MASTER-PROMPT.md`
- Kanıt: `SECURITY_STATE.md` Faz 0 = DONE · `MODE=ASSESS-ONLY`
- Yeniden üret: `python3 scripts/generate_security_giga_pack.py`
- Skill refs expand (~900k aggregate): `python3 scripts/generate_security_giga_pack.py --expand-refs`
- Gate: `python3 scripts/validate.py`

## Hızlı başlangıç

```bash
cat SECURITY_STATE.md
cat docs/CURSOR-SECURITY-GIGA-MASTER-PROMPT.md | head -80

# Cursor commands (sec-* — Canva /baslat ile çakışmaz)
# /sec-baslat  /sec-gap-analizi  /sec-etik-denetim

python3 scripts/secret_scan.py .
python3 scripts/ethics_check.py .
python3 scripts/validate.py
```

## MODE order

| Sıra | MODE | Ne zaman |
|---|---|---|
| 1 | **ASSESS-ONLY** | Varsayılan — gap, inventory, draft controls |
| 2 | **IMPLEMENT** | Owner `SECURITY_STATE.md` flip sonrası |
| 3 | **AUDIT** | Evidence + COMPLIANCE/ paketi |

ASSESS bitmeden IMPLEMENT yok.

## Restart / Authorize checklist (P0)

1. [ ] Cursor **restart** (yeni skills/rules/hooks)
2. [ ] Security MCP catalog entries — default **off**; enable only with `${VAR}` env
3. [ ] Confirm `MODE=ASSESS-ONLY` before any remediation
4. [ ] Run `/sec-etik-denetim` on generated packs

## K-003 eşlemesi

| Sahip talebi | 🚩 | Bu pakette |
|---|---|---|
| 900k char tek prompt | imkânsız | dense master + skills `references/` + generator |
| Her title top-100 kişi | uydurma | `EXPERTS/*/seed.json` + `pending_research.json` |
| Exploit/PoC | ethics | defense-only · ethics_check.py |
| Secret in repo | sızıntı | `${VAR}` / vault / REDACTED + secret_scan.py |

## Canva co-existence

Creative GIGA (`STATE.md`, Canva MCP) ile **yan yana**. Security için `SECURITY_STATE.md`. `STATE.md` varsa security pointer eklenir; yoksa bu dosya yeterli.

## İlgili dosyalar

- Rules: `.cursor/rules/00-security-core.mdc` … `40-secops.mdc`
- Commands: `.cursor/commands/sec-*.md`
- Plan: `.cursor/plans/security-master-plan.md`
- Hooks: `.cursor/hooks.json` + `.cursor/hooks/*.sh`
- Scanners: `tools/security-scanners/`, `scripts/secret_scan.py`, `scripts/ethics_check.py`
