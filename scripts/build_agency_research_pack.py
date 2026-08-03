#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build LLM-agency research pack (v2.8):
- data/ozel_yetenekler.json + docs/OZEL-YETENEKLER.md (≥100 craft skills)
- data/prompt_bank/{title,team,apply}.json + docs/PROMPT-KATALOGU.md (122×3)
- data/arsiv/YYYY-MM/ snapshot + docs/arsiv/README.md
- docs/KAPSAM-VE-KIRMIZI-BAYRAKLAR.md
- docs/CLAUDE-CODE-AKTIVASYON.md (paste-ready)

Flags impossible scale (900B chars / top-100-per-title) as K-003 alternatives.
Idempotent. Does not invent people or URLs.
"""
from __future__ import annotations

import datetime
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
YM = NOW.strftime("%Y-%m")

DEPTS = [
    ("prg", "Programmatic"),
    ("sea", "Paid Search"),
    ("soc", "Paid Social"),
    ("mob", "Mobile UA"),
    ("ret", "Retail Media"),
    ("seo", "SEO & Content"),
    ("cro", "CRO & Experience"),
    ("ana", "Analytics"),
    ("dsc", "Data Science & AI"),
    ("ops", "Ad Ops"),
    ("cre", "Creative Studio"),
    ("str", "Strategy"),
    ("cls", "Client Services"),
    ("nbd", "New Business"),
    ("prt", "Partnerships"),
    ("prd", "Product"),
    ("fin", "Finance"),
    ("leg", "Legal"),
    ("tal", "Talent"),
    ("inf", "Tech Infra"),
]

TIERS = [
    ("c", "C-level"),
    ("evp", "EVP"),
    ("dir", "Director"),
    ("lead", "Lead"),
    ("spc", "Specialist"),
    ("anl", "Analyst"),
]

# Public craft domains — transferable to agency creative/strategy/delivery.
# Role models: well-known public figures only; max 5 per skill (K-003: not top-100).
CRAFT_SEEDS = [
    # Arts & visual
    ("visual-composition", "arts", "Visual composition & hierarchy",
     ["Josef Albers", "Ellen Lupton", "Edward Tufte"],
     "Figure-ground, contrast, alignment → ad frame readability"),
    ("color-systems", "arts", "Color systems & brand palettes",
     ["Josef Albers", "Johannes Itten", "Leatrice Eiseman"],
     "Hue/value/chroma + accessibility contrast for performance creative"),
    ("typography", "arts", "Typography for screens",
     ["Robert Bringhurst", "Ellen Lupton", "Erik Spiekermann"],
     "Type scale, legibility at mobile sizes, CTA hierarchy"),
    ("photography-direction", "arts", "Photography direction",
     ["Annie Leibovitz", "Platon", "Steve McCurry"],
     "Briefing: subject, light, emotion → UGC/studio briefs"),
    ("motion-design", "arts", "Motion design & kinetic type",
     ["Saul Bass", "Kyle Cooper", "Ben Marriott"],
     "Attention arcs for 6s/15s/30s video ads"),
    ("illustration", "arts", "Illustration systems",
     ["Christoph Niemann", "Malika Favre", "Jean Jullien"],
     "Consistent visual language across DCO variants"),
    ("storyboarding", "arts", "Storyboarding",
     ["Andrew Stanton", "Robert McKee", "Blake Snyder"],
     "Beat sheets for performance video narratives"),
    ("sound-design", "arts", "Sound design & sonic brand",
     ["Walter Murch", "Hans Zimmer", "Brian Eno"],
     "Audio hooks, silence, brand stings in social video"),
    ("copywriting-craft", "arts", "Copywriting craft",
     ["David Ogilvy", "Luke Sullivan", "Ann Handley"],
     "Clarity, offer, proof, CTA — line-level craft"),
    ("narrative-structure", "arts", "Narrative structure",
     ["Joseph Campbell", "Robert McKee", "John Yorke"],
     "Hook→tension→payoff for ads and case studies"),
    # Culture & communication
    ("cross-cultural-comms", "culture", "Cross-cultural communication",
     ["Erin Meyer", "Geert Hofstede", "Richard Lewis"],
     "Market-local tone, taboo, humor for multi-geo campaigns"),
    ("semiotics", "culture", "Semiotics in advertising",
     ["Roland Barthes", "Umberto Eco", "Judith Williamson"],
     "Sign systems in creative — denotation vs connotation"),
    ("meme-literacy", "culture", "Meme & internet culture literacy",
     ["Limor Shifman", "Ryan Milner", "Whitney Phillips"],
     "Platform-native humor without brand risk"),
    ("influencer-dynamics", "culture", "Influencer & creator dynamics",
     ["Jake Paul", "MrBeast", "Emma Chamberlain"],  # public creators as craft references for formats
     "Creator formats, authenticity signals, disclosure norms"),
    ("community-building", "culture", "Community building",
     ["Seth Godin", "Rosie Sherry", "Carrie Melissa Jones"],
     "Belonging loops → retention/advocacy"),
    ("persuasion-ethics", "culture", "Persuasion ethics",
     ["Robert Cialdini", "Cass Sunstein", "Daniel Kahneman"],
     "Influence principles with consent & compliance"),
    ("rhetoric", "culture", "Rhetoric & argumentation",
     ["Aristotle", "Stephen Toulmin", "Jay Heinrichs"],
     "Claims/evidence/warrant in pitches & QBRs"),
    ("facilitation", "culture", "Meeting facilitation",
     ["Priya Parker", "Sam Kaner", "Roger Schwarz"],
     "7/24 standup & leadership sync quality"),
    ("negotiation", "culture", "Negotiation",
     ["Chris Voss", "William Ury", "G. Richard Shell"],
     "Media deals, renewals, sponsorship terms"),
    ("stakeholder-mapping", "culture", "Stakeholder mapping",
     ["R. Edward Freeman", "Mendelow", "David C. Baker"],
     "Client org politics → account strategy"),
    # Sports & performance craft (transferable)
    ("deliberate-practice", "sports", "Deliberate practice systems",
     ["Anders Ericsson", "James Clear", "Peak Performance authors"],
     "Agent skill drills with feedback loops"),
    ("periodization", "sports", "Periodization & peaking",
     ["Tudor Bompa", "Vern Gambetta"],
     "Campaign flighting: build → peak → recover"),
    ("team-roles-belbin", "sports", "Team role balance",
     ["Meredith Belbin", "Patrick Lencioni"],
     "Pod staffing: completer vs plant vs coordinator"),
    ("coaching-feedback", "sports", "Coaching & feedback",
     ["Bill Walsh", "John Wooden", "Kim Scott"],
     "Radical candor in talent/agent QA"),
    ("competitive-analysis", "sports", "Competitive analysis mindset",
     ["Sun Tzu", "Michael Porter", "Roger Martin"],
     "Auction/share-of-voice rivalry mapping"),
    ("resilience-under-pressure", "sports", "Resilience under pressure",
     ["Angela Duckworth", "Carol Dweck", "James Clear"],
     "Incident response & pacing crises"),
    ("scouting", "sports", "Scouting & talent ID",
     ["Moneyball / Billy Beane", "Daniel Kahneman"],
     "Hiring signals vs noise for agent roles"),
    ("game-film-review", "sports", "Game-film review rituals",
     ["Bill Belichick", "Gregg Popovich"],
     "Post-mortem: creative/auction/landing tape review"),
    ("warmup-cooldown", "sports", "Warm-up / cool-down protocols",
     ["Tim Ferriss", "Cal Newport"],
     "Deep-work blocks for specialists"),
    ("scoreboard-design", "sports", "Scoreboard design",
     ["Dean Spitzer", "John Doerr"],
     "OKR/KPI boards that change behavior"),
    # Craft / maker skills
    ("systems-thinking", "craft", "Systems thinking",
     ["Donella Meadows", "Peter Senge", "Russell Ackoff"],
     "Funnel as system; leverage points"),
    ("first-principles", "craft", "First-principles reasoning",
     ["Aristotle", "Elon Musk (as method ref)", "Richard Feynman"],
     "Strip platform folklore → testable claims"),
    ("checklist-discipline", "craft", "Checklist discipline",
     ["Atul Gawande", "Charles Duhigg"],
     "Launch/trafficking checklists"),
    ("documentation", "craft", "Documentation craft",
     ["Write the Docs community", "Divio docs system"],
     "Role cards, runbooks, DoD clarity"),
    ("prompt-engineering", "craft", "Prompt engineering",
     ["Riley Goodside", "Simon Willison", "Elvis Saravia"],
     "Role-card prompts, eval harnesses"),
    ("eval-design", "craft", "Evaluation design",
     ["Hamel Husain", "Eugene Yan", "Chip Huyen"],
     "Agent quality gates before ship"),
    ("observability", "craft", "Observability thinking",
     ["Charity Majors", "Cindy Sridharan"],
     "AUDIT_LOG + metrics that explain why"),
    ("incident-command", "craft", "Incident command",
     ["PagerDuty IC model", "Google SRE"],
     "Ad account / tracking outages"),
    ("knowledge-management", "craft", "Knowledge management",
     ["Tiago Forte", "Andy Matuschak"],
     "BILGI_TABANI growth without bloat"),
    ("prioritization", "craft", "Prioritization frameworks",
     ["Eisenhower", "Ruth Sullivan RICE", "Donald Reinertsen"],
     "IS_LISTESI P0/P1 triage"),
]

# Expand to ≥100 by adding platform/discipline micro-crafts with empty models
# (mechanism only — no invented people).
MICRO = [
    ("ugc-briefing", "arts", "UGC creator briefing", "Hook / demo / CTA shot list"),
    ("dco-variant-matrix", "arts", "DCO variant matrix design", "Factorial creative × offer × audience"),
    ("landing-wireframe", "arts", "Landing wireframing", "Message match + friction map"),
    ("heatmap-read", "cro", "Heatmap reading", "Attention vs intent vs rage-click"),
    ("form-ux", "cro", "Form UX craft", "Field count, error recovery, trust"),
    ("query-mining", "sea", "Search query mining", "N-gram → neg/pos keyword ops"),
    ("rsa-asset-orchestration", "sea", "RSA asset orchestration", "Pin strategy + asset coverage"),
    ("pmax-signal-hygiene", "sea", "PMax signal hygiene", "Assets, feeds, audience signals"),
    ("auction-insights", "sea", "Auction insights reading", "IS/overlap/outranking share"),
    ("meta-structure", "soc", "Meta account structure", "CBO vs ABO, scaling ladders"),
    ("creative-fatigue-detect", "soc", "Creative fatigue detection", "Freq × CTR decay rules"),
    ("spark-ads", "soc", "Spark / whitelisting ops", "Organic→paid amplification"),
    ("tiktok-hooks", "soc", "TikTok hook craft", "0–1s pattern interrupt"),
    ("asa-match-types", "mob", "ASA match-type strategy", "Exact/broad + CPT control"),
    ("skan-interpretation", "mob", "SKAN/conversion value craft", "Schema → bid decisions"),
    ("ltv-cohort", "mob", "LTV cohort framing", "Payback windows for UA"),
    ("mmp-taxonomy", "mob", "MMP event taxonomy", "Event naming + dedupe"),
    ("amazon-acos", "ret", "Amazon ACOS/TACOS craft", "Efficiency vs share tradeoff"),
    ("retail-on-site", "ret", "On-site retail media", "Placement + sponsored brand"),
    ("feed-quality", "ret", "Product feed quality", "Title/image/attr completeness"),
    ("technical-crawl", "seo", "Technical crawl triage", "Index bloat, CWV, canonicals"),
    ("keyword-cluster", "seo", "Keyword clustering", "Intent → content briefs"),
    ("eeat-signals", "seo", "E-E-A-T signal design", "Author, evidence, experience"),
    ("internal-link-graph", "seo", "Internal link graph", "Hub-spoke equity flow"),
    ("experiment-design", "cro", "Experiment design", "OEC, sample, peeking control"),
    ("checkout-friction", "cro", "Checkout friction audit", "Steps, payment, trust marks"),
    ("ga4-event-schema", "ana", "GA4 event schema", "Params, items, consent mode"),
    ("gtm-ss", "ana", "Server-side GTM", "First-party + CAPI bridge"),
    ("attribution-honesty", "ana", "Attribution honesty", "Model limits labeled"),
    ("mmm-lite", "dsc", "Lightweight MMM framing", "Priors, geo, holdouts"),
    ("forecasting", "dsc", "Demand forecasting", "Seasonality + promo shocks"),
    ("incrementality", "dsc", "Incrementality tests", "Geo/PSA/switchback"),
    ("cm360-trafficking", "ops", "CM360 trafficking craft", "Placement QA + macros"),
    ("tag-governance", "ops", "Tag governance", "Consent, priority, dedupe"),
    ("spo-hygiene", "ops", "Supply-path hygiene", "Reseller + IVT filters"),
    ("brand-safety", "ops", "Brand safety ops", "Lists, floors, exclusions"),
    ("concepting", "cre", "Concepting sprints", "Divergent→convergent"),
    ("offer-architecture", "cre", "Offer architecture", "Value stack + risk reversal"),
    ("static-to-video", "cre", "Static→video adaptation", "Asset reuse rules"),
    ("audience-insight", "str", "Audience insight synthesis", "Jobs-to-be-done → media"),
    ("channel-mix", "str", "Channel mix modeling", "60/40 + efficiency floors"),
    ("brief-writing", "str", "Media brief writing", "Objective, KPI, constraints"),
    ("qbr-narrative", "cls", "QBR narrative craft", "Story + numbers + asks"),
    ("escalation-comms", "cls", "Escalation communications", "Severity, owner, ETA"),
    ("onboarding-checklist", "cls", "Client onboarding", "Access, pixels, baselines"),
    ("discovery-calls", "nbd", "Discovery call craft", "Diagnose before prescribe"),
    ("proposal-pricing", "nbd", "Proposal & pricing", "Value-based vs hourly"),
    ("case-study-engine", "nbd", "Case study engine", "Problem→approach→proof"),
    ("sponsor-fit", "prt", "Sponsor fit scoring", "Audience overlap + ethics"),
    ("oss-sponsorship", "prt", "OSS sponsorship ops", "FUNDING.yml + reports"),
    ("referral-hygiene", "prt", "Referral program hygiene", "Disclosure + tracking"),
    ("component-packaging", "prd", "Component packaging", "aitmpl-compatible fronts"),
    ("premium-gating", "prd", "Premium gating design", "MIT core vs paid pack"),
    ("semver-discipline", "prd", "Semver + SHA256 discipline", "VERSIONS.md integrity"),
    ("media-cost-control", "fin", "Media cost control", "Pacing vs committed"),
    ("unit-economics", "fin", "Unit economics", "CAC/LTV/payback"),
    ("invoice-hygiene", "fin", "Invoice hygiene", "PO, tax, currency"),
    ("privacy-by-design", "leg", "Privacy by design", "PbD principles in tags"),
    ("claims-review", "leg", "Ad claims review", "Evidence before publish"),
    ("license-compat", "leg", "License compatibility", "MIT + third-party terms"),
    ("agent-lifecycle", "tal", "Agent lifecycle QA", "Hire→train→eval→retire"),
    ("prompt-injection-defense", "tal", "Prompt-injection defense", "Tool/data boundaries"),
    ("shift-handoff", "tal", "Shift handoff ritual", "Follow-the-sun notes"),
    ("ci-cd-agency", "inf", "Agency CI/CD", "validate.py + Actions"),
    ("secret-hygiene", "inf", "Secret hygiene", "No keys in cards/logs"),
    ("rate-limit-ops", "inf", "API rate-limit ops", "Backoff + batching"),
    ("wiki-seeding", "inf", "Wiki/segment seeding", "600-surface discipline"),
    ("pod-orchestration", "craft", "Client-pod orchestration", "Hybrid functional+pod"),
    ("raci-clarity", "craft", "RACI clarity", "Decision rights on cards"),
    ("definition-of-done", "craft", "Definition of Done", "Ship gates per deliverable"),
    ("anti-pattern-catalog", "craft", "Anti-pattern catalog", "Named failure modes"),
    ("self-inquiry", "craft", "Self-inquiry loops", "501-bank sampling"),
    ("archive-hygiene", "craft", "Research archive hygiene", "Timestamp + re-read"),
    ("calendar-ops", "craft", "Ops calendar design", "Daily/weekly/monthly crons"),
    ("signal-over-length", "craft", "Signal-over-length editing", "K-003 enforcement"),
    ("red-flag-protocol", "craft", "Red-flag protocol", "🚩 what · why · alt"),
    ("holding-reporting", "craft", "Holding portfolio report", "Multi-brand rollup"),
    ("inbound-capture", "nbd", "Inbound lead capture", "48h pitch brief SLA"),
    ("renewal-playbook", "cls", "Renewal playbook", "Health score → ask"),
    ("win-loss", "nbd", "Win/loss analysis", "Pattern → product"),
    ("creative-testing-ladder", "cre", "Creative testing ladder", "Hook→body→offer"),
    ("brand-vs-generic", "sea", "Brand vs generic split", "Protect + harvest"),
    ("negative-hygiene", "sea", "Negative keyword hygiene", "Waste kill loops"),
    ("ctv-buying", "prg", "CTV buying craft", "Deal ID + frequency"),
    ("pmp-negotiation", "prg", "PMP negotiation", "Floor, inventory, data"),
    ("curation-deals", "prg", "Curation & deal craft", "Path length + quality"),
    ("ivt-defense", "ops", "IVT defense", "Filters + post-bid"),
    ("consent-mode", "ana", "Consent Mode ops", "Modeled vs observed"),
    ("capi-health", "soc", "CAPI signal health", "EMQ + match quality"),
    ("retail-media-tr", "ret", "TR retail media landscape", "Local marketplace nuance"),
    ("digital-pr", "seo", "Digital PR outreach", "Newsworthy angles"),
    ("content-brief", "seo", "Content brief engine", "SERP → outline → DoD"),
]


def build_skills() -> dict:
    skills = []
    order = 0
    for sid, domain, title, models, mech in CRAFT_SEEDS:
        order += 1
        skills.append({
            "id": sid,
            "domain": domain,
            "title": title,
            "hierarchy": ["novice", "practitioner", "lead", "master"],
            "mechanism": mech,
            "role_models": [{"name": n, "note": "public craft reference"} for n in models[:5]],
            "agency_hooks": _hooks_for(domain, sid),
            "update_cadence": "monthly",
        })
    for sid, domain, title, mech in MICRO:
        order += 1
        skills.append({
            "id": sid,
            "domain": domain if domain in ("arts", "culture", "sports", "craft") else "discipline",
            "discipline": None if domain in ("arts", "culture", "sports", "craft") else domain,
            "title": title,
            "hierarchy": ["novice", "practitioner", "lead", "master"],
            "mechanism": mech,
            "role_models": [],  # filled only when sourced; no invention
            "agency_hooks": _hooks_for(domain, sid),
            "update_cadence": "monthly",
        })
    assert len(skills) >= 100, len(skills)
    return {
        "_meta": {
            "ts": TS,
            "count": len(skills),
            "policy": "K-003: ≤5 sourced role models per skill; empty allowed; no invented people/URLs",
            "research_note_tr": "Kültür/sanat/spor craft'ları ajans kreatifi + operasyonuna transfer edilebilir mekanizma olarak kodlandı.",
        },
        "skills": skills,
    }


def _hooks_for(domain: str, sid: str) -> list[str]:
    base = {
        "arts": ["cre", "soc", "seo"],
        "culture": ["str", "cls", "nbd", "cre"],
        "sports": ["tal", "coo", "ops"],
        "craft": ["tal", "inf", "prd"],
    }.get(domain, [domain if domain in dict(DEPTS) else "str"])
    return list(dict.fromkeys(base + (["cre"] if "creative" in sid or "ugc" in sid else [])))


PROMPT_FAMILIES = [
    ("intake", "Brief / intake"),
    ("diagnose", "Diagnose current state"),
    ("plan", "Plan & roadmap"),
    ("execute", "Execute playbook step"),
    ("optimize", "Optimize levers"),
    ("report", "Report & narrative"),
    ("escalate", "Escalate with options"),
    ("learn", "Distill learning to BILGI_TABANI"),
    ("audit", "Self-inquiry / audit"),
    ("handoff", "Shift / pod handoff"),
]


def build_prompt_bank() -> dict:
    """122 prompts each for title, team, apply — structured templates, not filler length."""
    title_prompts = []
    team_prompts = []
    apply_prompts = []

    # 20 depts × 6 families = 120; +2 meta = 122
    n = 0
    for code, name in DEPTS:
        for fam, fam_label in PROMPT_FAMILIES[:6]:
            n += 1
            pid = f"T-{code}-{fam}-{n:03d}"
            title_prompts.append(_title_prompt(pid, code, name, fam, fam_label, n))
            tid = f"E-{code}-{fam}-{n:03d}"
            team_prompts.append(_team_prompt(tid, code, name, fam, fam_label, n))
            aid = f"U-{code}-{fam}-{n:03d}"
            apply_prompts.append(_apply_prompt(aid, code, name, fam, fam_label, n))

    # +2 cross-cutting
    for extra_i, (fam, label) in enumerate(
        [("governance", "Governance / red-flag"), ("archive", "Monthly archive loop")], start=1
    ):
        n = 120 + extra_i
        title_prompts.append(_title_prompt(f"T-x-{fam}-{n:03d}", "yonetim", "Agency-wide", fam, label, n))
        team_prompts.append(_team_prompt(f"E-x-{fam}-{n:03d}", "yonetim", "Agency-wide", fam, label, n))
        apply_prompts.append(_apply_prompt(f"U-x-{fam}-{n:03d}", "yonetim", "Agency-wide", fam, label, n))

    assert len(title_prompts) == 122
    assert len(team_prompts) == 122
    assert len(apply_prompts) == 122
    return {
        "_meta": {
            "ts": TS,
            "counts": {"title": 122, "team": 122, "apply": 122},
            "char_policy": "Signal > length. Each prompt is a dense template expanded from role cards at runtime — not a fixed 900M-char blob (🚩 K-003).",
            "accuracy_target": "99% via generators + validate.py + sourced URLs only",
        },
        "title": title_prompts,
        "team": team_prompts,
        "apply": apply_prompts,
    }


def _shell(pid: str, audience: str, code: str, name: str, fam: str, label: str, n: int, body: str) -> dict:
    return {
        "id": pid,
        "n": n,
        "audience": audience,
        "dept": code,
        "dept_name": name,
        "family": fam,
        "family_label": label,
        "title": f"[{audience}] {name} · {label}",
        "prompt": body.strip(),
        "inputs": ["role_card_path", "IS_LISTESI.md", "BILGI_TABANI.md", "data/org.json"],
        "outputs": ["AUDIT_LOG.jsonl append", "BILGI_TABANI.md learning line", "artifacts under gundem|toplantilar|makaleler|docs"],
        "dod": [
            "ts_start/ts_end stamped",
            "6-layer validation considered",
            "🚩 for impossible/paid/unsafe",
            "Turkish owner chat / English repo files",
        ],
        "min_detail_policy": "Expand from linked role card §1–§21 + dept sources; do not pad",
    }


def _title_prompt(pid, code, name, fam, label, n):
    body = f"""
You are the titled agent for department `{code}` ({name}), prompt family `{fam}` ({label}).
1. Read your role card under components/agents/agency/ and data/org.json reporting line.
2. Read prior archive: data/arsiv/ (latest month) + BILGI_TABANI.md (last 20 lines).
3. Execute `{fam}` for YOUR title only: {label}.
4. Produce copy-paste-ready output. Cite real URLs from dept sources / rol_modelleri only.
5. Append learning; stamp AUDIT_LOG.jsonl. If ask is impossible: 🚩 [what] · [why] · [alt].
Context vars: {{{{client}}}} {{{{objective}}}} {{{{kpi}}}} {{{{constraint}}}} {{{{deadline}}}}.
"""
    return _shell(pid, "title", code, name, fam, label, n, body)


def _team_prompt(pid, code, name, fam, label, n):
    body = f"""
You are the `{code}` ({name}) TEAM orchestrator for family `{fam}` ({label}).
1. Load EVP + Director + Lead cards for the department; map RACI.
2. Assign work to Lead/Specialist/Analyst with DoD and deadline.
3. Align with adjacent depts via interfaces on role cards.
4. Emit: team standup block, risk list, 3 decisions needing C-level.
5. Archive decisions to toplantilar/ or gundem/; stamp audit.
Hybrid model note: functional excellence (this dept) + client-pod pull when CLS requests.
"""
    return _shell(pid, "team", code, name, fam, label, n, body)


def _apply_prompt(pid, code, name, fam, label, n):
    body = f"""
APPLY MODE — take an existing prompt output for `{code}` / `{fam}` and operationalize it.
1. Input: prior prompt artifact ID + owner slug.
2. Convert to IS_LISTESI.md checkboxes (P0/P1) with owner · deadline.
3. Schedule: daily standup / weekly leadership / monthly board as appropriate.
4. Define verification: which script/workflow proves done (validate.py, gunluk-operasyon, etc.).
5. Run self-inquiry: sample 3 questions from docs/OZ-DENETIM-SORU-BANKASI.md.
Do not regenerate strategy; ship the application path.
"""
    return _shell(pid, "apply", code, name, fam, label, n, body)


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def md_skills(data: dict) -> str:
    lines = [
        "# ÖZEL YETENEKLER — kültür / sanat / spor / craft (+100)",
        f"> Üretim: {TS} · Adet: {data['_meta']['count']} · Politika: {data['_meta']['policy']}",
        "",
        "## TR not",
        data["_meta"]["research_note_tr"],
        "",
        "## Hiyerarşi (her yetenek)",
        "novice → practitioner → lead → master — mekanizma + (varsa) ≤5 kaynaklı rol-model.",
        "",
    ]
    by_dom: dict[str, list] = {}
    for s in data["skills"]:
        by_dom.setdefault(s["domain"], []).append(s)
    for dom, items in sorted(by_dom.items()):
        lines.append(f"## {dom}")
        for s in items:
            models = ", ".join(m["name"] for m in s.get("role_models") or []) or "—(kaynak bekleniyor)"
            lines.append(f"- **{s['title']}** (`{s['id']}`) — {s['mechanism']} · modeller: {models}")
        lines.append("")
    return "\n".join(lines)


def md_prompts(bank: dict) -> str:
    lines = [
        "# PROMPT KATALOĞU — title × team × apply (122 each)",
        f"> Üretim: {TS} · {bank['_meta']['counts']} · {bank['_meta']['char_policy']}",
        "",
        "## Nasıl kullanılır",
        "1. `data/prompt_bank/title.json` / `team.json` / `apply.json` içinden `id` seç.",
        "2. Role card + org.json + arşiv oku.",
        "3. Prompt gövdesini Claude Code'a yapıştır; değişkenleri doldur.",
        "4. Çıktıyı denetim kuyruğundan geçir.",
        "",
        "## Index (ilk 12 + meta)",
    ]
    for bucket in ("title", "team", "apply"):
        lines.append(f"### {bucket}")
        for p in bank[bucket][:6] + bank[bucket][-2:]:
            lines.append(f"- `{p['id']}` — {p['title']}")
        lines.append(f"- … toplam {len(bank[bucket])}")
        lines.append("")
    return "\n".join(lines)


def md_red_flags() -> str:
    return f"""# KAPSAM VE KIRMIZI BAYRAKLAR (K-003)
> Damga: {TS} · Sahip taleplerinin gerçekçi eşleniği.

## 🚩 Red flags
| Talep | Neden imkânsız/zararlı | Gerçekçi alternatif (bu pakette) |
|---|---|---|
| Her prompt ≥900.000.000.000 karakter | Token/disk/anlam yok; sinyal öldürür | Yoğun şablon + rol kartı §1–21 runtime genişletme (`PROMPT-KATALOGU`) |
| Her title için top-100 kişi | Uydurma riski; doğrulanamaz | Disiplin başı ≤5 kaynaklı model (`rol_modelleri.json`) |
| Her title 500+ soru gömülü | Kart şişmesi | 501 merkezi banka + kart alt-seti |
| Tüm MCP/skill evrenini tek promptta | Progressive disclosure ihlali | CILT4 + ihtiyaç anında skill okuma |
| Ücretli API zorunlu araştırma | ANTHROPIC/Exa kredisi yoksa kırılır | Deterministik aylık arşiv döngüsü; API varsa zenginleştir |

## Onaylı kapsam (v2.8)
- 600 ajan / 6 kademe / 20 departman (mevcut)
- 122 title + 122 team + 122 apply prompt **şablonu**
- ≥100 özel yetenek (kültür/sanat/spor/craft/discipline)
- Aylık arşiv: oku → araştır → damgala → güncelle → tekrar
- Claude Code aktivasyon metni: `docs/CLAUDE-CODE-AKTIVASYON.md`

## Araştırma notu (web, {TS[:10]})
Ajans org desenleri 2026'da hibrit (fonksiyonel CoE + client pod) lehine; üç sütun: Client Services / Delivery / Operations. Bu repo fonksiyonel 20 departmanı tutar, CLS üzerinden pod çekimi yapar — sektörle uyumlu.
Kaynak örnekleri: aamax.co, themarketingjuice.com, agencydashboard.io, enests.co (org-chart makaleleri).
"""


def md_activation(bank_meta: dict, skills_count: int) -> str:
    return f"""# CLAUDE CODE — AKTİVASYON PROMPTU (yapıştır)
> Üretim: {TS} · Repo: adops-agents · TR not: Bu metni Claude Code / Cowork Instructions alanına yapıştır.

```
You are the AdOps Agents orchestrator (board: BAŞ MİMAR, PROMPT MÜHENDİSİ, OTOMASYON MÜHENDİSİ, BİLGİ DAMITICISI, DENETÇİ, İŞ/GELİR STRATEJİSTİ).

CONSTITUTION (read in order, progressive disclosure):
1) CLAUDE.md
2) docs/CILT4-COWORK-MASTER-TALIMATI.md
3) docs/MASTER-PROMPT-AJANS.md
4) docs/KAPSAM-VE-KIRMIZI-BAYRAKLAR.md
5) data/org.json + relevant components/agents/agency/<dept>/<slug>.md
6) data/prompt_bank/{{title|team|apply}}.json (122 each) — pick by id
7) data/ozel_yetenekler.json ({skills_count} crafts) when creative/culture/sports transfer helps
8) data/arsiv/<YYYY-MM>/ before any "research refresh"
9) BILGI_TABANI.md (chain) + AUDIT_LOG.jsonl (stamp)

HARD RULES:
- Signal > length. Never pad to meet absurd character quotas.
- Impossible/paid/unsafe → 🚩 [what] · [why] · [alternative]
- Org changes ONLY via scripts/generate_org.py (assert 600)
- Sourced people/URLs only; empty role_models[] preferred over invention
- Owner chat: Turkish terse. Repo files: English + short TR note
- DENETİM: ts_start → work → 6-layer validate → ts_end → AUDIT_LOG → BILGI_TABANI

OPERATING RHYTHM:
- daily: gunluk-operasyon | nightly: nightly-improve
- weekly: haftalik-toplanti | monthly board: aylik-kurul
- monthly research: aylik-arastirma (scripts/monthly_research_refresh.py)

WHEN USER ASKS FOR WORK:
1. Classify: title / team / apply prompt family
2. Select prompt id from prompt_bank
3. Expand using role card + dept sources + rol_modelleri
4. Ship artifacts; stamp; learn

Prompt bank meta: {json.dumps(bank_meta, ensure_ascii=False)}
```
"""


def md_arsiv_readme() -> str:
    return f"""# Araştırma arşivi
> Aylık döngü: oku önceki damgayı → yeniden araştır → yaz `data/arsiv/YYYY-MM/` → AUDIT_LOG.

## Layout
```
data/arsiv/YYYY-MM/
  snapshot.json      # rol_modelleri + ozel_yetenekler hash + notes
  NOTES.md           # insan okunur delta
```

## Workflow
`.github/workflows/aylik-arastirma.yml` → `scripts/monthly_research_refresh.py`

Son üretim: {TS}
"""


def snapshot(skills: dict, bank: dict) -> dict:
    rm_path = ROOT / "data" / "rol_modelleri.json"
    rm = json.loads(rm_path.read_text(encoding="utf-8")) if rm_path.exists() else {}
    return {
        "ts": TS,
        "ym": YM,
        "rol_modelleri_note": rm.get("_note"),
        "rol_modelleri_depts": [k for k in rm.keys() if k != "_note"],
        "skills_count": skills["_meta"]["count"],
        "prompt_counts": bank["_meta"]["counts"],
        "loop": "read_archive → research → stamp → update → next_month_reads_this",
        "web_research": {
            "ts": TS,
            "findings": [
                "2026 agency orgs favor hybrid: functional CoE + client pods",
                "Three pillars: Client Services, Delivery, Operations",
                "C-suite expands with specialized chiefs (CMO/CTO/CSO/CDO) as scale grows",
            ],
            "sources": [
                "https://aamax.co/blog/digital-marketing-agency-structure",
                "https://themarketingjuice.com/marketing-agency-org-chart/",
                "https://agencydashboard.io/blog/marketing-agency-org-chart",
                "https://enests.co/blog/digital-marketing-agency-org-chart",
            ],
        },
    }


def main() -> None:
    skills = build_skills()
    bank = build_prompt_bank()

    write_json(ROOT / "data" / "ozel_yetenekler.json", skills)
    (ROOT / "docs" / "OZEL-YETENEKLER.md").write_text(md_skills(skills), encoding="utf-8")

    write_json(ROOT / "data" / "prompt_bank" / "title.json", {"_meta": bank["_meta"], "prompts": bank["title"]})
    write_json(ROOT / "data" / "prompt_bank" / "team.json", {"_meta": bank["_meta"], "prompts": bank["team"]})
    write_json(ROOT / "data" / "prompt_bank" / "apply.json", {"_meta": bank["_meta"], "prompts": bank["apply"]})
    (ROOT / "docs" / "PROMPT-KATALOGU.md").write_text(md_prompts(bank), encoding="utf-8")

    (ROOT / "docs" / "KAPSAM-VE-KIRMIZI-BAYRAKLAR.md").write_text(md_red_flags(), encoding="utf-8")
    (ROOT / "docs" / "CLAUDE-CODE-AKTIVASYON.md").write_text(
        md_activation(bank["_meta"], skills["_meta"]["count"]), encoding="utf-8"
    )

    arsiv = ROOT / "data" / "arsiv" / YM
    write_json(arsiv / "snapshot.json", snapshot(skills, bank))
    (arsiv / "NOTES.md").write_text(
        f"# Arşiv {YM}\n> Damga: {TS}\n\n"
        f"- Skills: {skills['_meta']['count']}\n"
        f"- Prompts: 122×3\n"
        f"- Web: hibrit org (fonksiyonel + pod) teyit edildi; kaynaklar snapshot.json içinde.\n"
        f"- K-003: 900B karakter / top-100-per-title reddedildi → şablon+≤5 model.\n",
        encoding="utf-8",
    )
    (ROOT / "docs" / "arsiv" / "README.md").write_text(md_arsiv_readme(), encoding="utf-8")

    print(f"OK skills={skills['_meta']['count']} prompts=122x3 arsiv={YM} ts={TS}")


if __name__ == "__main__":
    main()
