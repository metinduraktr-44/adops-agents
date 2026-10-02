# Araştırma arşivi
> Aylık döngü: oku önceki damgayı → yeniden araştır → yaz `data/arsiv/YYYY-MM/` → AUDIT_LOG.

## Layout
```
data/arsiv/YYYY-MM/
  snapshot.json      # rol_modelleri + ozel_yetenekler hash + notes
  NOTES.md           # insan okunur delta
```

## Workflow
`.github/workflows/aylik-arastirma.yml` → `scripts/monthly_research_refresh.py`

Son üretim: 2026-10-02T10:52:12Z
