# Owner upload — Claude Code Bilgileri ve Güvenlik Uyarıları

> Damga: 2026-11-03T11:50:00Z · **No extract** — source files were not in this VM.
> TR: İçerik uydurulmaz. Byte-faithful metin için owner yüklemesi şart.

## Search result (this run)

Looked for `Claude Code Bilgileri ve Güvenlik Uyarıları.docx` and `.pdf` (NFC/NFD `ü`):

- `/workspace`, git tree, `/tmp`, `/home/ubuntu`, `/opt/cursor`, `/mnt`, `/cursor/stores`, `~/.cursor`
- Downloads/Desktop/attachments/uploads (paths absent)
- files newer than `2026-11-03 09:59 UTC` with `.docx`/`.pdf`

**Hits: 0.** Chat names only. Do not treat draft PR #628 as a substitute for the owner files.

## What to upload

1. Attach both files to the next Cursor Cloud / agent turn (workspace or conversation artifacts).
2. After they land, a later run can `pdftotext` / unzip docx, write extract under `/opt/cursor/artifacts/`, and apply **defense-only** mappings that fit this Claude Code component pack.
3. Secrets stay `${VAR}` / vault / `<REDACTED>`.

## Related in-repo (not a replacement)

- Draft (unofficial, not byte-faithful): https://github.com/metinduraktr-44/adops-agents/pull/628
- Security OS: `SECURITY_STATE.md` · `docs/SECURITY-GIGA-BOOTSTRAP.md`
- Unlock criteria: `TASKS/SEC-T003.md`
