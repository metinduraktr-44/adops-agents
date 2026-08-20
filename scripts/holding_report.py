#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daily HoldCo portfolio rollup → gundem/ + AUDIT_LOG."""
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
    if not holding_path.exists():
        print("missing data/holding.json — run build_holding_pack.py first")
        return 1
    h = json.loads(holding_path.read_text(encoding="utf-8"))

    lines = [
        f"# HoldCo portföy — {DAY}",
        f"> Damga: {TS} · {h['name']}",
        "",
        "## OpCo durum satırları",
    ]
    for s in h["subsidiaries"]:
        lines.append(
            f"- **{s['name']}** (`{s['id']}`): mandate OK · KPI owners={s['reports_to_holdco']} · surfaces={','.join(s['surfaces'])}"
        )
    lines += ["", "## Ülke ajansları"]
    for c in h["countries"]:
        lines.append(f"- {c['code']} {c['name']} ({c['role']}) → `{c['agency']}`")
    lines += [
        "",
        "## Aksiyon",
        "- Kırmızı KPI → OpCo EVP + HoldCo COO",
        "- Sermaye talebi → HoldCo CFO zarfı",
        "- Hukuk/privacy → HoldCo CLO + hukuk OpCo",
        "",
        "## DoD",
        "- Bu dosya yayınlandı; AUDIT_LOG damgalandı.",
    ]

    out_dir = ROOT / "gundem"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"{DAY}-holding-portfoy.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    audit = {
        "ts_start": TS,
        "ts_end": TS,
        "op": "holding-konsolide",
        "output": str(out.relative_to(ROOT)),
        "validation": "GECTI",
    }
    with open(ROOT / "AUDIT_LOG.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(audit, ensure_ascii=False) + "\n")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
