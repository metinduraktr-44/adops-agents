# TEK SAYFA RAPOR — 2026-11-03 (Europe/Istanbul)
> Owner: Metin · Agent: rapor+PR (merge yok) · Kanıt: STATE / LATOS_STATE / SECURITY_STATE / AKTIVASYON-DURUM · prev: `docs/RAPOR-TEK-SAYFA-2026-09-02.md`
> Damga: 2026-11-03T11:46:00Z · Branch: `cursor/llm-agency-research-loop-50e1` · Rapor ajanı: https://cursor.com/agents/bc-03ed1014-419a-53f5-9ddd-cd8d6a44f71b
> Kardeş ajan (aynı branch, dokunma): `bc-fe57f032-9a3d-527d-8657-b0dd886b2ecd`

## 1) Durum
Main yeşil döngüde: nightly `2026-11-03T00:12Z`, daily standup+makale `2026-11-03T04:31Z`, kurul `2026-11-01` (açık P0=8 · gelir aksiyonu=19). Aylık arşiv **2026-11** damgalı. F5 penceresi (Inbound Huni) **takvim olarak geçti**; kapı kriterleri (lead / gelir kaydı / vaka #1) **kanıtsız açık**. Claude Code paste **İPTAL**. Security **MODE=ASSESS-ONLY**. Canva **BRIEF-ONLY**. LATOS CONTEXT/INBOX **owner boş**. Bu branch main ile aynı tip’teydi; bu commit yalnız rapor.

Repo: https://github.com/metinduraktr-44/adops-agents

## 2) Benim iş listem (Owner)

### Yapacaklarım
| İş | Yön | URL |
|---|---|---|
| **Cursor restart** | Yeni Agent chat → Creative + Security + LATOS skills/hooks yüklensin | https://cursor.com/docs/agent/chat |
| **MCP Authorize** | Yalnız ihtiyaç: Canva · Semgrep · Exa · Datadog · Sentry · PagerDuty | https://cursor.com/docs/context/mcp |
| **`.env.local` rotate** | Leaked OpenRouter key iptal + yeni key; commit etme | https://openrouter.ai/settings/keys · `docs/LLM-ENV.md` |
| **ANTHROPIC_API_KEY** | GitHub secret yoksa makale hattı iskelet | Repo → Settings → Secrets |
| **LATOS CONTEXT/INBOX** | Marka brief doldur (şu an placeholder) → `/latos-baslat` | `CONTEXT/CONTEXT_BRIEF.md` · `CONTEXT/INBOX/` |
| **Domain TF apply** | Vault creds + cluster onayı; creds yoksa apply yok | `infra/observability/terraform/` |
| **OpCo scaffold seçimi** | VizaTrack / Movea / Cigkoftem hangisi önce | `docs/holding/gorevler/` |

### Onaylayacaklarım
| İş | Not | URL |
|---|---|---|
| **#628 draft** | Claude Code güvenlik uyarıları — Cursor eşdeğerleri. Owner `.docx`/`.pdf` byte-faithful extract; Auto-run/YOLO kapalı | https://github.com/metinduraktr-44/adops-agents/pull/628 |
| **Security MODE=IMPLEMENT** | Flip **yapma** ta ki gap/risk/SoA uzman incelemesi + yazılı kriter | `SECURITY_STATE.md` · `/sec-gap-analizi` |
| **Merge** | Bu görevde merge yok. #628 draft; #627/#621 Dependabot — CI+pin incele | aşağı §5 |
| **Unverified uzman listeleri** | LATOS/Security expert: `pending_research` / sourced only; yayınlama onayı sende | `LATOS_STATE.md` Human approval gates |
| **Canva CANVA:ON** | OAuth bitmeden açma | `STATE.md` |

## 3) Senin iş listen (Agent)

### Onaylılar (main’de bitmiş — 2026-08-31 «Onaylıyorum» batch)
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

Aktivasyon in-repo: `docs/AKTIVASYON-DURUM.md`. Org 600 · prompt bank 122×3 · skill mini-ajans · HoldCo · Domain pack main’de.

### Sonraki adımlar (owner beklemeden)
- Günlük/nightly/aylık cron izle (2026-11-03 yeşil)
- LATOS job-card generator batch (`/latos-devam`) — CONTEXT dolmadan **örnek kart** sınırında
- Security ASSESS deepen + `CALENDAR/` monthly stub — IMPLEMENT yok
- Domain2 **plan-only** PR iskeleti (apply token gelince)
- F5 içerik: `makaleler/` + README CTA; gelir checkbox’ları owner
- Kardeş ajan araştırma loop’una **path çakıştırma** (`docs/RAPOR-TEK-SAYFA-2026-11-03.md` ayrı)
- Eski merged branch prune (opsiyonel)

## 4) Roadmap + adam-saat
Band: **0.5 / 1 / 2 / 4 / 8 / 16** saat. Süre = **tahmin** (kişi-saat), gün/hafta değil. F5 takvim kapandı; iş açık.

| P | İş | Tahmin (saat) | Sahip |
|---|---|---|---|
| **P0** | Cursor restart + skill/hook keşif | 0.5 **tahmin** | Owner |
| **P0** | MCP Authorize (ihtiyaç listesi) | 1 **tahmin** | Owner |
| **P0** | `.env.local` rotate + secret kontrol | 0.5 **tahmin** | Owner |
| **P0** | LATOS CONTEXT/INBOX brief | 2 **tahmin** | Owner |
| **P0** | #628 draft review (güvenlik eşdeğer) | 1 **tahmin** | Owner |
| **P1** | Security MODE kriter yaz + uzman 20 mapping | 4 **tahmin** | Owner+Agent (ASSESS) |
| **P1** | IMPLEMENT (onay **sonrası**) | 8 **tahmin** | Agent — **blocked** |
| **P1** | Domain2 TF+OTel plan → apply | 4 **tahmin** | Owner creds + Agent |
| **P1** | LATOS job-card genişlet (örnek→batch) | 8 **tahmin** | Agent post-brief |
| **P1** | F5: nitelikli lead + gelir kaydı + vaka #1 | 16 **tahmin** | Owner ticari + Agent içerik |
| **P1** | Dependabot #627 + #621 review/merge kararı | 0.5 **tahmin** | Owner |
| **P2** | OpCo native scaffold (1 marka) | 16 **tahmin** | Agent post-seçim |
| **P2** | Top-100 kuyruk (Exa/MCP; sourced+pending only) | 8 **tahmin** | Agent monthly |
| **P2** | Canva OAuth → CANVA:ON deneme | 2 **tahmin** | Owner OAuth |

Toplam owner-kritik P0: **~5 saat tahmin**. Agent P1 (blocked kalemler hariç, cron+rapor+assess): **~2–4 saat/koşum tahmin**.

## 5) Açık PR’lar
| # | Durum | Başlık | URL |
|---|---|---|---|
| **628** | **DRAFT** | Claude Code güvenlik uyarıları — Cursor eşdeğerleri | https://github.com/metinduraktr-44/adops-agents/pull/628 |
| **627** | OPEN | build(deps): codeql-action 4.37.9 → 4.39.1 | https://github.com/metinduraktr-44/adops-agents/pull/627 |
| **621** | OPEN | build(deps): actions/setup-python 5 → 7 | https://github.com/metinduraktr-44/adops-agents/pull/621 |

Bu rapor PR: branch `cursor/llm-agency-research-loop-50e1` → `main` (aşağı footer’da URL). Merge **yok**.

## 6) Risk / K-003
- 🚩 900B prompt / uydurma top-100 / secret minting → **yapılmadı** (K-003)
- 🚩 Security MODE=ASSESS-ONLY — live remediate yok; IMPLEMENT owner onayı
- 🚩 MCP security catalog default OFF
- 🚩 Domain2 TF apply — credential olmadan apply yok
- 🚩 ANTHROPIC_API_KEY yoksa makale iskelet
- 🚩 F5 kapı kriterleri 2026-09-30’u geçti; gelir kanalları checkbox açık (`docs/GELIR-MODELI-TAKIP.md`)
- 🚩 Unverified uzman listesi yayınlama = human gate
- 🚩 Aynı branch’te ikinci ajan — rapor path izole; rebase gerekebilir
- ✅ paste Claude Code **İPTAL** · validate/cron 2026-11-03 yeşil

### Hızlı URL
| Kaynak | Yol |
|---|---|
| Main | https://github.com/metinduraktr-44/adops-agents |
| MCP | https://cursor.com/docs/context/mcp |
| LLM env | `docs/LLM-ENV.md` |
| Security / LATOS / Creative | `SECURITY_STATE.md` · `LATOS_STATE.md` · `STATE.md` |
| Observability IaC | `infra/observability/terraform/` |
| Yol haritası | `docs/YOL-HARITASI.md` |

⏱️[2026-11-03T11:45:26Z→2026-11-03T11:46:30Z] 🔍[GEÇTİ] 📚[tek sayfa 2026-11-03; adam-saat band; merge yok] 🔗[prev RAPOR-TEK-SAYFA-2026-09-02 used]
