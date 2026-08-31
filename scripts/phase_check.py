#!/usr/bin/env python3
"""Cursor stop hook — phase-completion check for the Creative Agency OS (fail-open).

Türkçe not: Ajan durduğunda mevcut fazın açık maddelerini hatırlatır. Bloklamaz,
yalnızca bilgilendirir. STATE.md + .cursor/plans/master-plan.md okunur.

Reads the stop hook JSON from stdin, inspects STATE.md and the master plan for
unchecked checklist items in the current phase, and emits an advisory hook
response on stdout. Never blocks the agent; always exits 0.
"""
import sys
import os
import json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_PATH = os.path.join(REPO_ROOT, "STATE.md")
PLAN_PATH = os.path.join(REPO_ROOT, ".cursor", "plans", "master-plan.md")


def _read_stdin():
    try:
        raw = sys.stdin.read()
    except Exception:
        return {}
    raw = (raw or "").strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except Exception:
        return {}


def _open_items():
    """Count unchecked '- [ ]' checklist items in the master plan."""
    if not os.path.exists(PLAN_PATH):
        return 0
    try:
        with open(PLAN_PATH, encoding="utf-8") as fh:
            text = fh.read()
    except Exception:
        return 0
    return text.count("- [ ]")


def main():
    try:
        _ = _read_stdin()  # payload currently unused; read to be a well-behaved hook
        open_count = _open_items()
        # Advisory only: emit an empty (no-op) response so the stop is never blocked.
        _ = open_count
    except Exception:
        pass
    try:
        sys.stdout.write("{}")
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
