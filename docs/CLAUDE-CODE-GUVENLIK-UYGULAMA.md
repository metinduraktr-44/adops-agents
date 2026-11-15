# Claude Code güvenlik — uygulama runbook

> **TR:** Ne uygulandı (in-repo) vs owner-gated. Paste Claude Code’a **İPTAL**.
> Damga: `2026-11-03T09:58:05Z`

## Applied (this PR)

| Madde | Dosya |
|---|---|
| Structured extract | `docs/CLAUDE-CODE-BILGILERI-VE-GUVENLIK-UYARILARI.md` |
| Context hygiene rule | `.cursor/rules/15-agent-context-hygiene.mdc` |
| Slash command | `.cursor/commands/cc-guvenlik.md` → `/cc-guvenlik` |
| Injection heuristic (defense) | `scripts/prompt_injection_guard.py` |
| Hooks merge | `.cursor/hooks.json` — `afterFileEdit` + `beforeSubmitPrompt` guard; **LATOS/Canva/Security hook’lar duruyor** |
| Dangerous shell | `.cursor/hooks/block-dangerous.sh` — skip-permissions + 777 `/` |
| Ignore (Cursor ≈ `.claudeignore`) | `.cursorignore` |
| Ethics / secret pointers | `05-ethics-guardrail.mdc`, `10-secret-hygiene.mdc` (ek satır; overwrite yok) |
| Agent map | `AGENTS.md` kısa bölüm |

`validate.py` + `secret_scan.py` + `ethics_check.py` + `prompt_injection_guard.py` yeşil hedef.

## Owner-gated P0 (Metin)

Binary’ler bu VM’e **binmedi**. Aşağısı insan/UI; ajan yazamaz.

1. **Dosyayı yeniden yükle** (byte-faithful): `Claude Code Bilgileri ve Güvenlik Uyarıları.docx` + `.pdf` → Cloud Agent chat. Sonra extract güncellenir.
2. **Cursor restart** — yeni `.mdc` / command / hook keşfi.
3. **Auto-run / YOLO kapalı tut** veya dar allowlist. Claude `--dangerously-skip-permissions` eşdeğeri. Settings → Agent / Auto-run.
4. **Sandbox:** local’de OS sandbox açık; ağ allowlist dar. File tools sandbox dışı olduğunu unutma. [Sandboxing](https://code.claude.com/docs/en/sandboxing)
5. **MCP Authorize yalnız ihtiyaç:** Canva/Semgrep/Exa/… — `SECURITY_STATE.md` catalog **off** kalır ta ki sen açana. Token `${VAR}` / OS keychain.
6. **Workspace trust** — tanımadığın klasörü “trust all” yapma. Home dizininden agent başlatma.
7. **Klon repo:** `.cursor/hooks.json`, `.cursor/mcp.json`, `CLAUDE.md`, `AGENTS.md` oku **sonra** Agent.
8. **Secret:** chat/kural/issue’ya yapıştırma. Rotation: vault. Tarama: `python3 scripts/secret_scan.py .`
9. **Kurulum kaynağı:** resmi Cursor + resmi Claude Code. Üçüncü parti installer yok.
10. **Zafiyet bildir:** [SECURITY.md](../SECURITY.md) · Claude Code: [HackerOne](https://hackerone.com/anthropic) · kamu PoC yok.
11. **Security GIGA** MODE=ASSESS-ONLY bırak (`/sec-baslat`). IMPLEMENT senin kriterin.
12. **Hooks kanalı:** Command Palette → Hooks output. `secret_scan` / `ethics_check` / `prompt_injection_guard` görünmeli.

## Commands

```bash
python3 scripts/prompt_injection_guard.py
python3 scripts/secret_scan.py .
python3 scripts/ethics_check.py .
python3 scripts/validate.py
```

Cursor: `/cc-guvenlik` · `/sec-etik-denetim`

## URLs (owner)

- https://code.claude.com/docs/en/security
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/sandboxing
- https://code.claude.com/docs/en/hooks-guide
- https://code.claude.com/docs/en/plugins/security
- https://www.anthropic.com/trust-center
- https://www.anthropic.com/research/claude-code-sandboxing
