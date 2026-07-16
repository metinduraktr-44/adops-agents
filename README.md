# AdOps Agents 🎯
**Claude Code agents, skills, commands & hooks for performance marketing & programmatic advertising.**

DV360 · CM360 · SA360 · GA4 · Adjust · AppsFlyer · Meta · ASA — a battle-tested component pack for media buyers, growth teams, and agencies running Claude Code.

> Structure is compatible with `claude-code-templates` (aitmpl.com), so components are drop-in. Copy any component into your project's `.claude/` folder, or install with the CLI (see below).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Status](https://img.shields.io/badge/status-beta-orange) ![Nightly](https://img.shields.io/badge/self--improving-nightly-blue)

---

## ⚡ Quick start
```bash
# Option A — copy into your Claude Code project
cp -r components/agents/performance-marketing .claude/agents/

# Option B — reference directly in Claude Code / Cowork / Chat project
# Point your project at this repo and let Claude load the components.
```

## 🧩 What's inside
| Type | Component | Does |
|---|---|---|
| Agent | `campaign-auditor` | Audits live campaigns (structure, tracking, waste) |
| Agent | `programmatic-strategist` | DV360/CM360/SA360 strategy + deal/PMP guidance |
| Agent | `roas-optimizer` | Bid/budget/creative levers to hit ROAS targets |
| Command | `/generate-media-plan` | Builds a channel-split media plan from a brief |
| Command | `/channel-report` | Weekly/monthly channel performance summary |
| Skill | `ga4-analysis` | Auto-activates on GA4 questions; funnel + attribution |
| Hook | `timestamp-audit` | Stamps every edit with UTC time into AUDIT_LOG.jsonl |
| MCP | `supermetrics` | Marketing data connector config template |

## 🌙 Nightly self-improvement (7/24)
A GitHub Actions cron (`.github/workflows/nightly-improve.yml`) runs every night at **00:00 UTC (03:00 Istanbul)**:
**read → distill → produce → validate → timestamp → commit**. Each run appends to `AUDIT_LOG.jsonl` and grows `BILGI_TABANI.md` (cumulative knowledge). Weights don't change — the *knowledge base* does.
> ⚠️ To let the nightly job call an LLM, set repo secret `ANTHROPIC_API_KEY`. This uses paid API credits. Without the key the job still timestamps, validates, and commits — it just skips generation.

## 🔍 Validation (6-layer, mirrors aitmpl)
`scripts/validate.py` + `validate-components.yml` enforce: frontmatter/structure, forbidden/dangerous patterns, and integrity (SHA256 in `VERSIONS.md`). PRs are blocked on failure.

## 💰 Revenue model (how this venture pays)
Open-source traction → monetize like the ecosystem does:
1. **Infra sponsorships** (Neon/Vercel/etc. sponsor popular Claude Code repos — real precedent: ~$5K + referral commissions).
2. **Featured/promoted components** (paid placement).
3. **Referral commissions** on tools you integrate (analytics/attribution vendors).
4. **Premium plugin pack** (advanced agents, sold/licensed).
5. **Inbound lead funnel** to your agency — the highest-value channel for a media expert.

## 🇹🇷 Türkçe özet
Performans pazarlama & programatik reklam için Claude Code bileşen paketi. Bileşenleri `.claude/` altına kopyala. Her gece kendini besleyen döngü (bilgi tabanı büyür, model değişmez), 6 katmanlı doğrulama, ve açık kaynak → sponsorluk/referral/ajans inbound gelir modeli.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md). License: [MIT](LICENSE).
