# OWNER TALEP YANITI — skill/MCP mega paket (2026-08-25)
> Damga: 2026-08-25T14:44:30Z · Claude Code yapıştır = **İPTAL** · Uygulama = **in-repo**
> validate: **GEÇTİ**

## Ne istedin (özet)
1. Listedeki bütün `/skill` + MCP’leri çalıştır
2. Claude Code’a yapıştırılacak **+900.000.000.000** karakter prompt
3. Her title için dünyanın en iyi **100** kişisi + makale/röportaj arşivi
4. C→işçi hiyerarşi, 122×3 prompt, +100 özel yetenek, aylık araştırma döngüsü
5. Lovable / tools / workflows / 7/24 ajans

## Ne yaptık (eşdeğer — K-003)

| Talep | Literalle | Bu repoda |
|---|---|---|
| Tüm skill’leri live invoke | 🚩 imkânsız ölçek | `data/skill_agency_registry.json` · **696 skill → 43 mini-ajans** · `docs/SKILL-AGENCY-REGISTRY.md` |
| 900B karakter prompt | 🚩 sinyal öldürür | Mega expander + yoğun şablon · `docs/MEGA-PROMPT-ESDEGER.md` · `data/prompt_bank/` |
| Title top-100 kişi uydur | 🚩 yasak | `data/title_top100_queues.json` · sourced + `pending_research` |
| Title ≥500 soru kart içi | 🚩 şişme | `data/title_questions/` · **600×500** (kart dışı) |
| Claude Code paste | İPTAL | `scripts/apply_activation.py` · `docs/AKTIVASYON-DURUM.md` |
| Domain/OTel/PD/Slack | Referans | `infra/observability/` · `data/domains/domain_pack.json` |
| Holding | Aktif | `data/holding.json` · 7 OpCo + 6 ülke |
| Aylık arşiv döngüsü | Aktif | `data/arsiv/` + workflows |
| MCP hepsi auth | Owner OAuth | 🚩 Authorize: https://cursor.com/docs/context/mcp |

## Kanıt index
- Aktivasyon: `docs/AKTIVASYON-DURUM.md`
- Skill router: `.cursor/skills/skill-agency-router/SKILL.md`
- Kapsam/red flags: `docs/KAPSAM-VE-KIRMIZI-BAYRAKLAR.md`
- Domain pack: `docs/OZET-DOMAIN-PACK-V213.md`
- Tek sayfa roadmap: `docs/RAPOR-TEK-SAYFA-2026-08-20.md`
- Live: `scripts/live_ops.sh` · tmux `adops-live-ops`

## Cursor meta skill’ler (bu mesajdaki)
`/update-cursor-settings` `/update-cli-config` `/statusline` `/split-to-prs` `/shell` `/review*` `/migrate-to-*` `/sdk` `/create-*` `/canvas` `/babysit`
→ family **`cursor-meta`** (registry’de). Bunlar ürün MCP’si değil; ajan DX. İhtiyaçta tek tek çalıştırılır — toplu “hepsini live” yok.

## Owner P0 (sen)
1. Gemini/OpenRouter key → `.env.local` · `docs/LLM-ENV.md`
2. MCP Authorize (ihtiyaca göre)
3. İlk OpCo scaffold seçimi
4. Domain2 TF apply için vault token + cluster

## Ajan iş listesi (bu tur)
- [x] Skill registry refresh (696/43/81)
- [x] K-003 eşdeğer yenile
- [x] Domain pack yenile
- [x] apply_activation + validate GEÇTİ
- [x] Live tmux devam
- [ ] Exa ile pending_research doldur (auth sonrası)
- [ ] OpCo scaffold (seçim sonrası)

🚩 **900B prompt dosyası üretilmedi. Uydurma kişi listesi yok. Paste yok.**
