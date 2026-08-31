#!/usr/bin/env python3
"""Cursor afterFileEdit hook — Canva/creative spec validator (fail-open).

Türkçe not: Üretilen görselleri (piksel/oran/dosya boyutu) kanal matrisine göre
denetler; sonuçları CANVA_OPS/VALIDATION.log'a yazar. Ajanı ASLA bloklamaz.

Behavior
--------
- Reads the afterFileEdit hook payload as JSON from stdin.
- If the edited file is an image (png/jpg/jpeg/gif/webp), attempts a spec check:
  * With Pillow (optional): real pixel width/height + aspect ratio.
  * Without Pillow: degrades gracefully to metadata-only (file size, extension).
- Looks up expected specs in MATRIX/PRODUCTION_GRID.csv when a matching row exists.
- Appends a verdict line to CANVA_OPS/VALIDATION.log.
- Emits valid hook JSON on stdout ({} = no-op / allow) and always exits 0.

This script is intentionally dependency-light (stdlib first) and fail-open: any
error is swallowed so the agent is never blocked by validation tooling.
"""
import sys
import os
import json
import csv
import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(REPO_ROOT, "CANVA_OPS", "VALIDATION.log")
GRID_PATH = os.path.join(REPO_ROOT, "MATRIX", "PRODUCTION_GRID.csv")
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp")


def _now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _log(line):
    """Append a line to VALIDATION.log; never raise."""
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as fh:
            fh.write(line.rstrip("\n") + "\n")
    except Exception:
        pass


def _read_payload():
    """Read hook JSON from stdin; tolerate empty/invalid input."""
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


def _extract_paths(payload):
    """Pull candidate file paths out of a variety of possible payload shapes."""
    paths = []
    if not isinstance(payload, dict):
        return paths
    for key in ("file_path", "filePath", "path"):
        val = payload.get(key)
        if isinstance(val, str):
            paths.append(val)
    edits = payload.get("edits") or payload.get("files")
    if isinstance(edits, list):
        for e in edits:
            if isinstance(e, str):
                paths.append(e)
            elif isinstance(e, dict):
                for key in ("file_path", "filePath", "path"):
                    if isinstance(e.get(key), str):
                        paths.append(e[key])
    return paths


def _load_grid():
    """Return list of expected-spec rows from PRODUCTION_GRID.csv (may be empty)."""
    rows = []
    if not os.path.exists(GRID_PATH):
        return rows
    try:
        with open(GRID_PATH, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                rows.append(row)
    except Exception:
        pass
    return rows


def _image_size(path):
    """Return (width, height) using Pillow if available, else None."""
    try:
        from PIL import Image  # optional dependency
    except Exception:
        return None
    try:
        with Image.open(path) as img:
            return img.size
    except Exception:
        return None


def _check_image(path):
    abspath = path if os.path.isabs(path) else os.path.join(REPO_ROOT, path)
    if not os.path.exists(abspath):
        _log(f"{_now()} SKIP {path} (file not found; metadata-only)")
        return
    try:
        size_bytes = os.path.getsize(abspath)
    except Exception:
        size_bytes = -1
    dims = _image_size(abspath)
    if dims is None:
        _log(
            f"{_now()} INFO {path} size={size_bytes}B dims=UNKNOWN "
            f"(Pillow not installed -> metadata-only; verify against MATRIX)"
        )
        return
    w, h = dims
    ratio = round(w / h, 4) if h else 0
    grid = _load_grid()
    match = None
    for r in grid:
        try:
            if int(r.get("width", -1)) == w and int(r.get("height", -1)) == h:
                match = r
                break
        except (ValueError, TypeError):
            continue
    if match is None:
        _log(
            f"{_now()} INFO {path} {w}x{h} ratio={ratio} size={size_bytes}B "
            f"(no matching PRODUCTION_GRID row; verify against official platform docs)"
        )
        return
    verdict = "PASS"
    notes = []
    max_bytes = None
    raw_max = (match.get("max_file_size") or "").strip().lower()
    try:
        if raw_max.endswith("kb"):
            max_bytes = int(float(raw_max[:-2]) * 1024)
        elif raw_max.endswith("mb"):
            max_bytes = int(float(raw_max[:-2]) * 1024 * 1024)
        elif raw_max.isdigit():
            max_bytes = int(raw_max)
    except Exception:
        max_bytes = None
    if max_bytes is not None and size_bytes > max_bytes:
        verdict = "FAIL"
        notes.append(f"size {size_bytes}B > max {max_bytes}B")
    _log(
        f"{_now()} {verdict} {path} {w}x{h} ratio={ratio} size={size_bytes}B "
        f"channel={match.get('channel','?')}/{match.get('placement','?')}"
        + (f" [{'; '.join(notes)}]" if notes else "")
    )


def main():
    try:
        payload = _read_payload()
        for p in _extract_paths(payload):
            if p.lower().endswith(IMAGE_EXTS):
                _check_image(p)
    except Exception as exc:  # absolute fail-open guarantee
        _log(f"{_now()} ERROR hook exception: {exc!r} (fail-open)")
    # Emit a no-op hook response and always succeed.
    try:
        sys.stdout.write("{}")
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
