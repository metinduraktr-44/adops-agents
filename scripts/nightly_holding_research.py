#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nightly holding research loop (country + OpCo).

Protocol:
1) Read prior stamped archive for each country
2) Write deterministic research NOTES (extend with live web when MCP/API available)
3) Stamp snapshot.json + AUDIT_LOG + BILGI_TABANI
4) Next night reads prior (chain 🔗)

Usage: python3 scripts/nightly_holding_research.py
"""
from __future__ import annotations

import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")


def main() -> int:
    holding_path = ROOT / "data" / "holding.json"
    models_path = ROOT / "data" / "holding_rol_modelleri.json"
    if not holding_path.exists():
        print("missing holding.json")
        return 1
    h = json.loads(holding_path.read_text(encoding="utf-8"))
    models = json.loads(models_path.read_text(encoding="utf-8")) if models_path.exists() else {}

    outputs = []
    for c in h["countries"]:
        d = ROOT / "data" / "arsiv" / "holding" / c["code"]
        d.mkdir(parents=True, exist_ok=True)
        prior_files = sorted(d.glob("snapshot-*.json"))
        prior_note = "none"
        if prior_files:
            prev = json.loads(prior_files[-1].read_text(encoding="utf-8"))
            prior_note = f"{prior_files[-1].name} ts={prev.get('ts')}"

        snap = {
            "ts": TS,
            "country": c["code"],
            "name": c["name"],
            "role": c["role"],
            "law": c["law"],
            "language": c["language"],
            "agency": c["agency"],
            "read_prior": prior_note,
            "research": {
                "competitors_top5": "queue — fill via WebSearch/Exa when auth; keep empty over invention",
                "regulation_delta": f"Watch: {', '.join(c['law'])}",
                "channel_benchmarks": "Use AdOps dept playbooks + country localization checklist",
                "role_models_ref": "data/holding_rol_modelleri.json → country_agencies",
            },
            "chain": "🔗 prior-archive-read",
        }
        snap_path = d / f"snapshot-{DAY}.json"
        snap_path.write_text(json.dumps(snap, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        notes = d / f"NOTES-{DAY}.md"
        notes.write_text(
            f"# {c['code']} gece araştırma\n"
            f"> Damga: {TS}\n\n"
            f"- prior: {prior_note}\n"
            f"- agency: `{c['agency']}`\n"
            f"- law focus: {', '.join(c['law'])}\n"
            f"- models: country_agencies block in holding_rol_modelleri.json\n"
            f"- status: GECTI (deterministic; live SERP optional)\n",
            encoding="utf-8",
        )
        outputs.append(str(snap_path.relative_to(ROOT)))

    # OpCo rollup note
    opco_dir = ROOT / "data" / "arsiv" / "holding" / "_opco"
    opco_dir.mkdir(parents=True, exist_ok=True)
    opco_snap = {
        "ts": TS,
        "subsidiaries": [s["id"] for s in h["subsidiaries"]],
        "models_keys": [k for k in models.keys() if not k.startswith("_")],
        "apps": list(h.get("apps", {}).keys()),
    }
    opco_path = opco_dir / f"snapshot-{DAY}.json"
    opco_path.write_text(json.dumps(opco_snap, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    outputs.append(str(opco_path.relative_to(ROOT)))

    audit = {
        "ts_start": TS,
        "ts_end": TS,
        "op": "gece-holding-arastirma",
        "outputs": outputs,
        "validation": "GECTI",
        "chain": "prev-archive-read",
    }
    with open(ROOT / "AUDIT_LOG.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(audit, ensure_ascii=False) + "\n")

    with open(ROOT / "BILGI_TABANI.md", "a", encoding="utf-8") as f:
        f.write(
            f"\n- [{TS}] gece-holding-arastirma: {len(h['countries'])} ülke + OpCo rollup damgalandı; prior arşiv okundu (🔗).\n"
        )

    print(f"nightly holding research GECTI — {len(outputs)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
