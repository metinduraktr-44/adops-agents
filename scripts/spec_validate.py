#!/usr/bin/env python3
"""Spec validator for GIGA creative agency MATRIX/ and CANVA_OPS/ paths.
Pillow optional — image dimension checks skipped gracefully if missing."""
import json
import os
import sys
from pathlib import Path

try:
    from PIL import Image
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False

issues = []
REQUIRED_MATRIX_KEYS = {"format", "dimensions", "variant_id", "brief_ref"}
REQUIRED_MANIFEST_KEYS = {"job_id", "brief_ref", "matrix_ref", "canva_mode"}


def check_matrix_file(path: Path) -> None:
    if path.suffix == ".json":
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            issues.append(f"[structural] {path}: invalid JSON — {e}")
            return
        if isinstance(data, list):
            for i, row in enumerate(data):
                if isinstance(row, dict):
                    missing = REQUIRED_MATRIX_KEYS - set(row.keys())
                    if missing:
                        issues.append(f"[structural] {path}[{i}]: missing keys {sorted(missing)}")
        elif isinstance(data, dict):
            missing = REQUIRED_MATRIX_KEYS - set(data.keys())
            if missing:
                issues.append(f"[structural] {path}: missing keys {sorted(missing)}")
    elif path.suffix == ".md":
        txt = path.read_text(encoding="utf-8", errors="replace")
        for key in REQUIRED_MATRIX_KEYS:
            if key not in txt:
                issues.append(f"[structural] {path}: missing field mention '{key}'")


def check_canva_ops_file(path: Path) -> None:
    if path.suffix != ".json":
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        issues.append(f"[structural] {path}: invalid JSON — {e}")
        return
    missing = REQUIRED_MANIFEST_KEYS - set(data.keys())
    if missing:
        issues.append(f"[structural] {path}: missing manifest keys {sorted(missing)}")
    mode = data.get("canva_mode", "")
    if mode not in ("BRIEF-ONLY", "FULL"):
        issues.append(f"[semantic] {path}: canva_mode must be BRIEF-ONLY or FULL, got '{mode}'")
    if data.get("autofill") and mode == "BRIEF-ONLY":
        issues.append(f"[semantic] {path}: autofill not allowed in BRIEF-ONLY mode")


def check_image(path: Path) -> None:
    if not HAS_PILLOW:
        return
    if path.suffix.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
        return
    try:
        with Image.open(path) as img:
            w, h = img.size
            if w < 1 or h < 1:
                issues.append(f"[integrity] {path}: invalid dimensions {w}x{h}")
    except OSError as e:
        issues.append(f"[integrity] {path}: cannot read image — {e}")


def scan_path(target: Path) -> None:
    if not target.exists():
        issues.append(f"[structural] path not found: {target}")
        return
    if target.is_file():
        if "MATRIX" in str(target) or target.parent.name == "MATRIX":
            check_matrix_file(target)
        elif "CANVA_OPS" in str(target) or target.parent.name == "CANVA_OPS":
            check_canva_ops_file(target)
        check_image(target)
        return
    for root, _, files in os.walk(target):
        for name in files:
            fp = Path(root) / name
            if fp.name.startswith("."):
                continue
            if "MATRIX" in str(fp):
                check_matrix_file(fp)
            elif "CANVA_OPS" in str(fp):
                check_canva_ops_file(fp)
            check_image(fp)


def main() -> int:
    targets = [Path(p) for p in sys.argv[1:]] if len(sys.argv) > 1 else [
        Path("MATRIX"), Path("CANVA_OPS")
    ]
    for t in targets:
        scan_path(t)
    if not HAS_PILLOW:
        print("SPEC_VALIDATE: GECTI (Pillow optional — image checks skipped)")
    if issues:
        print("SPEC_VALIDATE: KALDI")
        for i in issues:
            print(" -", i)
        return 1
    print("SPEC_VALIDATE: GECTI")
    return 0


if __name__ == "__main__":
    sys.exit(main())
