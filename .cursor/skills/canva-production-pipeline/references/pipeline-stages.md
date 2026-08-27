# Canva Production Pipeline — Stage Checklists

Türkçe not: Uçtan uca üretim hattının ayrıntılı kontrol listeleri. Ana akış `SKILL.md` içinde.

## Stage 1 — Brief
- [ ] Brief grounded only in `CONTEXT/CONTEXT_BRIEF.md` (no invented brand facts).
- [ ] One brief per channel × scenario present in `SCENARIOS/` and `MATRIX/PRODUCTION_GRID.csv`.

## Stage 2 — Bulk Create (autofill)
- [ ] Data table columns map to brand-template fields.
- [ ] Mode gate respected; dry-run writes payload to `CANVA_OPS/`.
- [ ] Job submitted + polled to completion.

## Stage 3 — Resize
- [ ] All target placements from the matrix covered.
- [ ] Each variant spec-checked (exact pixels, ratio).

## Stage 4 — QA gates
- [ ] `canva-brand-check`: colors/fonts/logo/tone.
- [ ] `spec-matrix` / `spec-dogrula`: pixels, ratio, file size, format.
- [ ] Off-spec/off-brand assets do not advance.

## Stage 5 — Export
- [ ] Format/quality per placement.
- [ ] Export URLs/paths registered.

## Stage 6 — Archive
- [ ] Approved set archived to `ARCHIVE/<date>-<phase>/`.
- [ ] `DESIGN_REGISTRY.csv` updated (append-only).

Reminder: verify all platform specs against official platform docs before production.
