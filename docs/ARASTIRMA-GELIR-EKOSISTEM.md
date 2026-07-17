# ARAŞTIRMA — GELİR EKOSİSTEMİ VE EMSALLER
> Tarih: 2026-07-17 · Yöntem: web araştırması (kaynaklı) · Sahip: cro-revenue · Beslediği yüzey: docs/GELIR-MODELI-TAKIP.md
> Kural: veri uydurma yok; her bulgu URL'li; "bulunamadı" açıkça yazılır.

## Blok 1 — İnfra Sponsorlukları

- **Neon Open Source Program** · $5.000/yıl platform kredisi + **$20/refere edilen ödeme yapan müşteri (üst limit yok)** + blog/sosyal tanıtım. Koşul: tanınmış OSS lisansı + Postgres tabanlı bileşen + entegrasyon dokümantasyonu. Yanıt 1-3 iş günü · https://neon.com/programs/open-source
- **Vercel OSS Program** · $3.600 kredi/12 ay + OSS Starter Pack + öncelikli destek. Kohort bazlı; **başvurular Ağustos 2026'da açılıyor** · https://vercel.com/open-source-program
- **Railway Template Kickback** · Şablon deploy gelirinin **%25'i komisyon**; $1M OSS fonu · https://railway.com/open-source-kickback
- **Supabase** · OSS sponsorluk sayfası var; tutar kamuya açık değil · https://supabase.com/open-source
- **Claude for Open Source (Anthropic)** · 6 ay ücretsiz Claude Max 20x (~$1.200). Kriterlerden biri yeter: 500+ bağımlı repo / 200k+ aylık indirme / 100+ merged dış PR / 20+ dış katkıcı / OpenSSF ≥0.4 · https://claude.com/contact-sales/claude-for-oss — 🚩 adops-agents henüz karşılamıyor → Q4 hedefi.
- **Kanıtlanmış emsal — davila7/claude-code-templates (28.2k★):** aynı anda Vercel + Neon + Claude for OSS + Z.AI sponsorluğu + Buy Me a Coffee; repoda NEON_INTEGRATION_PLAN.md (sponsorluk↔entegrasyon takası kanıtı) · https://github.com/davila7/claude-code-templates
- **GitHub Sponsors** · FUNDING.yml + Sponsors hesabı; emsal Caleb Porzio $100k/yıl → kümülatif $1M · https://calebporzio.com/i-just-cracked-1-million-on-github-sponsors-heres-my-playbook

**Aksiyon:** davila7 modelini kopyala — FUNDING.yml (bu commit'te eklendi) + Neon başvurusu için Postgres'li adops bileşeni gerekçesi + Ağustos Vercel kohort taslağı.

## Blok 2 — Paid Placement / Featured

- Newsletter emsalleri: TLDR $3.500/sayı (275k abone) · iOS Dev Weekly $1.800 · Sidebar $950 · CSS Weekly $500 · https://github.com/jackbridger/developer-newsletters · https://advertise.tldr.tech
- daily.dev Ads: CPM $8–20, CPC $0,50–2,50, min $1.000 · https://business.daily.dev/resources/developer-ads-pricing-options-best-channels/
- AI dizinleri: Futurepedia pay-to-feature; TAAFT fiyatı bulunamadı.
- **Anthropic marketplace'lerde ücretli öne çıkarma YOK** — kürasyon + güvenlik taramasıyla girilir.

**Aksiyon:** Erken aşamada placement SATIN ALMA; ücretsiz kürasyonu tüket. K2 kanalının asıl modeli: kendi kataloğumuzda şeffaf "sponsored" satırı SATMAK (tavan referansı: TLDR $3.500/sayı).

## Blok 3 — Referral / Affiliate

| Araç | Komisyon | Not | Kaynak |
|---|---|---|---|
| **Supermetrics** | **%20'ye kadar yinelenen** | PartnerStack, self-serve; Top tier 10 müşteri sonrası | https://supermetrics.com/partners |
| Triple Whale | Açıklanmıyor (Schedule A) | Son dokunuş, 30 gün pencere; ayrı Agency Partner Programı | https://www.triplewhale.com/affiliates |
| Funnel.io | Rev-share, oran gizli | Asıl değer: Funnel'dan lead paylaşımı | https://funnel.io/solution-partner-program |
| AppsFlyer | Nakit komisyon YOK | Sertifikasyon + co-marketing modeli | https://www.appsflyer.com/partner-program/ |
| Adjust | Bulunamadı | Tech-partner entegrasyon modeli | — |
| Northbeam | Bulunamadı | Agency partner sayfası var | — |

**Aksiyon:** Bu haftanın tek net kazanımı Supermetrics — başvur; Funnel/Triple Whale'e ajans kimliğiyle başvur, oranı onboarding'de öğren.

## Blok 4 — Premium Paket Emsalleri

- **Sidekiq Pro** · açık çekirdek + ticari lisans **$995/yıl**; tek kişi, $1M+/yıl · https://sidekiq.org/products/pro/
- **Sponsorware (Porzio)** · yeni bileşen önce sponsorlara → eşikte herkese açılır; 2 günde +$11k/yıl · https://calebporzio.com/sponsorware
- Satış altyapısı: LemonSqueezy lisans anahtarı/abonelikle dev-tool satışına Gumroad'dan uygun.
- **Claude Code ekosisteminde ücretli pro-paket satan bileşen reposu emsali BULUNAMADI — boşluk = fırsat.**

**Aksiyon:** K4 modeli netleşti: çekirdek MIT + Pro dikey paket; sponsorware ile başlat → LemonSqueezy lisansı $99–299/yıl bandı.

## Blok 5 — OSS → Ajans Inbound

- **Evil Martians** · OSS'i açık müşteri kazanım motoru yapan danışmanlık; portföy sayfası + metodoloji · https://evilmartians.com/opensource
- Bireysel vaka: OSS katkısından $100k danışmanlık akışı · https://medium.com/@CodeWithHannan/how-i-turned-open-source-contributions-into-a-100k-consulting-stream-82870330358a
- **Laravel Partners** · resmi partner dizini = ajanslara inbound modeli · https://laravel.com/partners

**Aksiyon:** Her bileşen README'sine "bu sistemi ajansınıza kuralım" CTA'sı; Evil Martians formatında tek vitrin sayfası.

## Blok 6 — Ekosistem Haritası / Dağıtım

- **aitmpl.com** · 1000+ bileşen, tamamen ücretsiz; monetizasyon = sponsor logoları. 28.2k★ · https://www.aitmpl.com
- **Anthropic resmi katman** · anthropics/claude-plugins-official + claude-plugins-community (read-only mirror). Giriş SADECE clau.de/plugin-directory-submission → otomatik güvenlik taraması + onay; doğrudan PR otomatik kapanır · https://code.claude.com/docs/en/discover-plugins
- Görünürlük: hesreallyhim/awesome-claude-code · a-list-of-claude-code-agents · awesomeclaude.ai · claudepluginhub.com · claudemarketplaces.com · TLDR/Bytes/daily.dev

**Aksiyon:** Dağıtım sırası: Anthropic community submission → awesome-claude-code PR → aitmpl katkısı → agregator dizinler. Hepsi ücretsiz.

## İLK 5 AKSİYON (bu hafta — IS_LISTESI P0'a işlendi)

1. FUNDING.yml + GitHub Sponsors hesabı (✅ FUNDING.yml bu pakette; Sponsors hesabını Metin açar, 30 dk).
2. Supermetrics affiliate başvurusu (PartnerStack, %20 recurring) → onayda referral linki README+skill'lere gömülür.
3. Anthropic community marketplace submission (clau.de/plugin-directory-submission) — güvenlik taraması rozeti = dağıtım + güven.
4. awesome-claude-code'a PR + aitmpl'e 1-2 bileşen katkısı — CTA'lı README ile ücretsiz inbound.
5. Ağustos hazırlığı: Vercel OSS kohort başvuru taslağı ($3.600) + Railway adops deploy şablonu (%25 kickback).
