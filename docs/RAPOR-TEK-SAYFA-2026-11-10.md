# TEK SAYFA RAPOR — 2026-11-10 (Europe/Istanbul)
> Owner: Metin · Agent: devam+rapor (merge yok) · Kanıt: STATE / LATOS_STATE / SECURITY_STATE / AKTIVASYON-DURUM / `data/arsiv/2026-11/`
> Damga: 2026-11-10T11:56:30Z (UTC) · Yerel: 2026-11-10 14:56 +03 · Branch: `cursor/llm-agency-research-loop-50e1`
> prev: `docs/RAPOR-TEK-SAYFA-2026-11-04.md` · Repo: https://github.com/metinduraktr-44/adops-agents
> Bu PR: https://github.com/metinduraktr-44/adops-agents/pull/629 (draft · rebase `origin/main` · merge yok)

## 1) Durum
Main cron 10 Kasım (UTC): nightly `2026-11-10T00:11Z` yeşil, günlük `04:31Z` yeşil, apply-activation `06:20Z` yeşil, holding-konsolide `07:19Z` yeşil. **Kırmızı:** `holding-arastirma` `2026-11-10T01:01Z` — `scripts/holding_research.py` `KeyError: 'holding'` (`data/holding.json` v2.10 kök `c_level`/`subsidiaries`; script `H["holding"]`). Bu dalda tek satır fix **yok** → genişletilmedi. `gece-holding-arastirma` 09 Kas `23:30Z` yeşil.

Aylık arşiv **2026-11** okundu; research-loop continue **idempotent** `2026-11-10T11:55:24Z`. Kuyruk: **79 sourced / 2021 pending** — isim uydurma yok. Registry damga: **696 skill / 43 aile / 81 MCP**. Claude Code `.docx`/`.pdf` VM’de **yok** (`uploads/` yok) → #628 extract dokunulmadı. Security **MODE=ASSESS-ONLY**. Canva **BRIEF-ONLY**. LATOS CONTEXT/INBOX **owner boş**. Claude Code paste **İPTAL**.

**#629:** `origin/main` üzerine rebase (AUDIT/BILGI kronolojik birleşim). Push öncesi GitHub `CONFLICTING`; push sonrası beklenen `CLEAN` (doğrula PR sayfası). Bu görev **merge-onayı değil**.

Açık PR (live `gh pr list`): #631 Dependabot codeql 4.39.3 MERGEABLE; #630 CONFLICTING; #629 draft; #628 draft CONFLICTING; #621 MERGEABLE. **#627 kapalı** (4.39.1 → 4.39.3 ile yer değişti).

## 2) Benim iş listem (Owner)

### Yapacaklarım
Her satırın içinde: **yönlendirme** · **URL** · **kısa not**.

| İş | Yönlendirme + URL + not |
|---|---|
| **Cursor restart** | **Yön:** Cursor → New Agent chat (skills/hooks yüklensin). **URL:** https://cursor.com/docs/agent/chat · https://cursor.com/agents **Not:** Restart yoksa yeni rule/skill keşfi eksik; risk düşük; skip = eski chat (hook drift). |
| **MCP Authorize** | **Yön:** Cursor Settings → MCP → yalnız ihtiyaç: Canva · Semgrep · Exa · Datadog · Sentry · PagerDuty → Authorize. **URL:** https://cursor.com/docs/context/mcp **Not:** Auth yoksa 🚩 offline docs; hepsini açma. Skip = ASSESS/BRIEF-ONLY yeter. |
| **`.env.local` rotate** | **Yön:** OpenRouter → Keys → leaked key Revoke → yeni key → lokal `.env.local` (commit etme). **URL:** https://openrouter.ai/settings/keys · `docs/LLM-ENV.md` **Not:** Sohbette sızmış key krediyi yakar. Skip = iskelet makale; döngü kırılmaz. |
| **ANTHROPIC_API_KEY** | **Yön:** GitHub repo → Settings → Secrets and variables → Actions → secret yoksa ekle. **URL:** https://github.com/metinduraktr-44/adops-agents/settings/secrets/actions **Not:** Yoksa makale/holding LLM iskelet. Skip = cron yeşil, içerik zayıf. |
| **LATOS CONTEXT/INBOX** | **Yön:** `CONTEXT/CONTEXT_BRIEF.md` + `CONTEXT/INBOX/` marka brief doldur → chat `/latos-baslat`. **URL:** repo `CONTEXT/CONTEXT_BRIEF.md` · `LATOS_STATE.md` **Not:** Placeholder’da job-card uydurma (K-003). Skip = 6 örnek kart. |
| **Domain TF apply** | **Yön:** Vault creds + cluster onayı sonra `infra/observability/terraform/` plan→apply. **URL:** `infra/observability/terraform/` · `data/domains/domain_pack.json` **Not:** Creds yoksa **apply yok**. Skip = plan-only. Risk: yanlış cluster. |
| **OpCo scaffold seçimi** | **Yön:** Chat’te tek marka: VizaTrack / Movea / Cigkoftem. **URL:** `docs/holding/gorevler/` · `data/holding.json` **Not:** Üçünü birden native scaffold = şişme. Skip = HoldCo doküman yeter. |
| **holding-arastirma CI** | **Yön:** Actions → failed run oku; ayrı küçük PR’da `holding_research.py` şema. **Komut (ajan, sonra):** `H.get("holding", H)` — bu loop’ta **yok**. **URL:** https://github.com/metinduraktr-44/adops-agents/actions/runs/42732728755 **Not:** Main cron kırmızı; `gece-holding-arastirma` yeşil. Skip = not yeterli (bu mesaj). |

### Onaylayacaklarım
| İş | Yön + URL + not |
|---|---|
| **#628 draft** | **Yön:** PR Files + Conversation; Auto-run/YOLO kapalı; merge **şimdi yok** (CONFLICTING). **URL:** https://github.com/metinduraktr-44/adops-agents/pull/628 **Not:** `.docx`/`.pdf` extract owner yüklemesi bekler. Validate yeşil (eski). |
| **#629 draft** | **Yön:** Bu rapor+rebase+loop incele; merge yok (bu mesaj onay değil). Push sonrası conflict durumunu PR’da doğrula. **URL:** https://github.com/metinduraktr-44/adops-agents/pull/629 **Not:** K-003 pending kuyruk; 900B yok. Rebase `origin/main`. |
| **#630 open** | **Yön:** SEC-T003 lock + upload talimatı + ethics FP; merge sende. **URL:** https://github.com/metinduraktr-44/adops-agents/pull/630 **Not:** ASSESS-ONLY. CONFLICTING. Validate yeşil. |
| **MODE=IMPLEMENT** | **Yön:** Flip **yapma** ta ki gap/risk/SoA uzman + yazılı kriter. Komut: `/sec-gap-analizi` (ASSESS). **URL:** `SECURITY_STATE.md` **Not:** Live remediate yasak. |
| **Unverified uzman** | **Yön:** LATOS/Security expert `pending_research` / sourced-URL; yayın = sen. **URL:** `LATOS_STATE.md` Human approval gates · `data/title_top100_queues.json` **Not:** İsim uydurma = K-003. |
| **Dependabot #631** | **Yön:** codeql-action 4.37.9→4.39.3 pin/CI oku; yeşil+pin sonra merge. **URL:** https://github.com/metinduraktr-44/adops-agents/pull/631 **Not:** #627 kapalı. MERGEABLE + validate yeşil. Acele yok. |
| **Dependabot #621** | **Yön:** setup-python 5→7 CI oku; yeşil+pin sonra merge. **URL:** https://github.com/metinduraktr-44/adops-agents/pull/621 **Not:** MERGEABLE; Node 20 deprecation Actions’ta olabilir. |
| **CANVA:ON** | **Yön:** Canva OAuth bitmeden açma. **URL:** `STATE.md` · Canva MCP Authorize **Not:** BRIEF-ONLY varsayılan. |

## 3) Senin iş listen (Agent)

### Onaylılar (main’de / prior owner «Onaylıyorum»)
| PR | Ne | URL |
|---|---|---|
| #616 | Creative Agency OS · CANVA:BRIEF-ONLY | https://github.com/metinduraktr-44/adops-agents/pull/616 |
| #618 | Security Governance OS · ASSESS-ONLY | https://github.com/metinduraktr-44/adops-agents/pull/618 |
| #617 | Security GIGA pack | https://github.com/metinduraktr-44/adops-agents/pull/617 |
| #619 | LATOS GIGA | https://github.com/metinduraktr-44/adops-agents/pull/619 |
| #614 | live-ops + domain-obs-router | https://github.com/metinduraktr-44/adops-agents/pull/614 |
| #612 | setup-python 5→7 (eski bump) | https://github.com/metinduraktr-44/adops-agents/pull/612 |
| #620 | codeql-action 4.37.4→4.37.9 | https://github.com/metinduraktr-44/adops-agents/pull/620 |
| #607 | v2.8–v2.13 agency+HoldCo+Domain | https://github.com/metinduraktr-44/adops-agents/pull/607 |

Aktivasyon in-repo: `docs/AKTIVASYON-DURUM.md`. Org 600 · prompt bank 122×3 · skill mini-ajans · HoldCo · Domain pack **main’de**.

### İleridekiler (owner beklemeden)
- Cron izle; **holding-arastirma** şema drift ayrı küçük PR (`H["holding"]` → kök `H`) — bu loop’a karıştırılmadı
- LATOS job-card: CONTEXT dolmadan **örnek kart**
- Security ASSESS deepen; IMPLEMENT yok
- Domain2 **plan-only**
- F5 içerik: `makaleler/` + README CTA
- #628 extract: `uploads/` boş → dokunma
- ManagePullRequest MCP bu ortamda **yok** → PR gövdesi git push ile güncellenir
- #629 conflict: rebase bu koşuda yapıldı; push `--force-with-lease`

## 4) Roadmap + adam-saat
Band: **0.5 / 1 / 2 / 4 / 8 / 16** saat. Süre = **tahmin** (kişi-saat). Gün/hafta yok.

| P | İş | Tahmin (saat) | Sahip |
|---|---|---|---|
| **P0** | Cursor restart + skill/hook keşif | 0.5 **tahmin** | Owner |
| **P0** | MCP Authorize (ihtiyaç listesi) | 1 **tahmin** | Owner |
| **P0** | `.env.local` rotate + secret kontrol | 0.5 **tahmin** | Owner |
| **P0** | LATOS CONTEXT/INBOX brief | 2 **tahmin** | Owner |
| **P0** | #628/#629/#630 review (merge yok) | 1 **tahmin** | Owner |
| **P0** | `holding_research.py` KeyError fix (CI) | 0.5 **tahmin** | Agent (ayrı PR) |
| **P1** | Security MODE kriter + uzman 20 mapping | 4 **tahmin** | Owner+Agent (ASSESS) |
| **P1** | IMPLEMENT (onay **sonrası**) | 8 **tahmin** | Agent — **blocked** |
| **P1** | Domain2 TF+OTel plan → apply | 4 **tahmin** | Owner creds + Agent |
| **P1** | LATOS job-card genişlet | 8 **tahmin** | Agent post-brief |
| **P1** | F5: lead + gelir kaydı + vaka #1 | 16 **tahmin** | Owner ticari + Agent içerik |
| **P1** | Dependabot #631 + #621 karar | 0.5 **tahmin** | Owner |
| **P2** | OpCo native scaffold (1 marka) | 16 **tahmin** | Agent post-seçim |
| **P2** | Top-100 kuyruk (Exa/MCP; sourced+pending) | 8 **tahmin** | Agent monthly |
| **P2** | Canva OAuth → CANVA:ON deneme | 2 **tahmin** | Owner OAuth |

Toplam owner-kritik P0: **~5 saat tahmin**. Agent P0 CI-fix: **0.5 saat tahmin**. Agent P1 (blocked hariç, cron+rapor+assess): **~2–4 saat/koşum tahmin**.

## 5) Açık PR URL list
Live: `gh pr list --state open` 2026-11-10T11:53Z.

| # | Durum | Başlık | URL |
|---|---|---|---|
| **631** | OPEN · MERGEABLE | build(deps): codeql-action 4.37.9 → 4.39.3 | https://github.com/metinduraktr-44/adops-agents/pull/631 |
| **630** | OPEN · CONFLICTING | Continue agency OS: SEC-T003 lock, owner upload docs, ethics FP | https://github.com/metinduraktr-44/adops-agents/pull/630 |
| **629** | **DRAFT** · rebase bu koşu | Research loop continue (archive-first, pending top-100) | https://github.com/metinduraktr-44/adops-agents/pull/629 |
| **628** | **DRAFT** · CONFLICTING | Claude Code güvenlik uyarıları — Cursor eşdeğerleri | https://github.com/metinduraktr-44/adops-agents/pull/628 |
| **621** | OPEN · MERGEABLE | build(deps): actions/setup-python 5 → 7 | https://github.com/metinduraktr-44/adops-agents/pull/621 |

Kapalı (referans): #627 codeql 4.39.1 — https://github.com/metinduraktr-44/adops-agents/pull/627

Merge **yok**. CI yeşil ≠ merge onayı.

## 6) Risk / K-003
- 🚩 900B prompt / uydurma top-100 / secret minting → **yapılmadı** (K-003)
- 🚩 Security MODE=ASSESS-ONLY — live remediate yok
- 🚩 MCP security catalog default OFF; ManagePullRequest MCP yok
- 🚩 Domain2 TF apply — credential olmadan apply yok
- 🚩 ANTHROPIC_API_KEY boş → LLM iskelet
- 🚩 `holding-arastirma` 2026-11-10 **failure** — şema drift; bu dalda fix yok
- 🚩 F5 kapı 2026-09-30 geçti; gelir checkbox açık
- 🚩 Unverified uzman yayınlama = human gate
- 🚩 #628/#630 hâlâ CONFLICTING vs main; #629 rebase+lease push
- 🚩 `.docx`/`.pdf` uploads yok → #628 extract duruyor
- ✅ paste Claude Code **İPTAL** · research-loop 2026-11-10 GECTI · kuyruk 79/2021

### Hızlı URL
| Kaynak | Yol |
|---|---|
| Main | https://github.com/metinduraktr-44/adops-agents |
| #629 | https://github.com/metinduraktr-44/adops-agents/pull/629 |
| MCP | https://cursor.com/docs/context/mcp |
| LLM env | `docs/LLM-ENV.md` |
| Security / LATOS / Creative | `SECURITY_STATE.md` · `LATOS_STATE.md` · `STATE.md` |
| Observability IaC | `infra/observability/terraform/` |
| holding-arastirma fail | https://github.com/metinduraktr-44/adops-agents/actions/runs/42732728755 |

⏱️[2026-11-10T11:53:41Z→2026-11-10T11:57:00Z] 🔍[GEÇTİ] 📚[tek sayfa 2026-11-10; #629 rebase; loop damga; #631/#627 not] 🔗[prev RAPOR-TEK-SAYFA-2026-11-04 used]
