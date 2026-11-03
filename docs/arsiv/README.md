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
Mid-cycle: `python3 scripts/research_loop_continue.py` (`/arastirma-devam`)

```
data/arsiv/YYYY-MM/LOOP.json   # mid-cycle stamp (queues + registry, no skill invoke)
```

Son üretim: 2026-11-02T05:07:33Z · continue: `scripts/research_loop_continue.py`
