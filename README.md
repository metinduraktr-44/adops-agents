# AdOps Agents 🎯 — a 600-agent AI Agency for Performance Marketing
**Claude Code agents, skills, commands & hooks for performance marketing & programmatic advertising — organized as a full 7/24 AI agency.**

DV360 · CM360 · SA360 · GA4 · Adjust · AppsFlyer · Meta · TikTok · ASA · Amazon Ads — a battle-tested component pack for media buyers, growth teams, and agencies running Claude Code.

> Structure is compatible with `claude-code-templates` (aitmpl.com), so components are drop-in. Copy any component into your project's `.claude/` folder.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Status](https://img.shields.io/badge/status-v2%20agency-brightgreen) ![Agents](https://img.shields.io/badge/agents-600-blue) ![Nightly](https://img.shields.io/badge/self--improving-7%2F24-blue)

---

## 🏢 The AI Agency (v2)
This repo is structured as **the org chart of a full-scale performance-marketing & programmatic agency**: **600 agents**, 6 tiers (C-level → EVP → Director → Lead → Specialist → Analyst), **20 departments**, follow-the-sun shift rotation, daily standups, weekly leadership syncs, monthly board meetings — all generated, versioned, and run by cron.

| Surface | What |
|---|---|
| `components/agents/agency/` | **600 agent role cards** (10 C-level + 20 departments) |
| `data/org.json` | Machine-readable org — single source of truth |
| `docs/MASTER-PROMPT-AJANS.md` | Agency constitution — **924 hierarchical headings** |
| `docs/ORG-SEMASI.md` | Org chart (mermaid + headcount table) |
| `docs/YOL-HARITASI.md` | Roadmap with hard deadlines (F0–F5) |
| `docs/GELIR-MODELI-TAKIP.md` | Revenue channel tracker (5 channels) |
| `docs/TOPLANTI-PROTOKOLU.md` | Meeting protocols & minute templates |
| `IS_LISTESI.md` | Live work list, re-prioritized daily |
| `gundem/` · `toplantilar/` · `makaleler/` | Daily standups, meeting minutes, daily articles |

**Departments:** Programmatic · Paid Search · Paid Social · Mobile UA · Retail Media · SEO & Content · CRO · Analytics & Measurement · Data Science & AI · Ad Ops · Creative Studio · Strategy · Client Services · New Business · Partnerships · Product/Premium · Finance · Legal · Talent · Tech Infra.

Org changes are made **only** via `scripts/generate_org.py` (asserts exactly 600 agents), docs via `scripts/generate_docs.py`.

## ⚡ Quick start
```bash
# Option A — copy a department into your Claude Code project
cp -r components/agents/agency/programmatic .claude/agents/

# Option B — copy the classic starter pack
cp -r components/agents/performance-marketing .claude/agents/

# Option C — reference directly in Claude Code / Cowork / Chat project
# Point your project at this repo and let Claude load the components.
```

## 🌙 7/24 operating rhythm (all cron, all committed)
| Workflow | When (Istanbul) | Does |
|---|---|---|
| `nightly-improve` | 03:00 daily | read → distill → produce → validate → stamp → commit |
| `gunluk-operasyon` | 07:30 daily | 20-dept standup + work-list re-prioritization + **1 article/day** + tracking |
| `haftalik-toplanti` | Mon 09:00 | leadership sync minutes (C-level + 20 EVPs) |
| `aylik-kurul` | 1st, 09:00 | board meeting: OKR scoring + roadmap phase gates |

Every run appends `AUDIT_LOG.jsonl` and grows `BILGI_TABANI.md` (cumulative knowledge). Weights don't change — the *knowledge base* does.
> ⚠️ To let generation steps call an LLM, set repo secret `ANTHROPIC_API_KEY` (paid API credits). Without it, loops still run deterministically — standups, minutes, work lists, timestamps, validation — articles ship as structured skeletons.

## 🧩 Classic components (v1, still included)
| Type | Component | Does |
|---|---|---|
| Agent | `campaign-auditor` | Audits live campaigns (structure, tracking, waste) |
| Agent | `programmatic-strategist` | DV360/CM360/SA360 strategy + deal/PMP guidance |
| Agent | `roas-optimizer` | Bid/budget/creative levers to hit ROAS targets |
| Command | `/generate-media-plan` | Builds a channel-split media plan from a brief |
| Command | `/gunluk-standup` · `/toplanti-tutanagi` · `/makale-uret` | Agency daily-ops commands (v2) |
| Skill | `ga4-analysis` | Auto-activates on GA4 questions; funnel + attribution |
| Hook | `timestamp-audit` | Stamps every edit with UTC time into AUDIT_LOG.jsonl |
| MCP | `supermetrics` | Marketing data connector config template |

## 🔍 Validation (6-layer, mirrors aitmpl)
`scripts/validate.py` + `validate-components.yml` enforce: frontmatter/structure, forbidden/dangerous patterns, and integrity (SHA256 in `VERSIONS.md`). PRs are blocked on failure.

## 💰 Revenue model (how this venture pays)
Open-source traction → monetize like the ecosystem does. Live tracker: [`docs/GELIR-MODELI-TAKIP.md`](docs/GELIR-MODELI-TAKIP.md).
1. **Infra sponsorships** (Neon/Vercel/etc. sponsor popular Claude Code repos — real precedent: ~$5K + referral commissions).
2. **Featured/promoted components** (paid placement, transparently labeled).
3. **Referral commissions** on tools we integrate (analytics/attribution vendors).
4. **Premium plugin pack** (advanced agents, sold/licensed — core stays MIT).
5. **Inbound lead funnel** to the agency — the highest-value channel for a media expert.

**Work with us:** need a performance-marketing / programmatic setup audited or built by this system? Open an issue with the `lead` label or email **metindurak.tr@gmail.com** — a pitch brief comes back within 48h.

## 🇹🇷 Türkçe özet
600 ajanlık, 6 kademeli, 20 departmanlı **AI ajans** olarak yapılandırılmış performans pazarlama bileşen paketi. Günlük standup + iş listesi + makale, haftalık liderlik toplantısı, aylık yönetim kurulu — hepsi cron ile 7/24, her koşum denetim zincirine damgalı. Anayasa: `docs/MASTER-PROMPT-AJANS.md` (924 başlık). Gelir: sponsorluk / öne çıkarma / referral / premium paket / ajansa inbound lead.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md). License: [MIT](LICENSE).
