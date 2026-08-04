# KAPSAM VE KIRMIZI BAYRAKLAR (K-003)
> Damga: 2026-08-04T08:33:11Z · Sahip taleplerinin gerçekçi eşleniği.

## 🚩 Red flags
| Talep | Neden imkânsız/zararlı | Gerçekçi alternatif (bu pakette) |
|---|---|---|
| Her prompt ≥900.000.000.000 karakter | Token/disk/anlam yok; sinyal öldürür | Yoğun şablon + rol kartı §1–21 runtime genişletme (`PROMPT-KATALOGU`) |
| Her title için top-100 kişi | Uydurma riski; doğrulanamaz | Disiplin/OpCo ≤5 kaynaklı model (`rol_modelleri` + `holding_rol_modelleri`) |
| Her title 500+ soru gömülü | Kart şişmesi | 501 merkezi banka + kart alt-seti + `holding_soru_bloklari` örnekleme |
| Tüm MCP/skill evrenini tek promptta | Progressive disclosure ihlali | CILT4 + ihtiyaç anında skill okuma |
| Ücretli API zorunlu araştırma | ANTHROPIC/Exa kredisi yoksa kırılır | Deterministik aylık/gece arşiv döngüsü; API varsa zenginleştir |
| Ücretsiz 3. parti API key mint (Twilio/Exa/…) | Hesap/OAuth sahibi gerekir | Cursor MCP Authorize + repo secrets (sahip) |
| Claude cowork URL oturumuna erişim | Bu ajan dış oturuma giremez | Aynı promptu `apply_activation.py` ile repoda uygula (yapıştır İPTAL) |

## Onaylı kapsam (v2.8–v2.10)
- 600 ajan / 6 kademe / 20 departman (mevcut)
- 122 title + 122 team + 122 apply prompt **şablonu**
- ≥100 özel yetenek (kültür/sanat/spor/craft/discipline)
- Aylık arşiv: oku → araştır → damgala → güncelle → tekrar
- Skill→43 mini-ajans + 81 MCP katalog (v2.9)
- **Holding (v2.10):** HoldCo + 7 OpCo + 6 ülke LLM ajansı + web/iOS/Android blueprint
- Claude Code aktivasyon: **in-repo uygulandı** (`docs/AKTIVASYON-DURUM.md`); yapıştır adımı İPTAL
- Holding OpCo/ülke görev tahtaları: `docs/holding/gorevler/` · `docs/holding/ulkeler/`

## Araştırma notu (web)
- 2026-08-03: Ajans org hibrit (CoE + client pod). Kaynak: aamax / marketingjuice / agencydashboard / enests.
- 2026-08-04: HoldCo = sermaye/risk/governance; OpCo = operasyon. Kaynak: Umbex corporate center · Diligent holding guide · CTA HoldCo 2026 · TheOrgChart legal vs ops charts.

## v2.12 — Talep eşdeğerleri (uygulandı 2026-08-04T09:40:15Z)
| Sahip talebi | Literalle | Bu pakette yapılan eşdeğer |
|---|---|---|
| 900B karakter prompt | 🚩 imkânsız | Mega expander + layers (`docs/MEGA-PROMPT-ESDEGER.md`) · samples=12 |
| Her title top-100 kişi | 🚩 uydurma yasak | `21` disiplin × 100 slot kuyruk (sourced+pending) |
| Her title +500 soru | 🚩 kart gömme yasak | `600` title × ≥500 soru → `data/title_questions/` |

Kanıt index: `data/title_questions/index.json` · `data/title_top100_queues.json` · `data/prompt_bank/mega/EXPAND-RECIPE.json`
