# TEK SAYFA RAPOR — 2026-11-15 (Europe/Istanbul) · DEVAM ET RAPORLA
> Owner: Metin · **Onaylıyorum** merge pass + LATOS/agency continue · Kanıt: STATE / LATOS_STATE / SECURITY_STATE / AKTIVASYON-DURUM / `data/arsiv/2026-11/`
> Damga: 2026-11-15T10:08:00Z (UTC) · Yerel: 2026-11-15 13:08 +03 · **main** (post-merge)
> prev: 09:48 merge-yok rapor · Repo: https://github.com/metinduraktr-44/adops-agents

## 1) Durum + merge edilenler

| PR | Sonuç | URL |
|---|---|---|
| **#630** | **MERGED** — Continue agency OS (SEC-T003, owner upload docs, ethics FP) | https://github.com/metinduraktr-44/adops-agents/pull/630 |
| **#621** | **MERGED** — Dependabot setup-python 5→7 | https://github.com/metinduraktr-44/adops-agents/pull/621 |
| **#631** | **MERGED** — Dependabot codeql-action 4.37.9→4.39.3 | https://github.com/metinduraktr-44/adops-agents/pull/631 |
| **#629** | **MERGED** — research-loop + LATOS scaffolds + tek-sayfa + holding schema fix | https://github.com/metinduraktr-44/adops-agents/pull/629 |
| **#628** | **MERGED** — Claude Code güvenlik uyarıları (rebase `origin/main` sonrası) | https://github.com/metinduraktr-44/adops-agents/pull/628 |

`npm run validate` → **VALIDATION: GECTI** (2108). Research-loop `2026-11-15T10:02:13Z` · kuyruk **79 sourced / 2021 pending**. Registry **696 / 43 / 81**. `holding_research.py` v2.10 fix main’de. Security **ASSESS-ONLY**. Canva **BRIEF-ONLY**. Exa **needsAuth**. CONTEXT/INBOX boş. `.docx`/`.pdf` yok (in-repo extract var, byte-faithful değil).

Scaffold main’de: `SKILLS_TALENT/` (~100), `ORG/LATOS_HIERARCHY.md`, `PROMPTS/**/INDEX` (P001–P122 stubs), `CALENDAR/2026-11-monthly-loop.md`, `/cc-guvenlik` + prompt-injection guard.

**Açık PR: yok** (`gh pr list --state open` → `[]`).

## 2) Benim iş listem (Owner)

### Yapacaklarım
| İş | Yön + URL + kısa not |
|---|---|
| **Cursor restart** | New Agent chat · https://cursor.com/docs/agent/chat · skills/hooks (#628 rules) keşfi |
| **MCP Authorize** | Settings→MCP ihtiyaç kadar · https://cursor.com/docs/context/mcp · Exa needsAuth → sourced delta kapalı |
| **`.env.local` rotate** | https://openrouter.ai/settings/keys · `docs/LLM-ENV.md` · commit etme |
| **ANTHROPIC_API_KEY** | https://github.com/metinduraktr-44/adops-agents/settings/secrets/actions · yoksa LLM iskelet |
| **LATOS CONTEXT/INBOX** | `CONTEXT/CONTEXT_BRIEF.md` → `/latos-baslat` · boşken 600×200 uydurma yok |
| **#628 byte-faithful** | `.docx`/`.pdf` → `uploads/` · `docs/OWNER-UPLOAD-CLAUDE-CODE-DOCS.md` · in-repo extract yedek |
| **Domain TF apply** | vault+cluster · `infra/observability/terraform/` · creds yoksa apply yok |
| **OpCo seçimi** | chat’te tek marka · `docs/holding/gorevler/` |

### Onaylayacaklarım
| İş | Yön + URL + not |
|---|---|
| **MODE=IMPLEMENT** | Flip yapma · `SECURITY_STATE.md` · `TASKS/SEC-T003.md` |
| **Unverified uzman** | Yayın = sen · `data/title_top100_queues.json` · K-003 |
| **CANVA:ON** | OAuth bitmeden açma · `STATE.md` |
| **Auto-run/YOLO** | Kapalı tut · `docs/CLAUDE-CODE-GUVENLIK-UYGULAMA.md` · `/cc-guvenlik` |

## 3) Senin iş listen (Agent)

### Onaylılar (main)
#616 Creative OS · #617–#619 Security+LATOS · #614 live-ops · #607 HoldCo · **#630 #621 #631 #629 #628** (bugün).

### İleridekiler
- LATOS job-card: CONTEXT dolmadan örnek + `/latos-devam`
- Security ASSESS deepen; IMPLEMENT yok
- Exa Authorize → ≤5 sourced/disiplin
- Domain2 plan-only
- F5 ticari owner + makale
- holding-arastirma cron izle (şema fix sonrası)

## 4) Roadmap + adam-saat
Band **0.5 / 1 / 2 / 4 / 8 / 16** (tahmin).

| P | İş | Saat | Sahip |
|---|---|---|---|
| P0 | Cursor restart | 0.5 | Owner |
| P0 | MCP Authorize (Exa+) | 1 | Owner |
| P0 | `.env.local` rotate | 0.5 | Owner |
| P0 | LATOS CONTEXT brief | 2 | Owner |
| P0 | `.docx`/`.pdf` upload | 0.5 | Owner |
| P0 | holding_research fix | 0.5 | Agent **done** |
| P0 | merge yeşil PR’lar | 1 | Agent **done** |
| P1 | SEC MODE kriter + 20 mapping | 4 | Owner+Agent |
| P1 | IMPLEMENT | 8 | **blocked** |
| P1 | Domain2 TF | 4 | Owner creds+Agent |
| P1 | LATOS expand post-brief | 8 | Agent |
| P1 | F5 lead+vaka | 16 | Owner+Agent |
| P2 | OpCo scaffold (1) | 16 | Agent |
| P2 | Top-100 sourced deltas | 8 | Agent |
| P2 | Canva OAuth | 2 | Owner |

Owner P0 kalan: **~4.5 saat**. Agent P0 bugün: **~1.5 saat** (tamam).

## 5) Açık PR’lar
**Yok.** Kapalı: #627 (superseded).

## 6) 🚩 K-003
- 🚩 **900M karakter prompt** — refuse; prompt_bank + INDEX stubs + `/latos-devam`
- 🚩 **Uydurma top-100** — 79/2021; Exa needsAuth
- 🚩 **600×200 / 200 forecast/day** one-pass — refuse
- 🚩 live-all-skills — family stamp only
- 🚩 ASSESS-ONLY · BRIEF-ONLY · Domain apply without vault
- 🚩 `.docx`/`.pdf` uploads yok · F5 kapı geçti

## 7) Kanıt
- Merged: #630 #621 #631 #629 #628
- `validate` / `secret_scan` / `ethics_check` → GECTI
- `data/arsiv/2026-11/LOOP.json` · `docs/RAPOR-TEK-SAYFA-2026-11-15.md`
