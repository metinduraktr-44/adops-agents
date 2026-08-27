# CHANNEL_MATRIX — 2026 Spec Reference

> ⚠️ **VERIFY AGAINST OFFICIAL PLATFORM DOCS BEFORE PRODUCTION.** These are working
> reference values for the Creative Agency OS scaffold. They must be reconciled with
> the master prompt's **Bölüm 8** table and confirmed against each platform's current
> official specs before any asset ships. Platform specs change frequently.
>
> Türkçe not: Aşağıdaki değerler çalışma referansıdır; **üretimden önce resmi platform
> dokümanına göre doğrulanmalıdır.** Doğrulanana kadar "verify" say.

The machine-readable source of truth for automation is `MATRIX/PRODUCTION_GRID.csv`.
Keep this markdown as human documentation; keep the CSV authoritative for the hook.

## Common social placements (reference — verify)

| Channel | Placement | Width | Height | Aspect | Format | Max size | Status |
|---|---|---:|---:|---|---|---|---|
| Instagram | Feed (square) | 1080 | 1080 | 1:1 | JPG/PNG | ~30MB | verify |
| Instagram | Feed (portrait) | 1080 | 1350 | 4:5 | JPG/PNG | ~30MB | verify |
| Instagram | Story/Reels | 1080 | 1920 | 9:16 | JPG/MP4 | ~4GB (video) | verify |
| Facebook | Feed | 1080 | 1080 | 1:1 | JPG/PNG | ~30MB | verify |
| Facebook | Story | 1080 | 1920 | 9:16 | JPG/MP4 | verify | verify |
| TikTok | In-feed video | 1080 | 1920 | 9:16 | MP4 | verify | verify |
| YouTube | Thumbnail | 1280 | 720 | 16:9 | JPG/PNG | ~2MB | verify |
| YouTube | Shorts | 1080 | 1920 | 9:16 | MP4 | verify | verify |
| LinkedIn | Feed (square) | 1080 | 1080 | 1:1 | JPG/PNG | verify | verify |
| X (Twitter) | Feed image | 1600 | 900 | 16:9 | JPG/PNG | ~5MB | verify |
| Pinterest | Standard pin | 1000 | 1500 | 2:3 | JPG/PNG | ~20MB | verify |
| Display | Leaderboard | 728 | 90 | ~8:1 | JPG/PNG/GIF | 150KB | verify |
| Display | Medium rectangle | 300 | 250 | 6:5 | JPG/PNG/GIF | 150KB | verify |
| Display | Wide skyscraper | 160 | 600 | ~4:15 | JPG/PNG/GIF | 150KB | verify |

> Every row's numbers are provisional. Reconcile with master-prompt Bölüm 8 and each
> platform's official documentation; update `PRODUCTION_GRID.csv` accordingly.
