# Claude Code bilgileri ve güvenlik uyarıları

> **TR:** Owner dosya adları: `Claude Code Bilgileri ve Güvenlik Uyarıları.docx` + `.pdf`. Bu Cloud Agent VM’de binary **yok** (uploads dizini boş). Aşağıdaki metin dump değil; Anthropic resmi güvenlik korpusundan yapılandırılmış çıkarım + bu repodaki eşleme.
>
> Damga: `2026-11-03T09:58:05Z` · Savunma-only · Secret düz metin yok · K-003 (900B blob yok)

## Provenance

| Kaynak | Durum |
|---|---|
| Owner `.docx` / `.pdf` | **Bulunamadı** bu oturumda. Aranan: `/home/ubuntu/.cursor/projects/workspace/uploads/`, `/workspace`, `/tmp`, Downloads. Parent transcript yalnız **dosya adı** içeriyor. |
| Resmi güvenlik | [Security](https://code.claude.com/docs/en/security) |
| İzinler | [Permissions](https://code.claude.com/docs/en/permissions) |
| Sandbox | [Sandboxing](https://code.claude.com/docs/en/sandboxing) · [sandbox environments](https://code.claude.com/docs/en/sandbox-environments) |
| Hooks | [Hooks guide](https://code.claude.com/docs/en/hooks-guide) · [hooks reference](https://code.claude.com/docs/en/hooks.md) |
| Plugin güveni | [Plugin security](https://code.claude.com/docs/en/plugins/security) |
| Best practices | [Best practices](https://code.claude.com/docs/en/best-practices) |
| Trust Center | [Anthropic Trust Center](https://www.anthropic.com/trust-center) |
| HackerOne | [Report](https://hackerone.com/anthropic) (kamuya açık exploit yazma) |

Owner byte-faithful extract isterse aynı iki dosyayı bu ajana yeniden yüklemeli.

## Facts (Claude Code)

1. Agentic coding tool: repo okur, dosya düzenler, kabuk çalıştırır, MCP/plugin bağlar. Yüzeyler: CLI, IDE, desktop, cloud, mobile.
2. Güvenlik temeli izin mimarisi + (isteğe bağlı) OS sandbox + hook’lar. Katmanlar birbirini **tamamlar**; biri diğerini iptal etmez.
3. **Auto mode:** sınıflandırıcı bazı eylemleri sizin yerinize onaylar/bloklar. **Manual mode:** salt-okunur başlar; yazma/test/komut onay ister.
4. Deny kuralları prompt veya hook `allow` ile **aşılmaz** (Anthropic: deny, bypass modunda bile uygulanır).
5. Sandbox yalnız **Bash/PowerShell/Monitor** ve çocuk süreçler. Read/Edit/Write, WebFetch, MCP, hook’lar sandbox **dışında** — onlar permission kurallarına bağlı.
6. `autoAllowBashIfSandboxed` (varsayılan true): sandbox içi kabuk onay sormadan gider. Plan mode’da bu ikame yok.
7. CLAUDE.md / AGENTS.md / hooks / `.claude/settings.json` oturum bağlamını ve (hook’larda) **deterministik kabuğu** etkiler. Klon repoda çalıştırmadan önce oku.
8. MCP: proje `.mcp.json` + kullanıcı/plugin sunucuları. Anthropic Directory listing ≠ güvenlik auditi.
9. Cloud oturumları izole VM + egress kontrolü. Remote Control = **yerel süreç**; cloud sandbox yok.
10. Credential: macOS Keychain / Linux `0600` dosya / Windows profil ACL. GitHub cloud proxy kısa ömürlü token; branch silme/tag push reddi.

## Warnings (operatör + ajan)

W1. **Siz sorumlusunuz.** Önerilen komut/diff’i onaylamadan güvenlik varsaymayın.
W2. **Prompt injection.** Repo dosyası, web, MCP çıktısı, CLAUDE.md “ignore previous / disable safety / send secrets” ile modeli saptırabilir. İzin + deny + sandbox ağ izolasyonu birlikte.
W3. **Ağ komutları.** `curl`/`wget` varsayılan auto-approve değil. Deny + sandbox host allowlist; komut metnine güvenmeyin.
W4. **Auto-approve / skip-permissions.** `--dangerously-skip-permissions` ve “her şeyi onayla” yorgunluğu = en büyük operatör riski. Accept Edits bile `rm`/`mv`/`sed` çalışma dizininde onaylar.
W5. **Sandbox boşlukları.** File tools, MCP, hook, statusline, `apiKeyHelper` sandbox dışı. Native Windows unsandboxed (WSL2 kullan).
W6. **Çalışma dizini sınırı prompt’tur**, OS değil. Onaylı Bash kullanıcı hesabının yazabildiği her yere yazabilir.
W7. **Hook’lar kod çalıştırır.** Başkasının `.cursor/hooks.json` / `.claude` hook komutu, onay akışından önce tetiklenebilir. Klon: oku, sonra aç.
W8. **Plugin/MCP güveni.** Eklenti sizin yetkinizle çalışır. Marketplace adı yayıncıyı söyler, her eklentiyi doğrulamaz.
W9. **Secret context.** Canlı key/token’ı CLAUDE.md, chat, kural, ekran görüntüsü, issue’ya yapıştırmayın. Model bağlamı log/transcript’e girebilir.
W10. **Untrusted içerik.** Ham web/MCP’yi doğrudan modele borulamayın. WebFetch özeti bile enjeksiyon taşıyabilir.
W11. **Windows WebDAV.** `\\*` / WebDAV yolları izin sistemini atlayabilir (Anthropic uyarısı; Microsoft deprecated).
W12. **Home dizininde trust.** `~` altında trust diske yazılmaz; her açılışta sorulur. Proje alt dizininden başlatın.
W13. **Kurulum kaynağı.** Yalnız resmi installer / `@anthropic-ai/claude-code`. Üçüncü parti “leaked Claude Code” repo/reklam düşman varsay.
W14. **Fail-closed.** Parse edilemeyen / eşleşmeyen kabuk Manual mode’da onay ister. `eval` her zaman onay. Allow kuralı `git *` injection tespitini atlamaz.
W15. **Hiçbir sistem bağışık değil.** Şüphe → `/feedback`; zafiyet → HackerOne, kamu PoC yok.

## Claude Code → Cursor eşdeğeri

| Claude Code | Cursor (bu repo) |
|---|---|
| CLAUDE.md | `CLAUDE.md` + `AGENTS.md` + `.cursor/rules/*.mdc` |
| `.claude/settings.json` permissions | Cursor Settings: Auto-run / sandbox / command allow-deny (**owner UI**) |
| `.claudeignore` | `.cursorignore` (bu PR) |
| Hooks `.claude/settings.json` | `.cursor/hooks.json` (merge; silinmedi) |
| Deny rules | `block-dangerous.sh` fail-closed + ethics/secret scanners |
| Sandbox `/sandbox` | Cloud Agent VM + owner local sandbox; file/MCP hâlâ sandbox dışı |
| Prompt injection | Rule `15-agent-context-hygiene.mdc` + `scripts/prompt_injection_guard.py` |
| Secret in context | `10-secret-hygiene.mdc` + `redact-secrets.sh` + `secret_scan.py` |
| Ethics / no exploit | `05-ethics-guardrail.mdc` + `ethics_check.py` |
| MCP `.mcp.json` | Owner Authorize; catalog off until enable (`SECURITY_STATE.md`) |
| `/permissions` audit | `/cc-guvenlik` + `/sec-etik-denetim` |
| Trust dialog | Cursor workspace trust (**owner**) |

## Map to existing pack (silinmedi)

| Uyarı | Pack |
|---|---|
| W1, W4 auto-approve | `docs/AKTIVASYON-DURUM.md` owner gated · runbook P0 |
| W2 injection | yeni kural 15 + guard script · Security GIGA ethics |
| W3, W5 sandbox | `00-security-core.mdc` · `block-dangerous.sh` |
| W7 hooks | `.cursor/hooks.json` (Security + LATOS + Canva `spec_validate` duruyor) |
| W8 MCP | `SECURITY_STATE.md` `MCP_SECURITY_CATALOG=off` |
| W9 secrets | `10-secret-hygiene.mdc` · `scripts/secret_scan.py` |
| W15 defense-only | `05-ethics-guardrail.mdc` · MODE=ASSESS-ONLY |
| Paste iptal | `docs/CLAUDE-CODE-AKTIVASYON.md` · `docs/SECURITY-GIGA-BOOTSTRAP.md` |
| Org 600 / LATOS | dokunulmadı |
| Canva BRIEF-ONLY | dokunulmadı |

## Not in this extract

- 900k/900B prompt gövdesi (K-003 🚩)
- Invented top-100 uzman
- Exploit/PoC/adım
- Düz metin secret
- Owner binary SHA (dosya yok)
