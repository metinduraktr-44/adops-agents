# TEK SAYFA RAPOR — 2026-11-04 (Europe/Istanbul)
> Owner: Metin · Agent: devam+rapor (merge yok) · Kanıt: STATE / LATOS_STATE / SECURITY_STATE / AKTIVASYON-DURUM / `data/arsiv/2026-11/`
> Damga: 2026-11-04T11:35:21Z (UTC) · Yerel: 2026-11-04 14:35 +03 · Branch: `cursor/llm-agency-research-loop-50e1`
> prev: `docs/RAPOR-TEK-SAYFA-2026-11-03.md` · Repo: https://github.com/metinduraktr-44/adops-agents
> Bu PR: https://github.com/metinduraktr-44/adops-agents/pull/629 (draft · CONFLICTING · merge yok)

## 1) Durum
Main cron 04 Kasım yeşil: nightly `2026-11-04T00:12Z`, günlük `04:31Z`, apply-activation `06:21Z`, holding-konsolide `07:20Z`. **Kırmızı:** `holding-arastirma` `2026-11-04T01:01Z` — `scripts/holding_research.py` `KeyError: 'holding'` (`data/holding.json` v2.10 düz şema: kök `c_level`/`subsidiaries`; script `H["holding"]` bekliyor). `gece-holding-arastirma` yeşil.

Aylık arşiv **2026-11** okundu; research-loop continue **idempotent** koştu (`2026-11-04T11:35:21Z`). Kuyruk: **79 sourced / 2021 pending** — isim uydurma yok. Registry damga: **696 skill / 43 aile / 81 MCP** (plugin cache taraması; aylık `snapshot.json` hâlâ 132 — ayrı paket). Claude Code `.docx`/`.pdf` VM’de **yok** → #628 extract dokunulmadı. Security **MODE=ASSESS-ONLY**. Canva **BRIEF-ONLY**. LATOS CONTEXT/INBOX **owner boş**. F5 takvim geçti; kapı kriterleri kanıtsız açık. Claude Code paste **İPTAL**.

Bu görev **merge-onayı değil**. #628/#629 **CONFLICTING** + draft. #630 açık (validate yeşil, CONFLICTING).

## 2) Benim iş listem (Owner)

### Yapacaklarım
Her satır: **yönlendirme** · **URL** · **kısa not**.

| İş | Yönlendirme + URL + not |
|---|---|
| **Cursor restart** | **Yön:** Cursor → New Agent chat → Creative / Security / LATOS skills-hooks yüklensin. **URL:** https://cursor.com/docs/agent/chat · https://cursor.com/agents **Not:** Restart yoksa yeni rule/skill keşfi eksik kalır; risk düşük; skip = eski chat’te çalışmaya devam (hook drift). |
| **MCP Authorize** | **Yön:** Cursor Settings → MCP → yalnız ihtiyaç: Canva · Semgrep · Exa · Datadog · Sentry · PagerDuty → Authorize. **URL:** https://cursor.com/docs/context/mcp **Not:** Auth yoksa 🚩 offline docs; hepsini açma (maliyet/sızıntı). Skip = ASSESS/BRIEF-ONLY yeter. |
| **`.env.local` rotate** | **Yön:** OpenRouter → Keys → leaked key Revoke → yeni key → lokal `.env.local` (commit etme). **URL:** https://openrouter.ai/settings/keys · `docs/LLM-ENV.md` **Not:** Sohbette sızmış key krediyi yakar. Skip = iskelet makale; döngü kırılmaz. |
| **ANTHROPIC_API_KEY** | **Yön:** GitHub repo → Settings → Secrets and variables → Actions → `ANTHROPIC_API_KEY` yoksa ekle. **URL:** https://github.com/metinduraktr-44/adops-agents/settings/secrets/actions **Not:** Secret yoksa makale/holding LLM iskelet. Skip = cron yeşil kalır, içerik zayıf. |
| **LATOS CONTEXT/INBOX** | **Yön:** `CONTEXT/CONTEXT_BRIEF.md` + `CONTEXT/INBOX/` marka brief doldur → chat’te `/latos-baslat`. **URL:** repo `CONTEXT/CONTEXT_BRIEF.md` · `LATOS_STATE.md` **Not:** Placeholder’da job-card batch uydurma olur (K-003). Skip = örnek 6 kart sınırı. |
| **Domain TF apply** | **Yön:** Vault creds + cluster onayı sonra `infra/observability/terraform/` plan→apply. **URL:** `infra/observability/terraform/` · Domain pack `data/domains/domain_pack.json` **Not:** Creds yoksa **apply yok**. Skip = plan-only. Risk: yanlış cluster. |
| **OpCo scaffold seçimi** | **Yön:** Chat’te tek marka söyle: VizaTrack / Movea / Cigkoftem. **URL:** `docs/holding/gorevler/` · `data/holding.json` **Not:** Üçünü birden native scaffold = kapsam şişmesi. Skip = HoldCo doküman yeter. |

### Onaylayacaklarım
| İş | Yön + URL + not |
|---|---|
| **#628 draft** | **Yön:** PR Files + Conversation oku; Auto-run/YOLO kapalı tut; merge **şimdi yok** (CONFLICTING). **URL:** https://github.com/metinduraktr-44/adops-agents/pull/628 **Not:** `.docx`/`.pdf` byte-faithful extract owner yüklemesi bekler. Validate yeşil. Draft. |
| **#629 draft** | **Yön:** Bu rapor+loop PR’ı incele; merge yok (CONFLICTING + bu mesaj onay değil). **URL:** https://github.com/metinduraktr-44/adops-agents/pull/629 **Not:** K-003 kuyruk pending; 900B yok. Validate yeşil (eski run). |
| **#630 open** | **Yön:** SEC-T003 lock + upload talimatı + ethics FP; merge kararı sende. **URL:** https://github.com/metinduraktr-44/adops-agents/pull/630 **Not:** ASSESS-ONLY. CONFLICTING. Validate yeşil. |
| **MODE=IMPLEMENT** | **Yön:** Flip **yapma** ta ki gap/risk/SoA uzman + yazılı kriter. Komut: `/sec-gap-analizi` (ASSESS). **URL:** `SECURITY_STATE.md` · `TASKS/SEC-T003.md` (varsa #630). **Not:** Live remediate yasak. |
| **Unverified uzman** | **Yön:** LATOS/Security expert listesi `pending_research` / sourced-URL; yayınlama = sen. **URL:** `LATOS_STATE.md` Human approval gates · `data/title_top100_queues.json` **Not:** İsim uydurma = K-003 ihlali. |
| **Dependabot** | **Yön:** #627 codeql-action 4.39.1 + #621 setup-python 5→7 pin/CI oku; yeşil+pin sonra merge. **URL:** https://github.com/metinduraktr-44/adops-agents/pull/627 · https://github.com/metinduraktr-44/adops-agents/pull/621 **Not:** Node 20 deprecation uyarısı Actions’ta var; acele merge yok. |
| **CANVA:ON** | **Yön:** Canva OAuth bitmeden açma. **URL:** `STATE.md` · Canva MCP Authorize **Not:** BRIEF-ONLY güvenli varsayılan. |

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
- Cron izle; **holding-arastirma** şema drift düzelt (`holding_research.py`: `H["holding"]` → kök `H` + `H["c_level"]` / `H["subsidiaries"]`) — ayrı küçük PR, bu loop’a karıştırma
- LATOS job-card: CONTEXT dolmadan **örnek kart**
- Security ASSESS deepen; IMPLEMENT yok
- Domain2 **plan-only** iskelet
- F5 içerik: `makaleler/` + README CTA; gelir checkbox owner
- #628 extract: `uploads/` hâlâ boş → dokunma
- ManagePullRequest MCP bu ortamda **yok** (GitHub write MCP unregistered) → PR gövdesi git push ile güncellenir
- Eski merged branch prune (opsiyonel)

## 4) Roadmap + adam-saat
Band: **0.5 / 1 / 2 / 4 / 8 / 16** saat. Süre = **tahmin** (kişi-saat). Gün/hafta yok. F5 takvim kapandı; iş açık.

| P | İş | Tahmin (saat) | Sahip |
|---|---|---|---|
| **P0** | Cursor restart + skill/hook keşif | 0.5 **tahmin** | Owner |
| **P0** | MCP Authorize (ihtiyaç listesi) | 1 **tahmin** | Owner |
| **P0** | `.env.local` rotate + secret kontrol | 0.5 **tahmin** | Owner |
| **P0** | LATOS CONTEXT/INBOX brief | 2 **tahmin** | Owner |
| **P0** | #628/#629/#630 review (merge yok) | 1 **tahmin** | Owner |
| **P0** | `holding_research.py` KeyError fix (CI) | 0.5 **tahmin** | Agent |
| **P1** | Security MODE kriter + uzman 20 mapping | 4 **tahmin** | Owner+Agent (ASSESS) |
| **P1** | IMPLEMENT (onay **sonrası**) | 8 **tahmin** | Agent — **blocked** |
| **P1** | Domain2 TF+OTel plan → apply | 4 **tahmin** | Owner creds + Agent |
| **P1** | LATOS job-card genişlet | 8 **tahmin** | Agent post-brief |
| **P1** | F5: lead + gelir kaydı + vaka #1 | 16 **tahmin** | Owner ticari + Agent içerik |
| **P1** | Dependabot #627 + #621 karar | 0.5 **tahmin** | Owner |
| **P2** | OpCo native scaffold (1 marka) | 16 **tahmin** | Agent post-seçim |
| **P2** | Top-100 kuyruk (Exa/MCP; sourced+pending) | 8 **tahmin** | Agent monthly |
| **P2** | Canva OAuth → CANVA:ON deneme | 2 **tahmin** | Owner OAuth |

Toplam owner-kritik P0: **~5 saat tahmin**. Agent P0 CI-fix: **0.5 saat tahmin**. Agent P1 (blocked hariç, cron+rapor+assess): **~2–4 saat/koşum tahmin**.

## 5) Açık PR URL list
| # | Durum | Başlık | URL |
|---|---|---|---|
| **630** | OPEN | Continue agency OS: SEC-T003 lock, owner upload docs, ethics FP | https://github.com/metinduraktr-44/adops-agents/pull/630 |
| **629** | **DRAFT** · CONFLICTING | Research loop continue (archive-first, pending top-100) | https://github.com/metinduraktr-44/adops-agents/pull/629 |
| **628** | **DRAFT** · CONFLICTING | Claude Code güvenlik uyarıları — Cursor eşdeğerleri | https://github.com/metinduraktr-44/adops-agents/pull/628 |
| **627** | OPEN | build(deps): codeql-action 4.37.9 → 4.39.1 | https://github.com/metinduraktr-44/adops-agents/pull/627 |
| **621** | OPEN | build(deps): actions/setup-python 5 → 7 | https://github.com/metinduraktr-44/adops-agents/pull/621 |

Merge **yok**. CI yeşil ≠ merge onayı.

## 6) Risk / K-003
- 🚩 900B prompt / uydurma top-100 / secret minting → **yapılmadı** (K-003)
- 🚩 Security MODE=ASSESS-ONLY — live remediate yok
- 🚩 MCP security catalog default OFF; ManagePullRequest MCP bu ajan yüzeyinde yok
- 🚩 Domain2 TF apply — credential olmadan apply yok
- 🚩 ANTHROPIC_API_KEY boş → makale/holding LLM iskelet (`holding-arastirma` log: `ANTHROPIC_API_KEY:` empty)
- 🚩 `holding-arastirma` 2026-11-04 **failure** — şema drift; `gece-holding-arastirma` yeşil (farklı script)
- 🚩 F5 kapı 2026-09-30 geçti; gelir checkbox açık (`docs/GELIR-MODELI-TAKIP.md`)
- 🚩 Unverified uzman yayınlama = human gate
- 🚩 #628/#629/#630 CONFLICTING vs main — rebase owner onayı olmadan force yok
- 🚩 `.docx`/`.pdf` uploads yok → #628 corpus extract duruyor
- ✅ paste Claude Code **İPTAL** · research-loop 2026-11-04 GECTI · kuyruk 79/2021

### Hızlı URL
| Kaynak | Yol |
|---|---|
| Main | https://github.com/metinduraktr-44/adops-agents |
| #629 | https://github.com/metinduraktr-44/adops-agents/pull/629 |
| MCP | https://cursor.com/docs/context/mcp |
| LLM env | `docs/LLM-ENV.md` |
| Security / LATOS / Creative | `SECURITY_STATE.md` · `LATOS_STATE.md` · `STATE.md` |
| Observability IaC | `infra/observability/terraform/` |
| Yol haritası | `docs/YOL-HARITASI.md` |
| holding-arastirma fail | https://github.com/metinduraktr-44/adops-agents/actions/runs/41751146016 |

⏱️[2026-11-04T11:34:29Z→2026-11-04T11:37:00Z] 🔍[GEÇTİ] 📚[tek sayfa 2026-11-04; loop damga; #630 eklendi; holding KeyError] 🔗[prev RAPOR-TEK-SAYFA-2026-11-03 used]
