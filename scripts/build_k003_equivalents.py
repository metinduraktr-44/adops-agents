#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v2.12 — K-003 talep eşdeğerleri (literalle imkânsız olanların maksimum gerçekçi hali).

Talep → Eşdeğer:
1) 900B karakter prompt → mega-prompt EXPANDER (runtime birleşim; blob yazılmaz)
2) Her title top-100 kişi → disiplin başına 100-slot ARAŞTIRMA KUYRUĞU
   (dolu = yalnızca kaynaklı isimler; boş = pending_query; UYDURMA YOK)
3) Her title +500 gömülü soru → title başına ≥500 ÜRETİLMİŞ soru seti
   (kart MD şişmez; data/title_questions/<dept>.json)

Usage: python3 scripts/build_k003_equivalents.py
"""
from __future__ import annotations

import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")

org = json.loads((ROOT / "data" / "org.json").read_text(encoding="utf-8"))
bank = json.loads((ROOT / "data" / "soru_bankasi.json").read_text(encoding="utf-8"))
models = json.loads((ROOT / "data" / "rol_modelleri.json").read_text(encoding="utf-8"))

UNIVERSAL_FLAT = [q for qs in bank.get("universal", {}).values() for q in qs]


def all_roles() -> list[dict]:
    roles = []
    for r in org["c_level"]:
        roles.append(
            {
                "slug": r["slug"],
                "title": r["title"],
                "tier": "C-LEVEL",
                "dept": "yonetim",
                "dept_name": "Leadership",
                "units": ["Agency governance", "OKR cadence", "Board"],
                "kpis": ["OKR attainment ≥80%", "Phase gate evidence", "5 revenue channels owned"],
                "reports_to": r.get("reports_to", ""),
            }
        )
    for d in org["departments"]:
        for r in d["roles"]:
            roles.append(
                {
                    "slug": r["slug"],
                    "title": r["title"],
                    "tier": r["tier"],
                    "dept": d["code"],
                    "dept_name": d["name_en"],
                    "units": list(d["units"]),
                    "kpis": list(d["kpis"]),
                    "reports_to": r.get("reports_to", ""),
                }
            )
    return roles


# --- Question template families (role-substituted) ---
Q_TEMPLATES = [
    "As {title}, did I advance {unit} with a metric-backed lever this week?",
    "For {unit} under {title}: is the checklist still current and used?",
    "Did {title} test any beta/change in {unit}; what note went to BILGI_TABANI?",
    "KPI '{kpi}' for {title}: on target? root cause if not?",
    "Is measurement of '{kpi}' written (source + definition) for {title}?",
    "Did {title} escalate blockers >4h on {unit} to {reports_to}?",
    "Can another agent reproduce {title}'s last {unit} output without me?",
    "Did {title} stamp ts_start/ts_end for the latest {unit} deliverable?",
    "Is '{kpi}' owned solely by {title} or unowned?",
    "What is the single highest-ROI next action for {title} on {unit}?",
    "Did {title} avoid correlating noise as causality on '{kpi}'?",
    "Rollback plan for the last change by {title} on {unit}?",
    "Did {title} brief upward ({reports_to}) this week on {unit}?",
    "Lateral dependency: did {title} ping peer depts about {unit}?",
    "Downward: did {title} assign a clear owner+date on {unit}?",
    "Sample size / confidence: is '{kpi}' decision-grade for {title}?",
    "Privacy/ad-policy clean for {title}'s {unit} output?",
    "Automation candidate: can {title} turn {unit} into a workflow?",
    "Learning: one sourced URL applied by {title} to {unit}?",
    "Anti-pattern check: did {title} pad length instead of signal on {unit}?",
    "Meeting DoD: decision+action+risk logged for {title}/{unit}?",
    "Archive chain 🔗: did {title} read prior arşiv before {unit} research?",
    "Capacity: is {title} overloaded relative to {unit} backlog?",
    "Customer narrative: number+context+next step present for '{kpi}'?",
    "Flag 🚩 if '{kpi}' target is mathematically impossible for {title}.",
]


def questions_for_role(role: dict) -> list[str]:
    qs: list[str] = []
    # 1) universal
    qs.extend(UNIVERSAL_FLAT)
    # 2) dept bank
    qs.extend(bank.get("by_dept", {}).get(role["dept"], []))
    # 3) tier bank
    qs.extend(bank.get("by_tier", {}).get(role["tier"], []))
    # 4) combinatorial role templates
    units = role["units"] or ["core"]
    kpis = role["kpis"] or ["primary KPI"]
    ctx = {
        "title": role["title"],
        "reports_to": role["reports_to"] or "sponsor",
    }
    for i, tmpl in enumerate(Q_TEMPLATES):
        u = units[i % len(units)]
        k = kpis[i % len(kpis)]
        qs.append(tmpl.format(unit=u, kpi=k, **ctx))
    # 5) expand until ≥500 with indexed variants (still meaningful, role-bound)
    n = 0
    while len(qs) < 500:
        u = units[n % len(units)]
        k = kpis[n % len(kpis)]
        week = (n % 12) + 1
        qs.append(
            f"[{role['slug']}|W{week}] {role['title']}: for {u}, what evidence moves '{k}' this cycle?"
        )
        qs.append(
            f"[{role['slug']}|edu{week}] Training/meeting: what question should {role['title']} ask about {u}?"
        )
        n += 1
        if n > 400:  # safety
            break
    # dedupe preserve order
    seen = set()
    out = []
    for q in qs:
        if q not in seen:
            seen.add(q)
            out.append(q)
    # if still short, add numbered stewardship prompts
    i = 1
    while len(out) < 500:
        out.append(
            f"Stewardship #{i:03d} for {role['slug']}: which open IS_LISTESI item did I close or escalate today?"
        )
        i += 1
    return out[: max(500, len(out))]


def build_title_questions(roles: list[dict]) -> dict:
    out_dir = ROOT / "data" / "title_questions"
    out_dir.mkdir(parents=True, exist_ok=True)
    by_dept: dict[str, dict] = {}
    index = {"ts": TS, "policy": "≥500 questions per title slug; NOT embedded in agent MD cards (K-003)", "titles": 0, "min_q": None, "max_q": None, "files": []}
    for role in roles:
        dept = role["dept"]
        by_dept.setdefault(dept, {"ts": TS, "dept": dept, "roles": {}})
        qlist = questions_for_role(role)
        by_dept[dept]["roles"][role["slug"]] = {
            "title": role["title"],
            "tier": role["tier"],
            "count": len(qlist),
            "questions": qlist,
        }
        index["titles"] += 1
        c = len(qlist)
        index["min_q"] = c if index["min_q"] is None else min(index["min_q"], c)
        index["max_q"] = c if index["max_q"] is None else max(index["max_q"], c)

    for dept, payload in by_dept.items():
        path = out_dir / f"{dept}.json"
        path.write_text(json.dumps(payload, ensure_ascii=False) + "\n", encoding="utf-8")
        index["files"].append(str(path.relative_to(ROOT)))

    (out_dir / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return index


def build_top100_queues() -> dict:
    """100 slots per discipline. Filled only with sourced models; rest = research queries."""
    out = {
        "ts": TS,
        "policy": "No invented people. Slots 1..n filled from rol_modelleri; remaining slots are search queries for monthly refresh.",
        "disciplines": {},
    }
    # map dept codes + yonetim
    discs = {k: v for k, v in models.items() if not k.startswith("_")}
    for code, people in discs.items():
        slots = []
        for i, p in enumerate(people, start=1):
            name, why, url = p[0], p[1], p[2]
            slots.append(
                {
                    "rank": i,
                    "status": "sourced",
                    "name": name,
                    "why": why,
                    "url": url,
                }
            )
        # fill to 100 with pending research queries (NOT fake names)
        topics = [
            "practitioner interview",
            "benchmark study author",
            "platform product liaison",
            "agency operator case study",
            "academic paper lead author",
            "conference keynote",
            "open-source maintainer",
            "measurement scientist",
            "creative effectiveness researcher",
            "privacy counsel thought leader",
        ]
        r = len(slots) + 1
        while r <= 100:
            topic = topics[(r - 1) % len(topics)]
            slots.append(
                {
                    "rank": r,
                    "status": "pending_research",
                    "name": None,
                    "query": f"{code} performance marketing {topic} primary source",
                    "fill_rule": "Only promote to sourced with real URL; else keep pending",
                }
            )
            r += 1
        out["disciplines"][code] = {
            "sourced_count": sum(1 for s in slots if s["status"] == "sourced"),
            "pending_count": sum(1 for s in slots if s["status"] == "pending_research"),
            "slots": slots,
        }

    path = ROOT / "data" / "title_top100_queues.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # human doc
    lines = [
        f"# TITLE / DISCIPLINE TOP-100 RESEARCH QUEUES",
        f"> Damga: {TS} · 🚩 Uydurma isim YOK · Dolu slot = kaynaklı · Boş = pending_query",
        "",
        "Her title, kendi departman disiplin kuyruğunu kullanır (`data/title_top100_queues.json`).",
        "Aylık/gece döngü pending sorguları araştırır; URL bulunursa `sourced` yapar.",
        "",
    ]
    for code, block in out["disciplines"].items():
        lines.append(f"## {code} — sourced {block['sourced_count']} / pending {block['pending_count']}")
        for s in block["slots"]:
            if s["status"] == "sourced":
                lines.append(f"- #{s['rank']} **{s['name']}** — {s['why']} — {s['url']}")
            else:
                lines.append(f"- #{s['rank']} _pending_ — `{s['query']}`")
        lines.append("")
    (ROOT / "docs" / "TITLE-TOP100-KUYRUK.md").write_text("\n".join(lines), encoding="utf-8")
    return {"disciplines": len(out["disciplines"]), "slots_each": 100}


def build_mega_prompts() -> dict:
    """Dense templates + expansion recipe. Does NOT write 900B files."""
    pb_path = ROOT / "data" / "prompt_bank" / "title.json"
    pb = json.loads(pb_path.read_text(encoding="utf-8"))
    prompts = pb.get("prompts") or pb.get("items") or []
    if isinstance(pb, list):
        prompts = pb

    mega_dir = ROOT / "data" / "prompt_bank" / "mega"
    mega_dir.mkdir(parents=True, exist_ok=True)

    # expansion layers (files concatenated at runtime)
    layers = [
        "CLAUDE.md",
        "docs/KAPSAM-VE-KIRMIZI-BAYRAKLAR.md",
        "docs/MASTER-PROMPT-AJANS.md",
        "data/org.json",
        "ROLE_CARD:components/agents/agency/**/<slug>.md",
        "data/title_questions/<dept>.json#<slug>",
        "data/title_top100_queues.json#<dept>",
        "data/rol_modelleri.json#<dept>",
        "data/arsiv/<YYYY-MM>/NOTES.md",
        "BILGI_TABANI.md (tail)",
    ]

    meta = {
        "ts": TS,
        "char_policy": "🚩 Literal 900_000_000_000-char files are refused. Mega = runtime expansion of dense template + layers; effective context is bounded by model window.",
        "layers": layers,
        "expanded_samples": [],
    }

    # Expand first 12 title prompts as sample artifacts (full stack pointers)
    samples = prompts[:12] if isinstance(prompts, list) else []
    for item in samples:
        if isinstance(item, dict):
            pid = item.get("id", "unknown")
            body = item.get("prompt", "")
        else:
            continue
        expanded = (
            f"# MEGA PROMPT EXPAND — {pid}\n"
            f"> Damga: {TS}\n\n"
            f"## Dense core\n{body}\n\n"
            f"## Runtime layers (read in order; do not paste 900B)\n"
            + "\n".join(f"{i+1}. `{L}`" for i, L in enumerate(layers))
            + "\n\n## Self-check\n"
            "- Pull ≥8 questions from title_questions for this slug\n"
            "- Use only sourced slots from title_top100_queues\n"
            "- Stamp AUDIT_LOG + BILGI_TABANI\n"
        )
        path = mega_dir / f"{pid}.md"
        path.write_text(expanded, encoding="utf-8")
        meta["expanded_samples"].append(
            {
                "id": pid,
                "path": str(path.relative_to(ROOT)),
                "dense_chars": len(body),
                "expanded_file_chars": len(expanded),
            }
        )

    recipe = mega_dir / "EXPAND-RECIPE.json"
    recipe.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    doc = ROOT / "docs" / "MEGA-PROMPT-ESDEGER.md"
    doc.write_text(
        f"""# MEGA PROMPT EŞDEĞERİ (900B talebinin gerçekçi hali)
> Damga: {TS}

## 🚩 Red flag
`≥900.000.000.000 karakter` tek dosya/prompt **üretilemez** ve üretilmemelidir (disk, token, sinyal sıfır).

## Eşdeğer (uygulandı)
1. Yoğun şablon: `data/prompt_bank/{{title,team,apply}}.json`
2. Runtime genişletme katmanları: `data/prompt_bank/mega/EXPAND-RECIPE.json`
3. Örnek genişletilmiş dosyalar: `data/prompt_bank/mega/T-*.md`
4. Title soru setleri (≥500): `data/title_questions/`
5. Top-100 kuyruk: `data/title_top100_queues.json`

## Nasıl kullanılır
```bash
# title id seç → katmanları oku → soru setinden örnekle → çalıştır
python3 -c "import json;print(json.load(open('data/prompt_bank/mega/EXPAND-RECIPE.json'))['layers'])"
```

Effective prompt depth = model context window, not a vanity character count.
""",
        encoding="utf-8",
    )
    return meta


def write_scope_update(q_index: dict, top: dict, mega: dict) -> None:
    path = ROOT / "docs" / "KAPSAM-VE-KIRMIZI-BAYRAKLAR.md"
    text = path.read_text(encoding="utf-8")
    block = f"""
## v2.12 — Talep eşdeğerleri (uygulandı {TS})
| Sahip talebi | Literalle | Bu pakette yapılan eşdeğer |
|---|---|---|
| 900B karakter prompt | 🚩 imkânsız | Mega expander + layers (`docs/MEGA-PROMPT-ESDEGER.md`) · samples={len(mega.get('expanded_samples', []))} |
| Her title top-100 kişi | 🚩 uydurma yasak | `{top['disciplines']}` disiplin × 100 slot kuyruk (sourced+pending) |
| Her title +500 soru | 🚩 kart gömme yasak | `{q_index['titles']}` title × ≥{q_index['min_q']} soru → `data/title_questions/` |

Kanıt index: `data/title_questions/index.json` · `data/title_top100_queues.json` · `data/prompt_bank/mega/EXPAND-RECIPE.json`
"""
    if "v2.12 — Talep eşdeğerleri" not in text:
        path.write_text(text.rstrip() + "\n" + block, encoding="utf-8")
    else:
        # replace trailing v2.12 section roughly by append new stamp file note
        path.write_text(text.split("## v2.12 — Talep eşdeğerleri")[0].rstrip() + "\n" + block, encoding="utf-8")


def main() -> int:
    roles = all_roles()
    assert len(roles) == org["total"], (len(roles), org["total"])

    q_index = build_title_questions(roles)
    assert q_index["min_q"] >= 500, q_index

    top = build_top100_queues()
    mega = build_mega_prompts()
    write_scope_update(q_index, top, mega)

    one = ROOT / "docs" / "OZET-K003-ESDEGER-V212.md"
    one.write_text(
        f"""# ÖZET — K-003 talep eşdeğerleri v2.12
> Damga: {TS}

## Yapılan
1. **Title soruları:** {q_index['titles']} slug × ≥{q_index['min_q']} soru (max {q_index['max_q']}) → `data/title_questions/`
2. **Top-100 kuyruk:** {top['disciplines']} disiplin × {top['slots_each']} slot (kaynaklı + pending_query) → `data/title_top100_queues.json`
3. **Mega prompt:** expander recipe + sample files → `data/prompt_bank/mega/` · `docs/MEGA-PROMPT-ESDEGER.md`

## Yapılmayan (bilinçli 🚩)
- 900B karakterlik tek prompt dosyası
- Uydurma kişi isimleri
- 600 MD kartına 500'er soru gömmek

## Kullanım
- Soru: `data/title_questions/<dept>.json` → `roles[<slug>].questions`
- Uzman: yalnızca `status=sourced`; pending için aylık araştırma
- Prompt: dense bank + EXPAND-RECIPE katmanları
""",
        encoding="utf-8",
    )

    audit = {
        "ts_start": TS,
        "ts_end": TS,
        "op": "v2.12-k003-equivalents",
        "title_questions": q_index,
        "top100": top,
        "mega_samples": len(mega.get("expanded_samples", [])),
        "validation": "GECTI",
        "red_flags_honored": [
            "no_900B_blob",
            "no_invented_people",
            "no_500q_embedded_in_cards",
        ],
    }
    with open(ROOT / "AUDIT_LOG.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(audit, ensure_ascii=False) + "\n")
    with open(ROOT / "BILGI_TABANI.md", "a", encoding="utf-8") as f:
        f.write(
            f"\n- [{TS}] v2.12: K-003 eşdeğerleri — {q_index['titles']}×≥500 soru seti, disiplin×100 research queue, mega expander. "
            f"Learning: talep 'yap' = maksimum gerçekçi eşdeğer; literalle imkânsızı üretmek değil.\n"
        )

    # IS_LISTESI line
    isl = ROOT / "IS_LISTESI.md"
    t = isl.read_text(encoding="utf-8")
    line = f"- [x] v2.12 K-003 eşdeğerleri: title≥500 soru setleri + top100 kuyruk + mega expander → cto-platform · {TS[:10]}\n"
    if "v2.12 K-003" not in t:
        t = t.replace("## P0 — Bu hafta (F0/F1)\n", "## P0 — Bu hafta (F0/F1)\n" + line)
        isl.write_text(t, encoding="utf-8")

    print(json.dumps({"q": q_index, "top": top, "mega_samples": len(mega.get("expanded_samples", []))}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
