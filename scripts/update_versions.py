#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VERSIONS.md yeniden üretici — tüm bileşenlerin SHA256 bütünlük satırları."""
import os, glob, hashlib, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.chdir(ROOT)

files = sorted(glob.glob("components/**/*.md", recursive=True) +
               glob.glob("components/**/*.json", recursive=True) +
               ["data/org.json"])
lines = ["# Component Integrity & Versions",
         "Format: `path | version | sha256 | last_updated_utc`",
         f"Regenerated: {NOW} by scripts/update_versions.py", ""]
for f in files:
    h = hashlib.sha256(open(f, "rb").read()).hexdigest()
    ver = "2.0.0" if "/agency/" in f or f == "data/org.json" else "1.0.1"
    lines.append(f"{f} | {ver} | {h} | {NOW}")
open("VERSIONS.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"VERSIONS.md: {len(files)} entries")
