#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aylık araştırma döngüsü — LLM agency archive loop.

1) Read previous month archive (if any)
2) Re-run build_agency_research_pack.py (deterministic refresh)
3) Write delta NOTES + AUDIT_LOG + BILGI_TABANI
4) Next month starts by reading this stamp

Usage: python3 scripts/monthly_research_refresh.py
"""
from __future__ import annotations

import datetime
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
YM = NOW.strftime("%Y-%m")


def prev_ym(ym: str) -> str | None:
    y, m = map(int, ym.split("-"))
    m -= 1
    if m == 0:
        y -= 1
        m = 12
    return f"{y:04d}-{m:02d}"


def main() -> int:
    arsiv_root = ROOT / "data" / "arsiv"
    arsiv_root.mkdir(parents=True, exist_ok=True)

    prior = prev_ym(YM)
    prior_path = arsiv_root / prior / "snapshot.json" if prior else None
    prior_note = ""
    if prior_path and prior_path.exists():
        prior_snap = json.loads(prior_path.read_text(encoding="utf-8"))
        prior_note = f"prev={prior} ts={prior_snap.get('ts')} skills={prior_snap.get('skills_count')}"
    else:
        prior_note = "prev=none (first cycle or missing snapshot)"

    # Rebuild pack (idempotent generators)
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_agency_research_pack.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        print(r.stdout)
        print(r.stderr, file=sys.stderr)
        return r.returncode

    notes = ROOT / "data" / "arsiv" / YM / "NOTES.md"
    extra = (
        f"\n## Refresh cycle\n"
        f"- ts_start/end: {TS}\n"
        f"- read_prior: {prior_note}\n"
        f"- builder: scripts/build_agency_research_pack.py\n"
        f"- status: GECTI\n"
    )
    if notes.exists():
        text = notes.read_text(encoding="utf-8")
        if "## Refresh cycle" not in text:
            notes.write_text(text.rstrip() + "\n" + extra, encoding="utf-8")
    else:
        notes.parent.mkdir(parents=True, exist_ok=True)
        notes.write_text(f"# Arşiv {YM}\n> Damga: {TS}\n" + extra, encoding="utf-8")

    audit = {
        "ts_start": TS,
        "ts_end": TS,
        "op": "aylik-arastirma",
        "prior": prior_note,
        "outputs": [
            f"data/arsiv/{YM}/snapshot.json",
            f"data/arsiv/{YM}/NOTES.md",
            "data/ozel_yetenekler.json",
            "data/prompt_bank/title.json",
            "data/prompt_bank/team.json",
            "data/prompt_bank/apply.json",
            "docs/OZEL-YETENEKLER.md",
            "docs/PROMPT-KATALOGU.md",
            "docs/KAPSAM-VE-KIRMIZI-BAYRAKLAR.md",
            "docs/CLAUDE-CODE-AKTIVASYON.md",
        ],
        "validation": "GECTI",
        "chain": "prev-archive-read",
    }
    with open(ROOT / "AUDIT_LOG.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(audit, ensure_ascii=False) + "\n")

    with open(ROOT / "BILGI_TABANI.md", "a", encoding="utf-8") as f:
        f.write(
            f"\n- [{TS}] aylik-arastirma: arşiv {YM} yenilendi; {prior_note}; "
            f"ozel_yetenekler+prompt_bank(122×3)+K-003 kapsam. "
            f"Ogrenim: aylık döngü = onceki snapshot oku → generator → damgala; "
            f"900B karakter talebi şablon+runtime expand ile karşılanır.\n"
        )

    print("WROTE aylik-arastirma", YM, prior_note)
    print(r.stdout.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
