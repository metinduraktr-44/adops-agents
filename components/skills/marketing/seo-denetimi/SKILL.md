---
name: seo-denetimi
description: Site SEO denetimi — teknik, on-page, içerik ve otorite katmanları. Kullanıcı "SEO denetimi", "neden sıralanmıyorum", "organik trafik düştü", "teknik SEO", "meta etiket kontrolü" veya bir müşteri sitesinin arama görünürlüğünden bahsettiğinde aktifleş. Örnek: "yeni müşterinin sitesine hızlı SEO taraması yap, pitch'e bulgu lazım".
allowed-tools: Read, Bash, WebFetch
model: sonnet
user-invocable: true
---
# SEO Denetimi
Müşteri sitelerinde SEO sorunlarını bulur, önceliklendirir, aksiyona çevirir. Tipik kullanım: pitch öncesi hızlı tarama, onboarding denetimi, çeyreklik sağlık kontrolü.

## Ne zaman aktifleş
SEO denetimi/sağlık kontrolü istendiğinde, organik trafik anomalisinde, site taşıma öncesi/sonrasında.

## Önce netleştir
- Site tipi (e-ticaret / kurumsal / yayıncı) ve SEO'nun iş hedefi
- Kapsam: tüm site mi, belirli şablon/sayfa mı; Search Console erişimi var mı
- Bilinen sorun veya yakın tarihli değişiklik (taşıma, tasarım yenileme)

## Denetim çerçevesi (öncelik sırası)
1. **Taranabilirlik & indeksleme** — robots.txt kazara engel, XML sitemap sağlığı, canonical tutarlılığı, önemli sayfalar ≤3 tık derinlikte mi
2. **Teknik temel** — Core Web Vitals, mobil uyum, HTTPS, yönlendirme zincirleri
3. **On-page** — title/meta kalıpları, başlık hiyerarşisi, iç bağlantı, yapısal veri
4. **İçerik** — arama niyeti eşleşmesi, ince/yinelenen içerik, içerik boşlukları (rakiplerin sıralandığı, müşterinin olmadığı sorgular)
5. **Otorite** — bağlantı profili özeti, markalı arama hacmi eğilimi

## TR notları
- Türkçe karakterli URL'lerde encoding tutarlılığı; tercihen ASCII slug
- Çok dilli sitelerde `hreflang="tr"` doğruluğu; TR/EN içerik eşleşmesi
- Yerel niyetli sorgular için Google Business Profile + yerel sayfa yapısı

## Çıktı sözleşmesi
Her bulgu: **sorun → kanıt (URL/metrik) → düzeltme (somut adım) → tahmini etki**.
İki kova halinde sun: **Hızlı kazanımlar** (≤2 hafta) ve **stratejik yatırımlar** (çeyreklik). Pitch bağlamında ilk 3 çarpıcı bulguyu yönetici diliyle özetle.

## Örnek
"Mobilya e-ticaret sitesi, organik trafik 3 ayda %30 düştü." → Search Console kıyası: hangi sorgu kümesi düştü; taşıma sonrası 302 zinciri tespiti; kategori sayfalarında kaybolan H1; hızlı kazanım: 301 düzeltmesi + title şablonu; stratejik: kategori içerik programı.
