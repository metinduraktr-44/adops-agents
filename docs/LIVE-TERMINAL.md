# LIVE TERMINAL
> TR: Tum ops ciktilari terminalde; tmux ile surekli.

## Komutlar
```bash
# tek tick (her seyi yazdir)
bash scripts/live_ops.sh

# canli dongu (varsayilan 120 sn)
bash scripts/live_ops.sh --loop 120
```

## Tmux oturumu
- Session: `adops-live-ops`
- Attach: `tmux -f /exec-daemon/tmux.portal.conf attach -t adops-live-ops`
- Tick: activation → k003 → holding_report → nightly_holding → daily_ops → validate → ozet

## Durum
- Claude Code paste: IPTAL
- Aktivasyon: in-repo (`docs/AKTIVASYON-DURUM.md`)
- validate: her tickte yeniden kosar
