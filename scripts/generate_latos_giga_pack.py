#!/usr/bin/env python3
"""Generate LATOS GIGA pack scaffolds (idempotent).

K-003: no 900M-char blob; no invented top-100 experts; progressive expansion via /devam.
Usage:
  python3 scripts/generate_latos_giga_pack.py [--force]
  python3 scripts/generate_latos_giga_pack.py --git-scan
"""
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATE = TS[:10]

SAMPLE_TITLES = [
    "ceo-orchestrator",
    "prg-evp-programmatic",
    "sea-evp-paid-search",
    "cmo-brand",
    "cro-revenue",
    "inf-evp-tech-infra",
]

SAMPLE_TEAMS = ["programmatic", "paid-search", "brand-creative", "revenue-ops"]

SKILLS = [
    ("title-discovery", "Discover and inventory all titles (current + git-deleted + archive)."),
    ("job-card-engine", "Generate and expand job cards with H001..H200 index pattern."),
    ("expert-engine", "Expert queues — sourced seeds + pending_research only."),
    ("talent-engine", "Talent taxonomy and title-to-talent mapping."),
    ("roadmap-engine", "OKR, roadmap, and 7/24 operation workflows."),
    ("prompt-engine", "122-slot prompt index per title/team/execution topic."),
    ("forecast-engine", "Daily forecast workflow with Brier calibration."),
    ("archive-loop", "READ→DELTA→DIFF→WRITE→DIGEST archive evolution."),
]

TALENT_CATEGORIES = [
    ("cognitive", ["critical-thinking", "problem-decomposition", "systems-thinking", "decision-making", "learning-agility"]),
    ("technical", ["data-literacy", "coding-basics", "automation-scripting", "platform-ops", "measurement-design"]),
    ("social", ["negotiation", "stakeholder-management", "cross-cultural-comm", "conflict-resolution", "networking"]),
    ("physical", ["endurance", "stress-regulation", "presentation-stance", "travel-readiness", "workplace-ergonomics"]),
    ("creative", ["creative-writing", "visual-storytelling", "improvisation", "design-thinking", "brand-narrative"]),
    ("management", ["delegation", "coaching", "performance-mgmt", "resource-allocation", "change-leadership"]),
    ("self-management", ["time-blocking", "focus-deep-work", "habit-design", "emotional-regulation", "energy-mgmt"]),
    ("digital", ["ai-literacy", "prompt-engineering", "tool-orchestration", "info-security-hygiene", "collab-platforms"]),
    ("ai-literacy", ["model-selection", "eval-design", "guardrail-design", "agent-orchestration", "human-in-loop"]),
    ("4c", ["creativity", "critical-thinking-4c", "communication", "collaboration"]),
]

DIRS = [
    "CONTEXT/INBOX", "ROSTER", "RESEARCH", "TASKS", "ORG", "JOB_CARDS",
    "EXPERTS", "SKILLS_TALENT", "EXPERTS_TALENT", "ROADMAP", "OPERATIONS",
    "PROMPTS/TITLES", "PROMPTS/TEAMS", "PROMPTS/EXECUTION",
    "FORECASTS", "ARCHIVE", "CALENDAR", "QA", "MEMORY", "REPORTS",
]


def write_if_needed(path: Path, content: str, force: bool) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        existing = path.read_text(encoding="utf-8")
        if existing == content:
            return False
        if len(existing) > len(content) + 200 and "HAND_AUTHORED" in existing:
            return False
    path.write_text(content, encoding="utf-8")
    return True


def load_org_titles() -> list[dict]:
    org = json.loads((ROOT / "data/org.json").read_text(encoding="utf-8"))
    titles: list[dict] = []
    for c in org.get("c_level", []):
        titles.append({
            "slug": c["slug"], "title": c["title"], "dept": "c_level",
            "tier": "C-level", "source": "org.json", "status": "active",
        })
    for dept in org.get("departments", []):
        for role in dept.get("roles", []):
            titles.append({
                "slug": role["slug"], "title": role["title"], "dept": dept["code"],
                "tier": role.get("tier", ""), "source": "org.json", "status": "active",
            })
    return titles


def git_deleted_paths() -> list[dict]:
    results: list[dict] = []
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True, text=True, cwd=ROOT, timeout=10,
        )
        if r.stdout.strip() != "true":
            return results
        log = subprocess.run(
            ["git", "log", "--all", "--diff-filter=D", "--name-only", "--pretty=format:%H|%aI"],
            capture_output=True, text=True, cwd=ROOT, timeout=60,
        )
        current_commit = ""
        for line in log.stdout.splitlines():
            if "|" in line and len(line.split("|")[0]) == 40:
                current_commit, _date = line.split("|", 1)
            elif line.strip():
                low = line.lower()
                if any(k in low for k in ("role", "title", "agent", "org", "card")):
                    results.append({
                        "path": line.strip(),
                        "commit": current_commit[:12],
                        "source": "git-deleted",
                        "status": "deleted-recoverable",
                    })
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        pass
    return results


def skill_md(name: str, desc: str) -> str:
    return f"""---
name: {name}
description: {desc}
---

# {name}

> TR: LATOS skill. Keşfedilmezse inline path kullan.
> Damga: {TS}

## Hybrid rule
If this skill is not discovered after Cursor restart → follow inline steps in
`docs/CURSOR-LATOS-GIGA-MASTER-PROMPT.md` for the same phase. Output paths identical.

## K-003 guardrails
- No 900M-char single prompt; expand via `references/` + `/devam`.
- No invented top-100 experts; `pending_research` + sourced seeds only.
- Human approval gates for restore, publish, self-modification.

## Progressive disclosure
- `references/overview.md` — scope
- `references/workflow.md` — operator steps
- `references/templates.md` — output schemas

## State
Read `LATOS_STATE.md` before each run. Stamp AUDIT_LOG on completion.
"""


def ref_overview(name: str) -> str:
    return f"""# {name} — Overview

> status: scaffold · damga: {TS}

## Purpose
LATOS **{name}** — progressive reference bundle.

## Related
- Master: `docs/CURSOR-LATOS-GIGA-MASTER-PROMPT.md`
- State: `LATOS_STATE.md`
- Generator: `scripts/generate_latos_giga_pack.py`
"""


def ref_workflow(name: str) -> str:
    return f"""# {name} — Workflow

1. Read `LATOS_STATE.md` + `ROSTER/TITLE_INVENTORY.md`
2. Execute phase steps from master prompt
3. Write outputs to canonical paths (see `30-latos-file-structure.mdc`)
4. Run `python3 scripts/qa_check.py` + `citation_check.py`
5. Append AUDIT_LOG.jsonl + BILGI_TABANI.md
6. Stop; owner types `/latos-devam` or `/devam`

Damga: {TS}
"""


def ref_templates(name: str) -> str:
    return f"""# {name} — Templates

## Job card heading (H001 pattern)
```yaml
id: H001
title: Mission alignment
description_min_chars: 200
guidance_min_chars: 200
training_min_chars: 200
status: scaffold
```

## Expert entry
```yaml
name: null
status: pending_research
query: "<discipline> expert primary source URL"
url: null
timestamp: {TS}
```

## Forecast entry
```yaml
claim: "<probabilistic statement>"
confidence: 0.0-1.0
resolution_date: YYYY-MM-DD
brier_slot: pending
```
"""


def title_inventory_md(titles: list[dict], deleted: list[dict]) -> str:
    lines = [
        "# TITLE_INVENTORY — Master List (no skip)",
        "",
        f"> Damga: {TS} · HAND_AUTHORED: generator seed · expand via `/latos-devam`",
        "",
        "## Policy",
        "- **No title skipped** — all 600 org.json slugs listed below.",
        "- Git-deleted paths appended separately; restore requires human approval.",
        "- Job cards expand per title via `job-card-engine` + `/devam`.",
        "",
        f"## Summary",
        f"- Active (org.json): **{len(titles)}**",
        f"- Git-deleted candidates: **{len(deleted)}**",
        "",
        "## Active titles (org.json)",
        "",
        "| slug | title | dept | tier | source | status |",
        "|---|---|---|---|---|---|",
    ]
    for t in titles:
        lines.append(
            f"| `{t['slug']}` | {t['title']} | {t['dept']} | {t.get('tier','')} | {t['source']} | {t['status']} |"
        )
    if deleted:
        lines += ["", "## Git-deleted candidates", "",
                  "| path | commit | source | status |", "|---|---|---|---|"]
        for d in deleted[:50]:
            lines.append(f"| `{d['path']}` | `{d['commit']}` | git-deleted | deleted-recoverable |")
        if len(deleted) > 50:
            lines.append(f"| … | … | … | +{len(deleted)-50} more (run `--git-scan`) |")
    else:
        lines += ["", "## Git-deleted candidates", "",
                  "_No role/title/agent paths found in git delete log, or git unavailable._"]
    lines += ["", "## Expansion queue", "",
              "All slugs without `JOB_CARDS/{slug}/CARD.md` are **pending**. ",
              "Sample cards exist for: " + ", ".join(f"`{s}`" for s in SAMPLE_TITLES)]
    return "\n".join(lines) + "\n"


def job_card_md(slug: str, title: str, dept: str) -> str:
    return f"""# Job Card — {title}

> slug: `{slug}` · dept: `{dept}` · damga: {TS}
> status: **scaffold** · target: 2000+ chars, 200+ headings (progressive via H001..H200)

## Identity
- **Title:** {title}
- **Slug:** {slug}
- **Department:** {dept}
- **Agent persona:** LATOS mini-agency role card

## Mission
Deliver measurable outcomes for {title} within the AdOps agency org (600 agents).
Align daily work to OKR cascade from `ROADMAP/{slug}.md`.

## Responsibilities (scaffold)
1. Execute role-specific workflows per `data/prompt_bank/` and dept board.
2. Maintain job card headings H001–H200 via `/latos-is-karti` + `/devam`.
3. Contribute forecasts to `FORECASTS/{slug}/` (workflow: 200/day target, not one-shot).
4. Escalate blockers >4h to sponsor per `data/org.json`.

## RACI (draft)
| Activity | R | A | C | I |
|---|---|---|---|---|
| Daily ops | {slug} | dept-head | QA | owner |

## KPI (draft)
- Output quality: QA pass rate
- Forecast calibration: Brier trend in `FORECASTS/CALIBRATION.md`
- Prompt coverage: 122-slot index completion

## Tools & skills
- LATOS: `job-card-engine`, `prompt-engine`, `forecast-engine`
- Agency: `data/skill_agency_registry.json`, dept MCP hints

## Escalation
- 🚩 Impossible targets (900M chars, fake top-100) → refuse; use generator
- Unverified experts → human review before publish

## Heading index
See `HEADINGS_INDEX.md` — expand H001..H200 via generator + `/devam`.
"""


def heading_stub(slug: str, n: int) -> str:
    hid = f"H{n:03d}"
    return f"""# {hid} — Heading {n} ({slug})

> status: scaffold · min 200+200+200 chars per heading when expanded

## Description (expand to 200+ chars)
Role-specific guidance block {n} for `{slug}`. Cover mission alignment, stakeholder
context, and measurable outcome. Cite `RESEARCH/{slug}.md` when available.

## Guidance (expand to 200+ chars)
Operator steps: read STATE → pick task from MASTER_TASKS → execute → QA → stamp audit.
Use `/latos-devam` for next heading batch. Parallel agents write to isolated folders.

## Training (expand to 200+ chars)
Learning path: dept questions in `data/title_questions/`, prompt bank slot, expert
queue in `EXPERTS/{slug}/`. Human review required for unverified claims.

Damga: {TS}
"""


def expert_queue_md(slug: str, title: str) -> str:
    return f"""# Expert queue — {title}

> slug: `{slug}` · damga: {TS}
> policy: **no invented names** · mirror `data/title_top100_queues.json`

## Status
- sourced: 0 (seed from dept discipline queue on `/latos-uzman-guncelle`)
- pending_research: 100 slots

## Slots 1–5 (pending_research)
| rank | status | name | query | url |
|---|---|---|---|---|
| 1 | pending_research | null | {slug} domain expert primary source award | null |
| 2 | pending_research | null | {slug} conference keynote primary source | null |
| 3 | pending_research | null | {slug} academic citation lead author | null |
| 4 | pending_research | null | {slug} industry ranking primary source | null |
| 5 | pending_research | null | {slug} open-source maintainer primary source | null |

## Human approval gate
Promote to `sourced` only with URL + timestamp. Else keep `pending_research` or `unverified`.
"""


def prompt_index_md(kind: str, key: str, label: str) -> str:
    lines = [
        f"# Prompt index — {label}",
        "",
        f"> kind: {kind} · key: `{key}` · damga: {TS}",
        "> target: 122 prompts (P001..P122) · 🚩 900M chars/prompt = impossible single output",
        "",
        "## Slots (scaffold P001–P010)",
        "",
    ]
    for i in range(1, 11):
        lines.append(f"- P{i:03d}: scaffold — expand via `/latos-prompt-uret` + `/devam`")
    lines += [
        "",
        "## Expansion",
        f"Full index: `PROMPTS/{kind}/{key}/P001.md` … P122.md via `prompt-engine`.",
        "Cross-ref: `data/prompt_bank/` for agency baseline prompts.",
    ]
    return "\n".join(lines) + "\n"


def context_brief() -> str:
    return f"""# CONTEXT_BRIEF — Repo scan (Faz 0/1)

> Damga: {TS} · generated by `generate_latos_giga_pack.py`

## Repo identity
- **Name:** adops-agents (Performance Growth / AdOps LLM agency pack)
- **Org:** 600 agents in `data/org.json` (assert via `generate_org.py`)
- **Activation:** in-repo (`docs/AKTIVASYON-DURUM.md`); Claude Code paste cancelled

## Key paths scanned
| Area | Path |
|---|---|
| Constitution | `CLAUDE.md`, `docs/CILT4-COWORK-MASTER-TALIMATI.md` |
| Org | `data/org.json`, `components/agents/agency/**` |
| Prompt bank | `data/prompt_bank/` (122×3) |
| Skill agency | `data/skill_agency_registry.json` v2.9 |
| Holding | `data/holding.json` v2.10 |
| Domains | `data/domains/domain_pack.json` |
| Top-100 queues | `data/title_top100_queues.json` (sourced + pending) |
| Security GIGA | coexists — `SECURITY_STATE.md`, `sec-*` commands |
| LATOS GIGA | `LATOS_STATE.md`, `latos-*` commands |

## Operator notes
- Drop prior chat dumps in `CONTEXT/INBOX/`
- Cursor restart after new `.cursor/skills/` 
- Git required for deleted-title recovery (see `ROSTER/TITLE_INVENTORY.md`)
"""


def master_tasks_md() -> str:
    return f"""# MASTER_TASKS — LATOS phased work

> Damga: {TS}

| ID | Phase | Owner | Output | Priority | Status |
|---|---|---|---|---|---|
| T-001 | Faz 0 | LATOS | `.cursor/` bootstrap + LATOS_STATE | P0 | done-scaffold |
| T-002 | Faz 0 | LATOS | CONTEXT/CONTEXT_BRIEF.md | P0 | done-scaffold |
| T-003 | Faz 1 | title-discovery | ROSTER/TITLE_INVENTORY.md (600) | P0 | done-scaffold |
| T-004 | Faz 1 | title-discovery | git deleted scan | P1 | conditional |
| T-005 | Faz 2 | researcher | RESEARCH/_ORG_BEST_PRACTICE.md | P1 | stub |
| T-006 | Faz 3 | architect | ORG/ORG_CHART.md | P1 | scaffold |
| T-007 | Faz 4 | job-card-engine | JOB_CARDS sample ×6 | P0 | done-scaffold |
| T-008 | Faz 4 | job-card-engine | Expand 600 cards via /devam | P2 | queued |
| T-009 | Faz 5 | expert-engine | EXPERTS pending queues | P1 | scaffold |
| T-010 | Faz 6 | talent-engine | SKILLS_TALENT/TALENT_TAXONOMY | P1 | scaffold |
| T-011 | Faz 7 | roadmap-engine | ROADMAP samples | P2 | stub |
| T-012 | Faz 8 | prompt-engine | PROMPTS 122-slot indexes | P2 | scaffold |
| T-013 | Faz 9 | forecast-engine | FORECASTS/CALIBRATION.md | P1 | scaffold |
| T-014 | ongoing | archive-loop | ARCHIVE snapshots | P3 | ready |

## Acceptance
- qa_check.py: no title skip vs inventory
- citation_check.py: experts have URL or unverified flag
- validate.py: GECTI
"""


def org_chart_md(titles: list[dict]) -> str:
    c_level = [t for t in titles if t["dept"] == "c_level"]
    lines = [
        "# ORG_CHART — LATOS scaffold",
        "",
        f"> Damga: {TS} · 600 titles · text tree + optional HTML in ORG/ORG_CHART.html",
        "",
        "## C-Level",
    ]
    for t in c_level:
        lines.append(f"- **{t['title']}** (`{t['slug']}`)")
    lines += ["", "## Departments (headcount summary)", ""]
    depts: dict[str, list] = {}
    for t in titles:
        if t["dept"] != "c_level":
            depts.setdefault(t["dept"], []).append(t)
    for dept, roles in sorted(depts.items()):
        evp = next((r for r in roles if "evp" in r["slug"]), roles[0] if roles else None)
        lines.append(f"- **{dept.upper()}** ({len(roles)} roles) → EVP: `{evp['slug'] if evp else 'n/a'}`")
    lines += [
        "",
        "## HTML panel",
        "Open `ORG/ORG_CHART.html` for interactive scaffold (expand via web-artifacts muadil).",
    ]
    return "\n".join(lines) + "\n"


def talent_taxonomy_md() -> str:
    lines = [
        "# TALENT_TAXONOMY — ~100 skills scaffold",
        "",
        f"> Damga: {TS} · 9 types + 4C · expand to 100 via `/latos-yetenek-guncelle`",
        "",
        "| category | cluster | skill | level scaffold |",
        "|---|---|---|---|",
    ]
    n = 0
    for cat, clusters in TALENT_CATEGORIES:
        for cl in clusters:
            n += 1
            lines.append(f"| {cat} | {cl} | {cl.replace('-', ' ').title()} | L1–L5 TBD |")
    lines += ["", f"**Total scaffold entries:** {n}", "",
              "## Title mapping", "See `SKILLS_TALENT/TITLE_TO_TALENT_MAP.md`"]
    return "\n".join(lines) + "\n"


def forecast_calibration_md() -> str:
    return f"""# FORECAST CALIBRATION

> Damga: {TS} · Tetlock + Brier practices

## Targets (progressive — not one-shot)
- Per title: **200 forecasts/day** workflow via `/latos-tahmin` + Cloud Agent
- 🚩 Claiming 200×600 titles in one commit = impossible

## Brier score reference
- Superforecaster benchmark ~0.166
- General public ~0.259
- Track in `FORECASTS/CALIBRATION.md` after resolutions

## Template (`FORECASTS/{{title}}/YYYY-MM-DD.md`)
```yaml
forecasts:
  - id: F001
    claim: "..."
    probability: 0.65
    resolve_by: {DATE}
    status: open
    source_url: required-or-unverified
```

## Recalibration gate
If Brier worsens 2 weeks → human review + adjust base rates.
"""


def qa_report_faz0() -> str:
    return f"""# QA_REPORT — Faz 0 Bootstrap

> Damga: {TS}

## Checks
| Check | Result |
|---|---|
| Title inventory (600) | scaffold |
| Sample job cards | {len(SAMPLE_TITLES)} |
| Expert queues pending only | yes |
| 900M prompt claim | 🚩 refused (K-003) |
| Security coexistence | merged hooks |
| validate.py | run post-commit |

## Next
1. Cursor restart
2. `/latos-devam` → Faz 1 git scan deepen
3. Human review unverified slots
"""


def latos_state_md(titles_count: int, deleted_count: int) -> str:
    return f"""# LATOS_STATE — Phase Tracker

> Damga: {TS} · preferred state file for LATOS GIGA pack

## Current phase
**Faz 0–1 scaffold complete** — Bootstrap + Ingestion + Title inventory seed.

## Metrics
| Metric | Value |
|---|---|
| Titles (org.json) | {titles_count} |
| Git-deleted candidates | {deleted_count} |
| Sample job cards | {len(SAMPLE_TITLES)} |
| Expert policy | pending_research only |
| Prompt target | 122/title (scaffold) |
| Forecast target | 200/day/title (workflow) |

## Active escalations
- None

## Next step
`/latos-devam` → expand job cards batch; run `--git-scan` for deleted titles.

## Coexistence
| Pack | State file |
|---|---|
| LATOS GIGA | `LATOS_STATE.md` (this file) |
| Security GIGA | `SECURITY_STATE.md` |
| Creative Canva | branch-specific |

## Human approval gates
- git restore deleted files
- publish verified expert lists
- flip Security MODE to IMPLEMENT
"""


def generate_skills(force: bool) -> int:
    count = 0
    for name, desc in SKILLS:
        base = ROOT / ".cursor/skills" / name
        if write_if_needed(base / "SKILL.md", skill_md(name, desc), force):
            count += 1
        for ref, fn in [
            ("overview.md", lambda n=name: ref_overview(n)),
            ("workflow.md", lambda n=name: ref_workflow(n)),
            ("templates.md", lambda n=name: ref_templates(n)),
        ]:
            if write_if_needed(base / "references" / ref, fn(), force):
                count += 1
    return count


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--git-scan", action="store_true", help="Run git deleted-file scan")
    args = ap.parse_args()
    force = args.force

    written = 0
    for d in DIRS:
        (ROOT / d).mkdir(parents=True, exist_ok=True)

    titles = load_org_titles()
    deleted = git_deleted_paths() if (args.git_scan or True) else []

    files = {
        "CONTEXT/CONTEXT_BRIEF.md": context_brief(),
        "ROSTER/TITLE_INVENTORY.md": title_inventory_md(titles, deleted),
        "TASKS/MASTER_TASKS.md": master_tasks_md(),
        "ORG/ORG_CHART.md": org_chart_md(titles),
        "SKILLS_TALENT/TALENT_TAXONOMY.md": talent_taxonomy_md(),
        "SKILLS_TALENT/TITLE_TO_TALENT_MAP.md": f"# TITLE_TO_TALENT_MAP\n\n> Damga: {TS}\n\nScaffold — map each title slug to 3–5 talent clusters via `/latos-yetenek-guncelle`.\n",
        "FORECASTS/CALIBRATION.md": forecast_calibration_md(),
        "QA/QA_REPORT_faz0.md": qa_report_faz0(),
        "LATOS_STATE.md": latos_state_md(len(titles), len(deleted)),
        "RESEARCH/_ORG_BEST_PRACTICE.md": f"# Org best practice research\n\n> Damga: {TS} · stub\n\nExpand via `@Web` + URL/timestamp per finding.\n",
        "OPERATIONS/247_WORKFLOWS.md": f"# 7/24 Workflows\n\n> Damga: {TS}\n\nMorning muadil + Cloud Agent automations — scaffold.\n",
        "CALENDAR/EXPERTS_UPDATE.md": f"# Expert update calendar\n\n> Damga: {TS}\n\nMonthly `/latos-aylik-dongu` — READ→DELTA→DIFF→WRITE→DIGEST.\n",
        "MEMORY/LONG_TERM.md": f"# Long-term memory (episodic)\n\n> Damga: {TS}\n\nLessons from forecast/expert/archive loops.\n",
    }
    for path, content in files.items():
        if content and write_if_needed(ROOT / path, content, force):
            written += 1

    # Sample job cards
    title_map = {t["slug"]: t for t in titles}
    for slug in SAMPLE_TITLES:
        t = title_map.get(slug, {"title": slug, "dept": "unknown"})
        base = ROOT / "JOB_CARDS" / slug
        if write_if_needed(base / "CARD.md", job_card_md(slug, t["title"], t["dept"]), force):
            written += 1
        idx_lines = [f"# HEADINGS_INDEX — {slug}", "", f"> Damga: {TS}", "", "| id | file | status |", "|---|---|---|"]
        for n in range(1, 11):
            hid = f"H{n:03d}"
            idx_lines.append(f"| {hid} | {hid}.md | scaffold |")
        idx_lines.append("| H011..H200 | (queued) | expand via /devam |")
        if write_if_needed(base / "HEADINGS_INDEX.md", "\n".join(idx_lines) + "\n", force):
            written += 1
        for n in range(1, 4):
            if write_if_needed(base / f"H{n:03d}.md", heading_stub(slug, n), force):
                written += 1

    # Experts
    for slug in SAMPLE_TITLES:
        t = title_map.get(slug, {"title": slug})
        if write_if_needed(ROOT / "EXPERTS" / slug / f"top100_{DATE}.md", expert_queue_md(slug, t["title"]), force):
            written += 1

    # Prompts
    for slug in SAMPLE_TITLES:
        t = title_map.get(slug, {"title": slug})
        if write_if_needed(ROOT / "PROMPTS/TITLES" / f"{slug}.md", prompt_index_md("TITLES", slug, t["title"]), force):
            written += 1
    for team in SAMPLE_TEAMS:
        if write_if_needed(ROOT / "PROMPTS/TEAMS" / f"{team}.md", prompt_index_md("TEAMS", team, team), force):
            written += 1
    if write_if_needed(ROOT / "PROMPTS/EXECUTION" / "agency-ops.md", prompt_index_md("EXECUTION", "agency-ops", "Agency Operations"), force):
        written += 1

    # Sample forecast
    for slug in SAMPLE_TITLES[:2]:
        fc = f"""# Forecasts — {slug} — {DATE}

> workflow scaffold · target 200/day via `/latos-tahmin`

| id | claim | p | resolve_by | status |
|---|---|---|---|---|
| F001 | Sample forecast slot — replace with grounded claim | 0.55 | {DATE} | open-unverified |

Human review required. Cite source URL or mark unverified.
"""
        if write_if_needed(ROOT / "FORECASTS" / slug / f"{DATE}.md", fc, force):
            written += 1

    # Roadmap samples
    for slug in SAMPLE_TITLES[:3]:
        rm = f"# Roadmap — {slug}\n\n> Damga: {TS}\n\n## Q3 North Star\nScaffold OKR — expand via `/latos-roadmap`.\n"
        if write_if_needed(ROOT / "ROADMAP" / f"{slug}.md", rm, force):
            written += 1

    written += generate_skills(force)

    print(json.dumps({
        "ts": TS,
        "written_or_updated": written,
        "titles": len(titles),
        "git_deleted": len(deleted),
        "sample_cards": len(SAMPLE_TITLES),
        "skills": len(SKILLS),
    }, indent=2))


if __name__ == "__main__":
    main()
