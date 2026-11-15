# TEK SAYFA RAPOR — 2026-11-15C (Europe/Istanbul) · DEVAM ET RAPORLA
> Owner: Metin · Onaylıyorum merge + skill-dump routing + Vercel /status · Kanıt: STATE / LATOS_STATE / SECURITY_STATE / `data/arsiv/2026-11/`
> Damga: 2026-11-15T11:08:00Z (UTC) · Yerel: 2026-11-15 14:08 +03 · dal: `cursor/tek-sayfa-rapor-15c-bdd4`
> prev: `docs/RAPOR-TEK-SAYFA-2026-11-15.md` · Repo: https://github.com/metinduraktr-44/adops-agents

## 1) Durum + merges + Vercel

| Madde | Sonuç |
|---|---|
| **Vercel /status** | **NOT linked** — `.vercel/project.json` yok · `vercel` CLI yok · MCP `Vercel` = **needsAuth** · Doctor **STOP** (gh Actions fallback yok) · öneri: `vercel link` sonra `/status` |
| **purchase domain** | 🚩 refuse — domain adı yok (owner dump’ta 2× listelenmiş) |
| **Merge pass** | Açık PR **[]** — zaten merge: **#630 #621 #631 #629 #628** (10:06Z pass) · force-merge red CI yok |
| **Validate** | `npm run validate` → GECTI (bu dalda yeniden koşulacak) |
| **Research loop** | `2026-11-15T11:07:16Z` · queues **79 sourced / 2021 pending** · registry **696 / 43 / 81** |
| **Skill matrix** | `ORG/SKILL_MATRIX.md` family router refresh |
| **Security** | **ASSESS-ONLY** · Canva **BRIEF-ONLY** · Exa **needsAuth** |
| **LATOS light** | ROSTER 600 · EXPERTS pending · PROMPTS INDEX stubs (6) · SKILLS_TALENT ~100 · CALENDAR 2026-11 stamp |

### Merged (bugün — yeniden açılmadı)
| PR | URL |
|---|---|
| #630 Continue agency OS | https://github.com/metinduraktr-44/adops-agents/pull/630 |
| #621 setup-python 5→7 | https://github.com/metinduraktr-44/adops-agents/pull/621 |
| #631 codeql-action bump | https://github.com/metinduraktr-44/adops-agents/pull/631 |
| #629 research-loop + LATOS | https://github.com/metinduraktr-44/adops-agents/pull/629 |
| #628 Claude Code güvenlik | https://github.com/metinduraktr-44/adops-agents/pull/628 |

## 2) Yapacaklarım (Owner)

| İş | Yön + URL + kısa not |
|---|---|
| **Cursor restart** | New Agent · https://cursor.com/docs/agent/chat · hooks/skills (#628) keşfi |
| **MCP Authorize** | Settings→MCP · https://cursor.com/docs/context/mcp · Exa+Vercel needsAuth → sourced/doctor kapalı |
| **`vercel link`** | Proje kökü · https://vercel.com/docs/cli/link · sonra `/status` Doctor |
| **`.env.local` rotate** | https://openrouter.ai/settings/keys · `docs/LLM-ENV.md` · commit etme |
| **ANTHROPIC_API_KEY (Actions)** | https://github.com/metinduraktr-44/adops-agents/settings/secrets/actions · yoksa LLM iskelet |
| **LATOS CONTEXT/INBOX** | `CONTEXT/CONTEXT_BRIEF.md` → `/latos-baslat` · boşken 600×200 uydurma yok |
| **#628 byte-faithful upload** | `.docx`/`.pdf` → `uploads/` · `docs/OWNER-UPLOAD-CLAUDE-CODE-DOCS.md` |
| **Domain TF apply** | vault+cluster · `infra/observability/terraform/` · creds yoksa apply yok |
| **OpCo seçimi** | chat’te tek marka · `docs/holding/gorevler/` |

## 3) Onaylayacaklarım

| İş | Yön + URL + not |
|---|---|
| **MODE=IMPLEMENT** | Flip yapma · `SECURITY_STATE.md` · `TASKS/SEC-T003.md` |
| **Unverified uzman publish** | Senin gate · `data/title_top100_queues.json` · K-003 |
| **CANVA:ON** | OAuth bitmeden açma · `STATE.md` |
| **Auto-run/YOLO** | Kapalı · `docs/CLAUDE-CODE-GUVENLIK-UYGULAMA.md` · `/cc-guvenlik` |
| **Vercel domain purchase** | İsim ver + onay · aksi 🚩 |
| **Bu PR (15C) merge** | Yeşil CI sonrası · branch `cursor/tek-sayfa-rapor-15c-bdd4` |

## 4) Agent — Onaylılar + İleridekiler

### Onaylılar (main)
#616 Creative OS · #617–#619 Security+LATOS · #614 live-ops · #607 HoldCo · **#630 #621 #631 #629 #628** · research-loop + SKILL_MATRIX 15C (bu dal).

### İleridekiler
- LATOS job-card: CONTEXT dolmadan örnek + `/latos-devam` only
- Security ASSESS deepen; IMPLEMENT yok
- Exa Authorize → ≤5 sourced/disiplin
- Vercel link sonrası Doctor (env counts, drains, analytics)
- Domain2 plan-only · F5 ticari owner+makale · holding cron izle

## 5) Roadmap + adam-saat
Band **0.5 / 1 / 2 / 4 / 8 / 16** (gün/hafta yok).

| P | İş | Saat | Sahip |
|---|---|---|---|
| P0 | Cursor restart | 0.5 | Owner |
| P0 | MCP Authorize (Exa+Vercel) | 1 | Owner |
| P0 | `vercel link` + `/status` | 0.5 | Owner |
| P0 | `.env.local` rotate | 0.5 | Owner |
| P0 | LATOS CONTEXT brief | 2 | Owner |
| P0 | `.docx`/`.pdf` upload | 0.5 | Owner |
| P0 | Skill dump → family stamp + 15C rapor | 1 | Agent **done** |
| P0 | Merge yeşil PR’lar | 1 | Agent **done** (önceki) |
| P1 | SEC MODE kriter + 20 mapping | 4 | Owner+Agent |
| P1 | IMPLEMENT | 8 | **blocked** |
| P1 | Domain2 TF | 4 | Owner creds+Agent |
| P1 | LATOS expand post-brief | 8 | Agent |
| P1 | F5 lead+vaka | 16 | Owner+Agent |
| P2 | OpCo scaffold (1) | 16 | Agent |
| P2 | Top-100 sourced deltas | 8 | Agent |
| P2 | Canva OAuth | 2 | Owner |

**Owner P0 kalan: ~5.0 saat** · Agent P0 bu tur: **~1.0 saat** (tamam).

## 6) 🚩 K-003 / güvenlik
- 🚩 **all-skills live** — family mini-agency + stamp only (`ORG/SKILL_MATRIX.md`)
- 🚩 **900M karakter prompt** — refuse; prompt_bank + INDEX stubs
- 🚩 **Uydurma top-100** — 79/2021; Exa needsAuth
- 🚩 **600×200 / forecast one-pass** — refuse
- 🚩 **purchase_vercel_domain** — domain adı yok
- 🚩 **Unsigned PDF sign-fill** — upload yok; imza yok
- 🚩 **Windsor AI auth** — invent data yok; needsAuth → catalog
- 🚩 ASSESS-ONLY · BRIEF-ONLY · Vercel not linked

## 7) Kanıt
- `data/arsiv/2026-11/LOOP.json` · `docs/SKILL-AGENCY-REGISTRY.md` · `ORG/SKILL_MATRIX.md`
- `docs/RAPOR-TEK-SAYFA-2026-11-15C.md` (bu dosya)
- Merged set: #630 #621 #631 #629 #628 · açık PR: yok (15C PR açılacak)
