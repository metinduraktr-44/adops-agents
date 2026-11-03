#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mid-cycle LLM agency research loop (DEVAM / archive-first).

Does NOT live-invoke Cursor skills. Does NOT invent top-100 people (K-003).
1) Read prior data/arsiv + arsiv/*-arastirma.md
2) Stamp title_top100_queues.json (pending_research stays pending)
3) Re-run research_loop.py + skill_agency_registry builder
4) Write data/arsiv/YYYY-MM/LOOP.json + NOTES + AUDIT/BILGI

Usage: python3 scripts/research_loop_continue.py [--month YYYY-MM]
"""
from __future__ import annotations

import argparse
import datetime
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")


def prev_ym(ym: str) -> str:
    y, m = map(int, ym.split("-"))
    m -= 1
    if m == 0:
        y -= 1
        m = 12
    return f"{y:04d}-{m:02d}"


def read_prior(ym: str) -> dict:
    arsiv = ROOT / "data" / "arsiv"
    prior = prev_ym(ym)
    out = {
        "ym": ym,
        "prior_ym": prior,
        "prior_snapshot": None,
        "current_snapshot": None,
        "role_model_archive": None,
    }
    cur = arsiv / ym / "snapshot.json"
    prev = arsiv / prior / "snapshot.json"
    if prev.exists():
        snap = json.loads(prev.read_text(encoding="utf-8"))
        out["prior_snapshot"] = {
            "path": str(prev.relative_to(ROOT)),
            "ts": snap.get("ts"),
            "skills_count": snap.get("skills_count"),
        }
    if cur.exists():
        snap = json.loads(cur.read_text(encoding="utf-8"))
        out["current_snapshot"] = {
            "path": str(cur.relative_to(ROOT)),
            "ts": snap.get("ts"),
            "skills_count": snap.get("skills_count"),
        }
    role_md = ROOT / "arsiv" / f"{ym}-arastirma.md"
    if role_md.exists():
        out["role_model_archive"] = str(role_md.relative_to(ROOT))
    return out


def stamp_title_top100(ym: str, prior: dict) -> dict:
    path = ROOT / "data" / "title_top100_queues.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    sourced = pending = 0
    invented = 0
    for _code, block in (data.get("disciplines") or {}).items():
        for slot in block.get("slots") or []:
            status = slot.get("status")
            if status == "sourced":
                sourced += 1
                if not slot.get("url") or not slot.get("name"):
                    invented += 1
            elif status == "pending_research":
                pending += 1
                if slot.get("name"):
                    invented += 1
    if invented:
        raise SystemExit(f"K-003: {invented} queue slots violate sourced-URL / pending-null-name")
    data["ts"] = TS
    data["last_loop"] = {
        "ts": TS,
        "ym": ym,
        "op": "research-loop-continue",
        "prior": prior.get("prior_snapshot"),
        "sourced_total": sourced,
        "pending_total": pending,
        "policy": "pending_research only — do not invent names; promote only with real URL",
        "fill_rule": "Keep pending until sourced URL exists",
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"sourced_total": sourced, "pending_total": pending, "path": str(path.relative_to(ROOT))}


def run_py(script: str, extra: list[str] | None = None) -> None:
    cmd = [sys.executable, str(ROOT / "scripts" / script)] + (extra or [])
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stdout)
        sys.stderr.write(r.stderr)
        raise SystemExit(r.returncode)
    if r.stdout.strip():
        print(r.stdout.strip())


def write_loop_artifact(ym: str, prior: dict, queues: dict) -> Path:
    dest = ROOT / "data" / "arsiv" / ym
    dest.mkdir(parents=True, exist_ok=True)
    payload = {
        "ts": TS,
        "ym": ym,
        "op": "research-loop-continue",
        "archive_first": prior,
        "queues": queues,
        "ran": [
            "scripts/research_loop.py",
            "scripts/build_skill_agency_registry.py",
        ],
        "not_ran": [
            "live skill invoke (family mini-agency stamp only)",
            "title_top100 name invention",
            "900B prompt blobs",
        ],
        "claude_code_docx": "not found under uploads/ — leftover on PR #628 corpus extract",
        "security_mode": "ASSESS-ONLY",
        "k003": "GECTI",
    }
    loop_path = dest / "LOOP.json"
    loop_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    notes = dest / "NOTES.md"
    extra = (
        f"\n## Research-loop continue\n"
        f"- ts: {TS}\n"
        f"- archive_first: prior={prior.get('prior_ym')} {prior.get('prior_snapshot')}\n"
        f"- queues: sourced={queues['sourced_total']} pending={queues['pending_total']} (no invented names)\n"
        f"- skill_agency_registry: rebuilt stamp, no live skill invoke\n"
        f"- Claude Code .docx/.pdf: VM'de yok → PR #628 extract duruyor\n"
        f"- Security MODE: ASSESS-ONLY\n"
    )
    if notes.exists():
        text = notes.read_text(encoding="utf-8")
        if "## Research-loop continue" not in text:
            notes.write_text(text.rstrip() + "\n" + extra, encoding="utf-8")
        else:
            notes.write_text(text.split("## Research-loop continue")[0].rstrip() + "\n" + extra, encoding="utf-8")
    else:
        notes.write_text(f"# Arşiv {ym}\n> Damga: {TS}\n" + extra, encoding="utf-8")
    return loop_path


def stamp_audit(ym: str, prior: dict, queues: dict) -> None:
    audit = {
        "ts_start": TS,
        "ts_end": TS,
        "op": "research-loop-continue",
        "month": ym,
        "prior": prior.get("prior_snapshot"),
        "outputs": [
            f"data/arsiv/{ym}/LOOP.json",
            f"data/arsiv/{ym}/NOTES.md",
            "data/title_top100_queues.json",
            "data/skill_agency_registry.json",
            f"arsiv/{ym}-arastirma.md",
            "docs/ARASTIRMA-TAKVIMI.md",
            "docs/SKILL-AGENCY-REGISTRY.md",
        ],
        "validation": "GECTI",
        "chain": "prev-archive-read",
        "k003": "pending_research only; no 900B; no invented people",
    }
    with open(ROOT / "AUDIT_LOG.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(audit, ensure_ascii=False) + "\n")
    with open(ROOT / "BILGI_TABANI.md", "a", encoding="utf-8") as f:
        f.write(
            f"\n- [{TS}] research-loop-continue: {ym} arşiv-önce "
            f"prev={prior.get('prior_ym')}; queues sourced={queues['sourced_total']} "
            f"pending={queues['pending_total']}; registry damga; skill canlı çağrı yok. "
            f"Öğrenim: mid-cycle = oku arşiv → kuyruk damgala (pending kalır) → "
            f"research_loop+registry; .docx yoksa #628 extract'e dokunma.\n"
        )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--month", default=NOW.strftime("%Y-%m"))
    args = ap.parse_args()
    ym = args.month

    prior = read_prior(ym)
    queues = stamp_title_top100(ym, prior)
    run_py("research_loop.py", ["--month", ym])
    run_py("build_skill_agency_registry.py")
    write_loop_artifact(ym, prior, queues)
    stamp_audit(ym, prior, queues)
    print("WROTE research-loop-continue", ym, TS, queues)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
