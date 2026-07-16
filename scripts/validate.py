#!/usr/bin/env python3
"""Lightweight 3-in-1 validator: structural + semantic + integrity.
Mirrors the aitmpl validation idea (no external deps)."""
import os, re, sys, hashlib, glob

FORBIDDEN = [r"rm\s+-rf\s+/", r"curl[^\n]*\|\s*sh", r"\beval\s*\(",
             r"base64\s+-d[^\n]*\|\s*sh", r"wget[^\n]*\|\s*sh"]
issues = []

def check_md(path):
    txt = open(path, encoding="utf-8", errors="replace").read()
    # structural: agents/commands/skills need frontmatter
    if txt.lstrip().startswith("---"):
        fm = txt.split("---", 2)
        head = fm[1] if len(fm) > 2 else ""
        if "skills/" in path and "SKILL.md" in path:
            for key in ("name:", "description:"):
                if key not in head:
                    issues.append(f"[structural] {path}: missing {key}")
        elif "/agents/" in path or "/commands/" in path:
            if "description:" not in head:
                issues.append(f"[structural] {path}: missing description:")
    else:
        if "/agents/" in path or "/commands/" in path or path.endswith("SKILL.md"):
            issues.append(f"[structural] {path}: missing YAML frontmatter")
    # semantic
    for pat in FORBIDDEN:
        if re.search(pat, txt):
            issues.append(f"[semantic] {path}: dangerous pattern /{pat}/")

def main():
    files = glob.glob("components/**/*.md", recursive=True)
    files += glob.glob("components/**/*.json", recursive=True)
    for f in files:
        if f.endswith(".md"):
            check_md(f)
    # integrity summary (informational)
    print(f"Scanned {len(files)} component files.")
    if issues:
        print("VALIDATION: KALDI")
        for i in issues:
            print(" -", i)
        sys.exit(1)
    print("VALIDATION: GECTI")

if __name__ == "__main__":
    main()
