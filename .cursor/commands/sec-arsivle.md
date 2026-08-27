---
name: sec-arsivle
description: Archive completed security phase outputs into ARCHIVE/ without losing history.
---

# /sec-arsivle (ARŞİVLE — Security)

## Objective
Move completed-phase security artifacts into a dated archive folder.

## Requirements
- Read `SECURITY_STATE.md` to confirm which phase is complete.
- Copy/move that phase's outputs into `ARCHIVE/<YYYY-MM-DD>-<phase>/`.
- Never delete source-of-truth files (`SECURITY_STATE.md`, plan); append an archive note.
- No secrets in archived content (redact to `<REDACTED>` if found).

## Output
- `ARCHIVE/<YYYY-MM-DD>-<phase>/` populated.
- Archive note appended to `SECURITY_STATE.md` resume notes.
