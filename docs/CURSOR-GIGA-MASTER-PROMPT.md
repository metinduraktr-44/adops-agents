# CURSOR GIGA MASTER PROMPT — Otonom AI Creative Agency Operating System (Canva Dual-Mode)

> Damga: 2026-08-27T00:35:00Z · **In-repo apply** — Claude Code paste İPTAL (K-003).
> Bu belge çok dosyalı bootstrap'un ana referansıdır; tek 900B blob **üretilmez**.

---

## 0 — Amaç

Performance Growth Holding altında **otonom AI creative agency** işletim sistemi kurmak:
- Brief → spec → Canva üretim → QA → arşiv döngüsü
- **Canva Dual-Mode:** `CANVA:BRIEF-ONLY` (varsayılan) ve `CANVA:FULL` (OAuth sonrası)
- Mevcut AdOps pack ile entegrasyon: `org.json`, `prompt_bank`, `skill_agency_registry`, `holding.json`

---

## 0.5 — Bootstrap (minimum uygulandı)

| Artefakt | Konum |
|---|---|
| Master prompt | `docs/CURSOR-GIGA-MASTER-PROMPT.md` (bu dosya) |
| Bootstrap + K-003 | `docs/GIGA-AGENCY-BOOTSTRAP.md` |
| Agency context | `AGENTS.md` |
| Cursor rules | `.cursor/rules/00-agency-core.mdc` … `40-canva-ops.mdc` |
| Commands | `.cursor/commands/*.md` |
| Canva MCP | `.cursor/mcp.json` → `https://mcp.canva.com/mcp` |
| Hooks + spec validate | `.cursor/hooks.json`, `scripts/spec_validate.py` |
| Canva client scaffold | `tools/canva-client/` |
| Klasör ağacı | `CONTEXT/`, `RESEARCH/`, `TASKS/`, `ORG/`, `EXPERTS/`, `SCENARIOS/`, `MATRIX/`, `BRIEFS/`, `CANVA_OPS/`, `QA/`, `ARCHIVE/` |
| Phase tracker | `STATE.md`, `.cursor/plans/master-plan.md` |
| Skills | `.cursor/skills/canva-*`, agency workflow skills |
| Critics | `.cursor/agents/critic-*.md` |

---

## 1 — Canva Dual-Mode

| Mod | Flag (`STATE.md`) | Davranış |
|---|---|---|
| **BRIEF-ONLY** | `CANVA_MODE=BRIEF-ONLY` | Brief/spec/MATRIX yaz; Canva MCP çağırma; export stub |
| **FULL** | `CANVA_MODE=FULL` | OAuth sonrası Canva MCP ile design create/edit/export |

**Kısıtlar:**
- Canva **Autofill** yalnızca Enterprise plan — dokümante et, zorlama yok
- OAuth bu repoda **çalıştırılmaz**; owner Cursor MCP Authorize yapar
- İlk üretimler her zaman `BRIEF-ONLY`

---

## 2 — Dosya yapısı

```
CONTEXT/       — marka, ton, hedef kitle özeti
RESEARCH/      — kaynaklı araştırma notları
TASKS/         — aktif iş kartları
ORG/           — creative pod RACI (org.json'dan türetilmiş)
EXPERTS/       — {title}/ seeded + pending_research (K-003)
SCENARIOS/     — kampanya senaryoları
MATRIX/        — spec matrisleri (boyut × format × varyant)
BRIEFS/        — creative brief'ler
CANVA_OPS/     — Canva job manifestleri
QA/            — critic çıktıları
ARCHIVE/       — tamamlanan paketler
```

---

## 3 — İş akışı (günlük)

1. `/baslat` veya `/devam` → `STATE.md` oku
2. Brief üret (`/brief-uret`) → `BRIEFS/`
3. Spec doğrula (`/spec-dogrula`) → `MATRIX/`, `scripts/spec_validate.py`
4. Canva modu BRIEF-ONLY ise manifest yaz; FULL ise `/canva-uret`
5. Critics (`critic-copy`, `critic-design`, `critic-spec`) → `QA/`
6. `/arsivle` → `ARCHIVE/` + AUDIT_LOG

---

## 4 — Skills (Bölüm 4 B2)

| Skill | Amaç |
|---|---|
| `canva-brief` | Brief şablonu + brand guardrails |
| `canva-design` | Canva MCP design create/edit (FULL mod) |
| `canva-export` | Export format seçimi + manifest |
| `canva-autofill` | Enterprise autofill — 🚩 plan kontrolü |
| `agency-workflow` | Faz döngüsü orchestration |
| `brief-validate` | BRIEFS/ yapısal kontrol |
| `spec-validate` | MATRIX/ + görsel spec hook |
| `expert-research` | EXPERTS/ pending_research kuyruğu |
| `phase-report` | Faz raporu şablonu |
| `archive-cycle` | ARCHIVE/ + audit stamp |

---

## 5 — Experts (K-003)

- `EXPERTS/{title}/` — disiplin başına klasör
- Her klasör: `seed.json` (≤5 **kaynaklı** profil) + `pending_research.json` (100 slot kuyruk)
- Uydurma bio **yasak**; boş slot tercih edilir
- Ana kuyruk: `data/title_top100_queues.json`

**Seed disiplinler (creative):** `cre-evp`, `cre-dir`, `design-figma-lead`, `copy-chief`, `brand-strategist`

---

## 6 — Brand guardrails

- BRIEFS/ ve SCENARIOS/ düzenlenirken `.cursor/rules/10-brand-guardrails.mdc` uygulanır
- Tone, yasaklı iddialar, logo/renk referansı `CONTEXT/brand.md`'den okunur

---

## 7 — Spec validation

- MATRIX/ ve CANVA_OPS/ için `.cursor/rules/20-spec-validation.mdc`
- Hook: `scripts/spec_validate.py` (Pillow opsiyonel; yoksa graceful skip)

---

## 8 — MCP

```json
{
  "mcpServers": {
    "Canva": {
      "url": "https://mcp.canva.com/mcp"
    }
  }
}
```

Owner: Cursor Settings → MCP → Authorize (OAuth). Secret repoya **commit edilmez**.

---

## 9 — Critics (readonly subagents)

| Agent | Odak |
|---|---|
| `critic-copy` | Metin, CTA, compliance |
| `critic-design` | Layout, hierarchy, brand |
| `critic-spec` | MATRIX boyut/format tutarlılığı |

---

## 10 — Komutlar

| Komut | İşlev |
|---|---|
| `/baslat` | Oturum başlat, STATE oku |
| `/devam` | Kaldığı yerden devam |
| `/resume` | EN alias for devam |
| `/faz-raporu` | Faz özeti |
| `/aylik-dongu` | Aylık araştırma + arşiv |
| `/canva-uret` | Canva job (mod kontrollü) |
| `/brief-uret` | Yeni brief |
| `/uzman-guncelle` | EXPERTS pending kuyruk |
| `/spec-dogrula` | Spec validate |
| `/arsivle` | Paket arşivle |

---

## 11 — Entegrasyon (mevcut pack)

- Constitution: `CLAUDE.md`, `docs/KAPSAM-VE-KIRMIZI-BAYRAKLAR.md`
- Org 600: `data/org.json` — creative dept `cre`
- Skill router: `data/skill_agency_registry.json` → family `design-figma`
- Denetim: `AUDIT_LOG.jsonl`, `BILGI_TABANI.md`
- Gate: `python3 scripts/validate.py`

---

## 12 — K-003 uyumu

| Yasak | Alternatif |
|---|---|
| 900B tek dosya | Çok dosyalı bootstrap + mega expander |
| Top-100 uydurma | EXPERTS seed + pending_research |
| Secret mint | Owner OAuth + env dışında |
| Tüm skill live | Family mini-agency routing |

---

## 13 — Yedi fazlı plan

| Faz | Ad | Çıktı |
|---|---|---|
| 0 | Bootstrap | Rules, commands, klasörler, STATE |
| 1 | Context + Brand | `CONTEXT/`, brand guardrails |
| 2 | Experts seed | `EXPERTS/` sourced seeds |
| 3 | Brief pipeline | `BRIEFS/` şablonları |
| 4 | Spec + Matrix | `MATRIX/` validation |
| 5 | Canva BRIEF-ONLY | `CANVA_OPS/` manifest |
| 6 | Canva FULL | OAuth + MCP live |
| 7 | QA + Archive | Critics, `ARCHIVE/` döngüsü |

Detay: `.cursor/plans/master-plan.md`

---

## 14 — Owner P0

1. Canva OAuth — Cursor MCP Authorize
2. Cursor restart — MCP yükle
3. İlk sprint: `CANVA:BRIEF-ONLY` — brief/spec pipeline doğrula
4. FULL moda geçmeden önce brand kit onayı
