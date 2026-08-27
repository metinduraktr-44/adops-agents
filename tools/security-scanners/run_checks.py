#!/usr/bin/env python3
"""Run defense-only security scaffolding checks."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def run(cmd: list[str]) -> int:
    print("+", " ".join(cmd))
    return subprocess.call(cmd, cwd=ROOT)


def main() -> int:
    rc = 0
    for cmd in (
        [sys.executable, "scripts/secret_scan.py", "."],
        [sys.executable, "scripts/ethics_check.py", "."],
        [sys.executable, "scripts/validate.py"],
    ):
        c = run(cmd)
        if c != 0:
            rc = c
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
