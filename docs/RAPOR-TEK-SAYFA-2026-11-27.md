# TEK SAYFA RAPOR — 2026-11-27 (Europe/Istanbul) · DEVAM ET RAPORLA
> Owner: Metin · **Onaylıyorum** + mega LATOS/skill dump (K-003 eşdeğer) · Repo: https://github.com/metinduraktr-44/adops-agents
> Damga: 2026-11-27T10:20:00Z (UTC) · Yerel: 2026-11-27 13:20 +03
> prev: `docs/RAPOR-TEK-SAYFA-2026-11-15.md` · `docs/RAPOR-TEK-SAYFA-2026-11-15C.md`

## 1) Durum + merge
| PR | Sonuç | URL |
|---|---|---|
| **#635** | **MERGED** — Dependabot codeql-action 4.39.3→4.39.4 | https://github.com/metinduraktr-44/adops-agents/pull/635 |
| **#633** | **CLOSED** — CONFLICTING superseded (16 Kas rapor) | https://github.com/metinduraktr-44/adops-agents/pull/633 |
| **#634** | **CLOSED** — CONFLICTING superseded | https://github.com/metinduraktr-44/adops-agents/pull/634 |

Bu tur: archive-first `research_loop_continue.py` · registry **696 / 43 / 81** · kuyruk **79 sourced / 2021 pending** · Security **ASSESS-ONLY** · Canva **BRIEF-ONLY** · Vercel **NOT linked**.

🚩 all-skills live / 900M prompt / uydurma top-100 → **yapılmadı** (family stamp + INDEX stubs).

## 2) Benim iş listem (Owner)

### Yapacaklarım
| İş | Yön + URL + kısa not |
|---|---|
| **Cursor restart** | New Agent chat · https://cursor.com/docs/agent/chat · LATOS/Security/CC rules+skills keşfi |
| **MCP Authorize** | Settings→MCP yalnız ihtiyaç · https://cursor.com/docs/context/mcp · Exa needsAuth → sourced delta kapalı; hepsini açma |
| **`vercel link`** | Proje kökünde `vercel link` sonra `/status` · https://vercel.com/docs/cli/project-linking · `.vercel/project.json` yok → Doctor STOP |
| **`.env.local` rotate** | https://openrouter.ai/settings/keys · `docs/LLM-ENV.md` · commit etme; leak riski |
| **ANTHROPIC_API_KEY** | https://github.com/metinduraktr-44/adops-agents/settings/secrets/actions · yoksa LLM iskelet |
| **LATOS CONTEXT/INBOX** | `CONTEXT/CONTEXT_BRIEF.md` doldur → `/latos-baslat` · boşken 600×200 uydurma yok |
| **Claude Code `.docx`/`.pdf`** | yeniden yükle → `uploads/` · `docs/CLAUDE-CODE-GUVENLIK-UYGULAMA.md` · byte-faithful extract |
| **Domain TF apply** | vault+cluster onayı sonra · `infra/observability/terraform/` · creds yoksa apply yok |
| **OpCo seçimi** | chat’te **tek** marka · `docs/holding/gorevler/` · üçü birden skip |

### Onaylayacaklarım
| İş | Yön + URL + not |
|---|---|
| **Bu rapor PR** | Review → merge · (açılınca buraya URL) · bu mesaj önceki CONFLICTING’leri kapattı |
| **MODE=IMPLEMENT** | Flip **yapma** · `SECURITY_STATE.md` · `TASKS/SEC-T003.md` tick’leri senden |
| **Unverified uzman yayın** | Human gate · `data/title_top100_queues.json` · K-003 |
| **CANVA:ON** | OAuth bitmeden açma · `STATE.md` |
| **Auto-run / YOLO** | Kapalı · `docs/CLAUDE-CODE-GUVENLIK-UYGULAMA.md` · `/cc-guvenlik` |
| **Domain purchase / PDF imza** | Domain adı / yetkili form yoksa **yok** |

## 3) Senin iş listen (Agent)

### Onaylılar (main’de)
Creative #616 · Security #617–#618 · LATOS #619 · live-ops #614 · Claude Code #628 · research-loop #629 · SEC-T003 #630 · Dependabot #621 #631 **#635** · rapor #632.

### İleridekiler (owner gerekmez / blocker sonrası)
- Monthly archive loop damga (bu tur yapıldı)
- LATOS job-card batch: CONTEXT dolunca `/latos-devam`
- Security ASSESS deepen; IMPLEMENT blocked
- Exa Authorize sonrası ≤5 sourced/disiplin
- Domain2 **plan-only** PR (apply yok)
- Vercel Doctor: link sonrası tekrar `/status`

## 4) Healthy roadmap + adam-saat (tahmin)
Band: **0.5 / 1 / 2 / 4 / 8 / 16** — gün/hafta yok.

| P | İş | Saat | Sahip |
|---|---|---|---|
| P0 | Cursor restart | 0.5 | Owner |
| P0 | MCP Authorize | 1 | Owner |
| P0 | vercel link | 0.5 | Owner |
| P0 | `.env.local` rotate | 0.5 | Owner |
| P0 | LATOS CONTEXT brief | 2 | Owner |
| P0 | `.docx`/`.pdf` upload | 0.5 | Owner |
| P0 | Merge #635 + close #633/#634 + loop + rapor | 1.5 | Agent **done** |
| P1 | SEC-T003 + 20 mapping review | 4 | Owner+Agent |
| P1 | MODE=IMPLEMENT | 8 | **blocked** |
| P1 | Domain2 TF plan→apply | 4 | Owner creds + Agent |
| P1 | LATOS expand post-brief | 8 | Agent |
| P1 | F5 lead+vaka | 16 | Owner+Agent |
| P2 | OpCo native scaffold (1) | 16 | Agent |
| P2 | Top-100 sourced deltas | 8 | Agent (Exa) |
| P2 | Canva OAuth → ON | 2 | Owner |

Owner P0 kalan ≈ **5.0 saat**.

## 5) Açık PR’lar
Bu yazım anında merge/close sonrası boştu; bu dalın draft PR’si açılacak.

## 6) 🚩 K-003 / red-flag
- 🚩 **900.000.000 karakter prompt** — refuse; `data/prompt_bank` + `PROMPTS/**/INDEX` + `/latos-devam`
- 🚩 **Uydurma top-100** — 79 sourced / 2021 pending; Exa needsAuth
- 🚩 **600×200 / 200 forecast/day** one-pass — refuse
- 🚩 **Bütün skill’leri live** — `skill_agency_registry` family stamp only
- 🚩 Vercel purchase domain (isim yok) · PDF sign · Windsor auth
- 🚩 ASSESS-ONLY · BRIEF-ONLY · Domain apply without vault

## 7) Kanıt
- Loop: `data/arsiv/2026-11/LOOP.json` · ts `2026-11-27T10:19:51Z`
- Registry: `data/skill_agency_registry.json` · 696/43/81
- `npm run validate` / `secret_scan` / `ethics_check` → **GECTI**

⏱️[2026-11-27T10:19:00Z→2026-11-27T10:22:00Z] 🔍[GEÇTİ] 📚[skill-route+merge+rapor] 🔗[prev 2026-11-15]
