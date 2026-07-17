# SEGMENT-600 PLANI — HER GITHUB SEKMESİNDE +600 İŞLEM
> Tarih: 2026-07-17 · Sahip: inf-evp-tech-infra · Motor: `.github/workflows/seed-600.yml` (elle tetiklenir)
> İlke: her işlem GERÇEK bir artefakt taşır (rol kaydı, aktivasyon dosyası, denetim kaydı) — boş gürültü yok.

## Segment tablosu

| Segment | Mekanizma | Sayı | Ön koşul | ETA | Durum |
|---|---|---|---|---|---|
| **Issues** | `seed_issues.py`: 600 rol issue'su ([ROL] slug — aktivasyon) + 27 etiket, checklist gövdeli, idempotent | 600 | Sadece push (built-in GITHUB_TOKEN yeter) | ~15 dk (tek koşum) | HAZIR |
| **Pull requests** | `seed_prs.sh`: rol başına branch→`kayit/aktivasyon/<slug>.md`→PR→merge; 150'lik 4 batch | 600 | Push (built-in token) | ~25 dk × 4 koşum | HAZIR |
| **Actions** | Yan ürün: her PR validate-components'i tetikler (600 koşum) + 4 günlük/haftalık cron + seed koşumları | 600+ | PR tohumlaması | PR'larla birlikte otomatik | HAZIR |
| **Wiki** | `build_wiki.py`: 623 sayfa (600 rol + 20 departman + Home/Sidebar/Footer) → `.wiki.git`'e tek push | 623 | ⚠️ Wiki'de Home sayfasını BİR KEZ UI'dan oluştur | ~2 dk | HAZIR (test edildi: 623 sayfa üretiyor) |
| **Security** | `validate_sarif.py`: bileşen başına 6-katman denetim kaydı → Code scanning (SARIF, kategori `ajans-audit`) + haftalık cron + Dependabot + SECURITY.md | 627 | Push; public repoda code scanning ücretsiz | ~2 dk | HAZIR (test edildi: 627 kayıt) |
| **Projects** | `seed_project_items.py`: "AdOps Ajans — 600 Rol Panosu" (Projects v2) + 600 draft kart | 600 | 🚩 `PROJECTS_TOKEN` secret (PAT, scope: project) — built-in token Projects v2'ye erişemez | ~10 dk | TOKEN BEKLİYOR |
| **Insights** | Ayna sekme — işlem "yaratılmaz"; 600 merge + günlük 2-4 cron commit'i grafiklerini doldurur | 600+ commit | PR tohumlaması | PR'larla otomatik | OTOMATİK |
| **Agents** | 🚩 GitHub Copilot ürün yüzeyi — API ile doldurulamaz · gerçekçi karşılık: repoda 600 ajan kartı + Issues'ta 600 rol kaydı + Wiki'de 600 rol sayfası | — | Copilot aboneliği (istenirse ileride) | — | 🚩 ALTERNATİFLE KAPANDI |

## Koşum sırası (Metin — push sonrası, toplam ~2,5 saat)
1. Actions → **seed-600** → hedef=`issues`, adet=`600` → Run. (~15 dk; Issues sekmesi: 600)
2. Actions → **seed-600** → hedef=`prs`, start=`0/150/300/450`, adet=`150` → 4 kez Run. (PR: 600 · Actions: 600+ · Insights: 600+ commit — hepsi bu adımdan)
3. Repo → Wiki → "Create the first page" → Home'u kaydet (içerik fark etmez, üzerine yazılacak) → Actions → **seed-600** → hedef=`wiki`. (Wiki: 623 sayfa)
4. Actions → **security-audit** → Run. (Security → Code scanning: 627 kayıt; sonrası her Pazartesi otomatik)
5. (Opsiyonel) Settings → Secrets → `PROJECTS_TOKEN` (PAT, scope: project) ekle → seed-600 → hedef=`projeler`. (Projects: 600 kart)

## Hız limiti notları
- Issues/PR üretimi saniyede ~1 işlemle sınırlandı (GitHub secondary rate limit); 403/429'da otomatik bekle-yeniden dene.
- PR batch'i 150 tutuldu — tek koşumda 600 PR abuse tetikleyebilir; 4 batch güvenli bant.
- Tüm scriptler idempotent: yeniden koşum mevcut kayıtları atlar, sayıyı bozmaz.

## Bakım
- Yeni ajan eklenirse (generate_org.py): seed'leri yeniden koştur — sadece delta işlenir.
- Issues = rol backlog'u olarak yaşar; kapatma ritmi departman sync'lerinde kararlaştırılır.
