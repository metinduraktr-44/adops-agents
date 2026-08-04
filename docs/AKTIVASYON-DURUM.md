# AKTİVASYON DURUMU
> Damga: 2026-08-04T09:40:15Z · **Claude Code'a yapıştır = İPTAL** · Prompt **bu repoda / bu ajan tarafından uygulandı**.

## Applied layers
| Katman | Durum | Kanıt |
|---|---|---|
| Constitution (CLAUDE.md + CILT4 + MASTER + K-003) | AKTİF | always-on rule + CLAUDE.md |
| Org 600 | AKTİF | data/org.json |
| Prompt bank 122×3 | AKTİF | data/prompt_bank/ |
| Skill mini-ajans (v2.9) | AKTİF | data/skill_agency_registry.json |
| Holding (v2.10) | AKTİF | data/holding.json |
| Daily standup | KOŞTU | gundem/2026-08-04-standup.md |
| HoldCo portföy | KOŞTU | gundem/2026-08-04-holding-portfoy.md |
| Gece ülke arşivi | KOŞTU | data/arsiv/holding/*/snapshot-2026-08-04.json |
| OpCo görev tahtaları | YAZILDI | docs/holding/gorevler/ |
| Ülke ajans tahtaları | YAZILDI | docs/holding/ulkeler/ |
| validate.py | GEÇTİ | exit 0 |

## Bugünün öz-denetim örnekleri
1. Holdout/artımsallık düşündüm mü?
2. Dashboard SLA'sını tutturdum mu?
3. Bu işi başka bir ajan benim yardımım olmadan tekrarlayabilir mi?
4. Artefaktı zaman damgaladım mı?
5. Playbook'u güncel tuttum mu?
6. P0 işleri gerçekten P0 mı; yoksa kolay olanı mı önce yaptım?
7. Biten işi arşive taşıdım mı?
8. IS_LISTESI'ni bugün yeniden önceliklendirdim mi?
9. [holdco] Sermaye tahsisi bu hafta en yüksek marjinal getirili OpCo'ya mı gitti?
10. [holdco] Portföy KPI'ları OpCo'lar arasında karşılaştırılabilir mi (ROIC/FCF)?
11. [apps] Web konsol P0 bug açık mı?
12. [apps] iOS/Android release train tarihi net mi?

## Script sonuçları
```json
{
  "build_holding_pack.py": 0,
  "build_skill_agency_registry.py": 0,
  "build_k003_equivalents.py": 0,
  "daily_ops.py": 0,
  "holding_report.py": 0,
  "nightly_holding_research.py": 0,
  "validate.py": 0
}
```

## Owner next (Metin)
- MCP Authorize yalnızca ihtiyaç olanlar (Exa/Twilio/…)
- OpCo native scaffold hangi markadan → söyle; ayrı PR açılır
- Claude Code paste **gerekmiyor** — bu dosya kanıt
