# AKTİVASYON DURUMU
> Damga: 2026-08-27T12:43:28Z · **Claude Code'a yapıştır = İPTAL** · Prompt **bu repoda / bu ajan tarafından uygulandı**.

## Applied layers
| Katman | Durum | Kanıt |
|---|---|---|
| Constitution (CLAUDE.md + CILT4 + MASTER + K-003) | AKTİF | always-on rule + CLAUDE.md |
| Org 600 | AKTİF | data/org.json |
| Prompt bank 122×3 | AKTİF | data/prompt_bank/ |
| Skill mini-ajans (v2.9) | AKTİF | data/skill_agency_registry.json |
| Holding (v2.10) | AKTİF | data/holding.json |
| Domain pack (v2.13) | AKTİF | data/domains/domain_pack.json + infra/observability/ |
| **Security GIGA pack** | **AKTİF (in-repo)** | `docs/CURSOR-SECURITY-GIGA-MASTER-PROMPT.md` · `SECURITY_STATE.md` MODE=ASSESS-ONLY |
| Security Claude Code paste | **İPTAL** | `docs/SECURITY-GIGA-BOOTSTRAP.md` |
| Daily standup | KOŞTU | gundem/2026-08-27-standup.md |
| HoldCo portföy | KOŞTU | gundem/2026-08-27-holding-portfoy.md |
| Gece ülke arşivi | KOŞTU | data/arsiv/holding/*/snapshot-2026-08-27.json |
| OpCo görev tahtaları | YAZILDI | docs/holding/gorevler/ |
| Ülke ajans tahtaları | YAZILDI | docs/holding/ulkeler/ |
| validate.py | GEÇTİ | exit 0 |

## Bugünün öz-denetim örnekleri
1. Başkasının işini beklerken kendi tarafımı hazır tuttum mu?
2. Sessiz kalarak bir riski gömdüm mü?
3. Kararımın kanıtını (link/commit/dosya) bıraktım mı?
4. Bu çıktı için 'definition of done' karşılandı mı?
5. Bugün ajansı bir adım ileri götüren en somut şey neydi?
6. Yarına devrettiğim en kritik açık madde ne; sahibi kim?
7. Bu işi baştan yapsam neyi farklı yapardım?
8. Ölçebildiğim bir ilerleme kaydettim mi, yoksa sadece meşgul mü göründüm?
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
  "build_domain_observability_pack.py": 0,
  "daily_ops.py": 0,
  "holding_report.py": 0,
  "nightly_holding_research.py": 0,
  "validate.py": 0
}
```

## Owner next (Metin)
- MCP Authorize yalnızca ihtiyaç olanlar (Exa/Twilio/Datadog/Sentry/PagerDuty/…)
- Domain2 TF/OTel apply için credential + cluster onayı
- OpCo native scaffold hangi markadan → söyle; ayrı PR açılır
- Claude Code paste **gerekmiyor** — bu dosya kanıt
- **Security GIGA:** Cursor restart → skills/hooks; MODE=ASSESS-ONLY; MCP security catalog off until enable; `/sec-baslat`
