#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AI AGENCY DOC GENERATOR — org.json'dan MASTER-PROMPT (900+ başlık) + operasyon dokümanları üretir."""
import json, os, re, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TODAY = NOW[:10]
org = json.load(open(os.path.join(ROOT, "data", "org.json"), encoding="utf-8"))

TIER_ORDER = ["EVP", "DIRECTOR", "LEAD", "SPECIALIST", "ANALYST"]
TIER_TR = {"EVP": "KADEME 2 — EVP", "DIRECTOR": "KADEME 3 — DİREKTÖR", "LEAD": "KADEME 4 — LEAD",
           "SPECIALIST": "KADEME 5 — UZMAN", "ANALYST": "KADEME 6 — ANALİST"}

FAZLAR = [
 ("F0", "2026-07-17 → 2026-07-18", "Lansman", ["v2 yapısı main'e push", "3 yeni Actions workflow aktif", "ANTHROPIC_API_KEY secret kontrolü"]),
 ("F1", "2026-07-19 → 2026-07-24", "Isınma", ["Günlük döngü 7 gün kesintisiz yeşil", "İlk 5 standup + toplantı tutanağı", "IS_LISTESI günlük güncelleniyor"]),
 ("F2", "2026-07-25 → 2026-07-31", "İçerik & Vitrin", ["5+ makale yayında (makaleler/)", "3 ekosistem dizinine listeleme (aitmpl vb.)", "README inbound yolu canlı (iletişim + CTA)"]),
 ("F3", "2026-08-01 → 2026-08-14", "Gelir Kapıları 1-3", ["10 sponsor/vendor görüşmesi başlatıldı", "İlk referral anlaşması imza/sözlü onay", "Featured placement fiyat kartı yayınlandı"]),
 ("F4", "2026-08-15 → 2026-08-31", "Premium Paket", ["Premium pack v1 spec + 10 gelişmiş bileşen", "Lisans/fiyat modeli yayında", "2. referral anlaşması"]),
 ("F5", "2026-09-01 → 2026-09-30", "Inbound Huni", ["İlk nitelikli ajans lead'i", "İlk gelir kaydı (herhangi bir kanaldan)", "Vaka çalışması #1 yayında"]),
]

GELIR = [
 ("K1", "Altyapı Sponsorlukları", "cro-revenue → prt-evp-partnerships-sponsorships",
  "Neon/Vercel benzeri altyapı firmalarından repo sponsorluğu (~$5K emsal + referral).",
  ["Hedef liste: 20 firma (F2)", "Pitch kit: sponsorship-pitch-kit (F2)", "10 görüşme (F3)", "İlk anlaşma (F3-F4)"]),
 ("K2", "Featured/Promoted Bileşenler", "cpo-product → prd-evp-product-premium",
  "Katalogda ücretli öne çıkarma alanı; şeffaf 'sponsored' etiketiyle.",
  ["Fiyat kartı (F3)", "Yerleşim slotları README+katalog (F3)", "İlk satış (F4-F5)"]),
 ("K3", "Referral Komisyonları", "cro-revenue → prt bölümü",
  "Entegre edilen analytics/attribution araçlarında (Supermetrics, MMP'ler vb.) yönlendirme komisyonu.",
  ["Vendor listesi + program şartları (F2)", "İlk anlaşma (F3)", "UTM'li yönlendirme takibi (F3)"]),
 ("K4", "Premium Plugin Paketi", "cpo-product → prd bölümü",
  "Gelişmiş ajanlar/workflow'lar lisanslı paket olarak satılır; çekirdek MIT kalır.",
  ["Spec (F4)", "10 premium bileşen (F4)", "Lisans + ödeme yolu (F4)", "İlk satış (F5)"]),
 ("K5", "Ajansa Inbound Lead Hunisi", "cro-revenue → nbd-evp-new-business",
  "En yüksek değerli kanal: repo trafiği → keşif görüşmesi → medya uzmanı ajans hizmeti.",
  ["README CTA + iletişim yolu (F2)", "Lead scoring (F3)", "Pitch factory 48s SLA (F3)", "İlk nitelikli lead (F5)"]),
]

def W(rel, content):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print("WROTE", rel, f"({len(content):,} ch)")

# ============================================================================
# 1) MASTER-PROMPT-AJANS.md — 900+ başlık
# ============================================================================
L = []
A = L.append
A(f"# MASTER-PROMPT — ADOPS AI AGENCY (v2)")
A(f"> Üretim: {NOW} · Kaynak: scripts/generate_org.py + generate_docs.py · Ajan sayısı: {org['total']} · Bu belge ajansın anayasasıdır; her ajan kendi rol kartını buradan ve components/agents/agency/ altından okur.")
A("")

# --- BÖLÜM I
A("## BÖLÜM I — KİMLİK VE MİSYON")
for h, t in [
 ("Vizyon", "Dünyanın en büyük AI-yerlisi performans pazarlama ve programatik ajansı: 600 uzman ajan, 7/24 vardiya, günde minimum 1 üretim döngüsü."),
 ("Misyon", "Doğrulanmış, kopyala-yapıştır hazır performans pazarlama bileşenleri üretmek; açık kaynak çekişini 5 kanallı gelire çevirmek."),
 ("Sahiplik", "Sahip: Metin Durak. CEO ajanı sahibe raporlar; sahip onayı olmadan ücretli taahhüt verilmez."),
 ("Çalışma Dili", "Sahibe dönük çıktı: Türkçe, terse. Repo/ürün dosyaları: İngilizce + kısa TR not."),
 ("Değer Ölçüsü", "Sinyal > uzunluk. Öğrenme = bilgi tabanı büyümesi (model değil) — K-003."),
 ("Çalışma Modeli", "Cron-tetiklemeli nöbet: ajanlar sürekli süreç değil, tetiklenen roldür; 7/24'lük, kesintisiz cron zinciriyle sağlanır."),
 ("Tek Doğruluk Kaynağı", "Org yapısı data/org.json; değişiklik SADECE generate_org.py üzerinden."),
 ("Bağlılık", "CILT4 operasyon anayasası ve 5 güvenlik kuralı bu belgenin üstündedir."),
]:
    A(f"### I.{h}")
    A(t)
A("")

# --- BÖLÜM II
A("## BÖLÜM II — GÜVENLİK VE YÖNETİŞİM")
for h, t in [
 ("Kural 1 — Resmi Öncelik", "Anthropic resmi kaynağı varsa önce o; topluluk kaynağı boşluk doldurur."),
 ("Kural 2 — Yürütülebilir Script Tedbiri", "Script bundle eden bileşen: oku, özetle, DENETÇİ onayı olmadan çalıştırma."),
 ("Kural 3 — Güncellik Yanılgısı Yok", "Güven sırası: resmi org > çapraz konsensüs > kesintisiz geçmiş > yıldız."),
 ("Kural 4 — Fork/Mirror Yasağı", "Kurulum sadece kanonik organizasyondan."),
 ("Kural 5 — Marketplace Öncelik", "Önce Anthropic'in taradığı katman."),
 ("Doğrulama Katmanları", "6 katman: structural, integrity/SHA256, semantic/injection, reference/SSRF, known-patterns, independent review."),
 ("Denetim Zinciri", "Her işlem: ts_start → iş → doğrula → ts_end → AUDIT_LOG.jsonl → BILGI_TABANI.md."),
 ("Eskalasyon Anayasası", "Blocker>4h → yönetici; bütçe/politika → fin/leg; imkânsız hedef → 🚩 formatı."),
 ("Veri Dürüstlüğü", "Veri uydurma yasak; tahmin açıkça etiketlenir."),
 ("Sürüm Disiplini", "Her bileşen VERSIONS.md'de semver + SHA256 ile izlenir."),
]:
    A(f"### II.{h}")
    A(t)
A("")

# --- BÖLÜM III — ORGANİZASYON
A("## BÖLÜM III — ORGANİZASYON (600 AJAN, 6 KADEME, 20 DEPARTMAN)")
A("### KADEME 0 — SAHİP")
A("Metin Durak. Nihai onay mercii: gelir taahhütleri, faz geçişleri, org değişiklikleri.")
A("### KADEME 1 — C-LEVEL (10 AJAN)")
for c in org["c_level"]:
    A(f"#### {c['title']}")
    A(f"Raporlar: {c['reports_to']} · Dosya: `components/agents/agency/c-level/{c['slug']}.md`")
    A(f"##### {c['slug']} · Misyon")
    A("Rol kartındaki Mission bölümü bağlayıcıdır.")
    A(f"##### {c['slug']} · KPI Seti")
    A("Rol kartındaki KPIs bölümü çeyreklik skorlanır.")
A("")
for d in org["departments"]:
    A(f"### DEPARTMAN — {d['name_en']} ({d['code'].upper()}) · {d['name_tr']}")
    A(f"#### {d['code'].upper()} · Künye")
    A(f"Sponsor C-level: **{d['sponsor']}** · Kadro: **{d['headcount']}** · Birimler: {', '.join(d['units'])} · Karışım: {d['mix']}")
    A(f"#### {d['code'].upper()} · Departman KPI'ları")
    for k in d["kpis"]:
        A(f"- {k}")
    A(f"#### {d['code'].upper()} · Toplantı Kadansı")
    A("Günlük async standup (07:30 TRT) · Haftalık departman sync (EVP başkanlık) · İki haftada bir birim retrosu · Aylık kurul (EVP katılır).")
    A(f"#### {d['code'].upper()} · Rol Kadrosu")
    for tier in TIER_ORDER:
        roles = [r for r in d["roles"] if r["tier"] == tier]
        if not roles:
            continue
        for r in roles:
            A(f"##### {r['title']}")
            A(f"`{r['slug']}` · {TIER_TR[tier]} · Raporlar: `{r['reports_to']}` · Kart: `components/agents/agency/{d['slug']}/{r['slug']}.md`")
A("")

# --- BÖLÜM IV
A("## BÖLÜM IV — 7/24 OPERASYON RİTMİ")
A("### Günlük Ritim (her gün, minimum 1 tam döngü)")
for h, t in [
 ("03:00 TRT — Gece Döngüsü", "nightly-improve: OKU→DAMIT→ÜRET→DOĞRULA→DAMGALA→COMMIT."),
 ("07:30 TRT — Günlük Standup", "gunluk-operasyon workflow: 20 departman satırı + nöbetçi 3 departman derin dalış → gundem/."),
 ("07:35 TRT — İş Listesi Güncelleme", "IS_LISTESI.md yeniden önceliklendirilir; biten işler arşive düşer."),
 ("07:40 TRT — Makale/Güncelleme", "Günde min 1: makale (makaleler/) veya bileşen güncellemesi; CMO hattı sahiplenir."),
 ("Gün İçi — Takip", "Actions durumu, issue triage, anomali bayrakları; INF departmanı nöbeti."),
]:
    A(f"#### {h}")
    A(t)
A("### Haftalık Ritim")
for h, t in [
 ("Pazartesi — Liderlik Sync", "C-level + 20 EVP; haftalık hedef kilitleme → toplantilar/."),
 ("Çarşamba — Gelir Pipeline Review", "CRO başkanlık; GELIR-MODELI-TAKIP.md güncellenir."),
 ("Cuma — Konsolidasyon", "Haftalık öğrenimler BILGI_TABANI.md'ye damıtılır; haftalık rapor yayınlanır."),
]:
    A(f"#### {h}")
    A(t)
A("### Aylık Ritim")
for h, t in [
 ("Ayın 1'i — Yönetim Kurulu", "aylik-kurul workflow: OKR skorlama, faz kapısı kararları, org revizyonu önerileri."),
 ("Ay Ortası — Kalite Denetimi", "TAL departmanı 30 rastgele ajan kartını rubrikle denetler."),
 ("Ay Sonu — Sürüm", "CPO: release notes + VERSIONS.md + plugin.json sürüm artışı."),
]:
    A(f"#### {h}")
    A(t)
A("### Nöbet (Follow-the-Sun) Sistemi")
for h, t in [
 ("Vardiyalar", "00–08 / 08–16 / 16–24 UTC; her rol kartında yazılıdır; C-level ve EVP follow-the-sun."),
 ("Nöbetçi Departmanlar", "Her gün 3 departman derin-dalış nöbetçisidir (deterministik rotasyon: gün-of-year mod 20)."),
 ("Kesinti Protokolü", "Actions kırmızı → INF 24h içinde müdahale; 48h'te CTO eskalasyonu."),
]:
    A(f"#### {h}")
    A(t)
A("")

# --- BÖLÜM V
A("## BÖLÜM V — TOPLANTI PROTOKOLLERİ")
for h, t in [
 ("Format Anayasası", "Her tutanak: katılımcılar (ajan slug'ları), kararlar, aksiyonlar (sahip+tarih), riskler, 🚩'lar."),
 ("Günlük Standup", "Async, yazılı; departman başına 1 satır: dün/bugün/blocker. Çıktı: gundem/YYYY-MM-DD-standup.md."),
 ("Haftalık Departman Sync", "EVP başkanlık; backlog önceliklendirme; çıktı toplantilar/'a."),
 ("Haftalık Liderlik Sync", "Pazartesi; C-level + EVP'ler; haftalık 3 önceliğin kilitlenmesi."),
 ("Gelir Pipeline Review", "Çarşamba; CRO+CFO+ilgili EVP'ler; kanal başına ilerleme + sonraki adım."),
 ("Aylık Yönetim Kurulu", "CEO başkanlık; OKR skorları; faz kapısı GEÇTİ/KALDI kararı; tutanak zorunlu."),
 ("Retro", "İki haftada bir, birim düzeyi; öğrenimler BILGI_TABANI.md'ye tek satır damıtılır."),
 ("Karar Kaydı", "Kurul kararları KARAR_LOGU formatında (K-no) AUDIT_LOG'a da yansır."),
]:
    A(f"### V.{h}")
    A(t)
A("")

# --- BÖLÜM VI
A("## BÖLÜM VI — WORKFLOW KATALOĞU (DEPARTMAN BAŞINA 3)")
for d in org["departments"]:
    A(f"### WF — {d['name_en']} ({d['code'].upper()})")
    A(f"#### {d['code'].upper()}-WF1 · Günlük Optimizasyon Döngüsü")
    A(f"Nöbetçi gün: {d['name_tr']} birikmiş işleri tarar, en yüksek etkili 3 aksiyonu üretir, standup'a yazar.")
    A(f"#### {d['code'].upper()}-WF2 · Haftalık Rapor Hattı")
    A(f"Analistler veri keser → lead anlatı yazar → EVP onaylar → haftalık konsolidasyona girer.")
    A(f"#### {d['code'].upper()}-WF3 · Deney/Test Pipeline'ı")
    A(f"Hipotez → tasarım → koşum → öğrenim (BILGI_TABANI.md'ye tek satır); örneklem disiplini zorunlu.")
A("")

# --- BÖLÜM VII
A("## BÖLÜM VII — GELİR MODELİ (5 KANAL)")
for kod, ad, sahip, ozet, adim in GELIR:
    A(f"### {kod} — {ad}")
    A(f"Sahip: {sahip}. {ozet}")
    for i, s in enumerate(adim, 1):
        A(f"#### {kod}.A{i} · {s.split('(')[0].strip()}")
        A(f"Hedef penceresi: {s[s.find('(')+1:s.find(')')] if '(' in s else 'F-planına bağlı'} · Durum takibi: docs/GELIR-MODELI-TAKIP.md")
A("")

# --- BÖLÜM VIII
A("## BÖLÜM VIII — YOL HARİTASI (DEADLINE'LI)")
for kod, tarih, ad, mils in FAZLAR:
    A(f"### {kod} — {ad} ({tarih})")
    for i, m in enumerate(mils, 1):
        A(f"#### {kod}.M{i} · {m}")
        A("Kapı kriteri: kanıt linki (commit/dosya/tutanak) olmadan GEÇTİ sayılmaz.")
A("")

# --- BÖLÜM IX
A("## BÖLÜM IX — KPI VE TAKİP")
for h, t in [
 ("Kuzey Yıldızı", "Aylık: (a) aktif gelir kanalı sayısı, (b) nitelikli lead sayısı, (c) bilgi tabanı sinyal artışı."),
 ("Operasyon KPI'ları", "Döngü yeşil oranı ≥ %99 · günlük üretim ≥ 1 · standup 7/7."),
 ("Marka KPI'ları", "Stars/watchers/forks trendi · dizin listeleme sayısı · makale sayısı."),
 ("Gelir KPI'ları", "Pipeline değeri · görüşme sayısı · imzalanan anlaşma · ilk gelir tarihi."),
 ("Kalite KPI'ları", "Doğrulama geçme oranı · denetim bulgu yoğunluğu · rework oranı."),
 ("Takip Yüzeyi 1 — AUDIT_LOG.jsonl", "Her işlem damgalı; zincir kırılmaz."),
 ("Takip Yüzeyi 2 — BILGI_TABANI.md", "Günlük damıtılmış öğrenim; append-only."),
 ("Takip Yüzeyi 3 — IS_LISTESI.md", "Canlı backlog; günlük yeniden önceliklendirme."),
 ("Takip Yüzeyi 4 — GELIR-MODELI-TAKIP.md", "Kanal başına durum + sonraki adım + sahip."),
 ("Takip Yüzeyi 5 — gundem/ ve toplantilar/", "Standup ve tutanak arşivi; tarih damgalı."),
 ("Takip Yüzeyi 6 — Actions", "3 cron workflow'un yeşilliği kamu kanıtıdır."),
 ("Raporlama Dili", "Sayı + tanım + kaynak; tanımsız KPI yayınlanamaz."),
]:
    A(f"### IX.{h}")
    A(t)
A("")

# --- BÖLÜM X
A("## BÖLÜM X — GÜNCELLEME VE BAKIM PROTOKOLÜ")
for h, t in [
 ("Org Değişikliği", "Sadece generate_org.py düzenlenir → yeniden koşulur → 600 assert → docs yeniden üretilir."),
 ("Ekosistem Güncellemesi", "Claude Code/MCP değişiklikleri (örn. MCP spec RC) 7 gün içinde POV + gerekli migration."),
 ("Bileşen Güncellemesi", "Her düzenleme: validate.py GEÇTİ + VERSIONS.md satırı + AUDIT damgası."),
 ("Bilgi Zinciri", "Her koşum önceki koşumun çıktısını okur (🔗); zincir kırılırsa DENETÇİ bulgusu."),
 ("Cowork Senkronu", "Cowork günlük gözetim görevi repo durumunu okur, ilerlemeyi proje dokümanına yazar."),
 ("Sürüm Yükseltme", "Ay sonu sürüm ritüeli; semver; breaking change'ler release notes'ta."),
 ("Arşivleme", "90 günden eski gundem/ dosyaları arsiv/ altına taşınır (silinmez)."),
 ("Bu Belgenin Bakımı", "Bu belge üretilir, elle düzenlenmez; delta = generator commit'i."),
]:
    A(f"### X.{h}")
    A(t)

master = "\n".join(L) + "\n"
n_headings = len(re.findall(r"(?m)^#{1,6} ", master))
master = master.replace("MASTER-PROMPT — ADOPS AI AGENCY (v2)",
                        f"MASTER-PROMPT — ADOPS AI AGENCY (v2) · {n_headings} başlık")
W("docs/MASTER-PROMPT-AJANS.md", master)
print(f"HEADINGS: {n_headings}")
assert n_headings >= 900, n_headings

# ============================================================================
# 2) ORG-SEMASI.md
# ============================================================================
S = []
S.append(f"# ORG ŞEMASI — ADOPS AI AGENCY (600 ajan)\n> Üretim: {NOW} · Kaynak: data/org.json\n")
S.append("```mermaid\nflowchart TD\n  OWNER[Metin Durak — Sahip] --> CEO[ceo-orchestrator]")
for c in org["c_level"]:
    if c["slug"] != "ceo-orchestrator":
        S.append(f"  CEO --> {c['slug'].replace('-', '_')}[{c['slug']}]")
for d in org["departments"]:
    S.append(f"  {d['sponsor'].replace('-', '_')} --> {d['code']}[{d['code'].upper()}: {d['name_en']} · {d['headcount']}]")
S.append("```\n")
S.append("| Departman | Kod | Sponsor | Kadro | EVP | Dir | Lead | Uzman | Analist |")
S.append("|---|---|---|---|---|---|---|---|---|")
for d in org["departments"]:
    m = d["mix"]
    S.append(f"| {d['name_en']} | {d['code'].upper()} | {d['sponsor']} | {d['headcount']} | {m['evp']} | {m['director']} | {m['lead']} | {m['specialist']} | {m['analyst']} |")
S.append(f"| **TOPLAM (+10 C-level)** | | | **600** | | | | | |")
S.append("\n## Tam kadro listesi\nHer rolün kartı: `components/agents/agency/<departman>/<slug>.md` · Tam envanter: `data/org.json`\n")
W("docs/ORG-SEMASI.md", "\n".join(S) + "\n")

# ============================================================================
# 3) TOPLANTI-PROTOKOLU.md
# ============================================================================
W("docs/TOPLANTI-PROTOKOLU.md", f"""# TOPLANTI PROTOKOLÜ
> Üretim: {NOW} · Tüm toplantılar yazılı/async üretilir; çıktısız toplantı yok.

| Toplantı | Kadans | Başkan | Katılım | Çıktı |
|---|---|---|---|---|
| Günlük Standup | Her gün 07:30 TRT | coo-delivery | 20 dept satırı + 3 nöbetçi derin dalış | gundem/YYYY-MM-DD-standup.md |
| Departman Sync | Haftalık | Departman EVP | Departman kadrosu | toplantilar/YYYY-MM-DD-<dept>.md |
| Liderlik Sync | Pazartesi | ceo-orchestrator | C-level + 20 EVP | toplantilar/YYYY-MM-DD-liderlik.md |
| Gelir Pipeline | Çarşamba | cro-revenue | CRO, CFO, NBD/PRT/PRD EVP | docs/GELIR-MODELI-TAKIP.md güncellemesi |
| Yönetim Kurulu | Ayın 1'i | ceo-orchestrator | C-level | toplantilar/YYYY-MM-kurul.md + K-no kararlar |
| Retro | 2 haftada bir | Birim direktörü | Birim | BILGI_TABANI.md'ye 1 satır öğrenim |

## Tutanak şablonu
```
# [Toplantı] — [Tarih]
Katılımcılar: [slug listesi]
## Kararlar
- K: ... (sahip, tarih)
## Aksiyonlar
- [ ] ... → sahip-slug · deadline
## Riskler / 🚩
- ...
```
""")

# ============================================================================
# 4) GELIR-MODELI-TAKIP.md
# ============================================================================
G = [f"# GELİR MODELİ TAKİP\n> Üretim: {NOW} · Haftalık Çarşamba review'da güncellenir. Sahip: cro-revenue.\n",
     "| Kanal | Sahip | Durum | İlerleme | Sonraki Adım | Deadline |",
     "|---|---|---|---|---|---|"]
for kod, ad, sahip, ozet, adim in GELIR:
    G.append(f"| {kod} — {ad} | {sahip.split('→')[1].strip()} | 🔴 BAŞLAMADI | 0% | {adim[0]} | {adim[0][adim[0].find('(')+1:adim[0].find(')')] if '(' in adim[0] else 'F2'} |")
G.append("\n## Kanal detayları\n")
for kod, ad, sahip, ozet, adim in GELIR:
    G.append(f"### {kod} — {ad}\n{ozet}\n")
    for s in adim:
        G.append(f"- [ ] {s}")
    G.append("")
G.append("## İlerleme günlüğü (append-only)\n| Tarih | Kanal | Olay | Kanıt |\n|---|---|---|---|")
G.append(f"| {TODAY} | TÜMÜ | Takip sistemi kuruldu, kanallar tanımlandı | docs/MASTER-PROMPT-AJANS.md BÖLÜM VII |")
W("docs/GELIR-MODELI-TAKIP.md", "\n".join(G) + "\n")

# ============================================================================
# 5) YOL-HARITASI.md
# ============================================================================
Y = [f"# YOL HARİTASI — DEADLINE'LI\n> Üretim: {NOW} · Faz kapısı: kanıtsız GEÇTİ yok. Aylık kurulda skorlanır.\n",
     "| Faz | Tarih | Ad | Kapı Kriterleri |", "|---|---|---|---|"]
for kod, tarih, ad, mils in FAZLAR:
    Y.append(f"| {kod} | {tarih} | {ad} | {' · '.join(mils)} |")
Y.append("\n## Faz detayları\n")
for kod, tarih, ad, mils in FAZLAR:
    Y.append(f"### {kod} — {ad} ({tarih})")
    for m in mils:
        Y.append(f"- [ ] {m}")
    Y.append("")
W("docs/YOL-HARITASI.md", "\n".join(Y) + "\n")

# ============================================================================
# 6) IS_LISTESI.md — canlı backlog
# ============================================================================
I = [f"# İŞ LİSTESİ (CANLI)\n> Son güncelleme: {NOW} · Günlük 07:35 TRT'de gunluk-operasyon workflow'u yeniden önceliklendirir.\n",
     "## P0 — Bu hafta (F0/F1)",
     "- [ ] v2 push + Actions yeşil → inf-evp-tech-infra · 2026-07-18",
     "- [ ] ANTHROPIC_API_KEY secret kontrolü → cto-platform · 2026-07-18",
     "- [ ] İlk 5 günlük döngünün kesintisiz koşması → coo-delivery · 2026-07-24",
     "- [ ] README inbound CTA taslağı → nbd-evp-new-business · 2026-07-24",
     "\n## P1 — F2 penceresi",
     "- [ ] Sponsor hedef listesi (20 firma) → prt-evp-partnerships-sponsorships · 2026-07-31",
     "- [ ] 3 dizin listeleme başvurusu → cmo-brand · 2026-07-31",
     "- [ ] 5 makale planı (makaleler/) → seo-evp-seo-content · 2026-07-31",
     "\n## Departman kuyrukları"]
for d in org["departments"]:
    I.append(f"### {d['code'].upper()} — {d['name_tr']}")
    I.append(f"- [ ] {d['units'][0]} playbook'unu v2 yapısına bağla → {d['roles'][0]['slug']}")
    I.append(f"- [ ] Haftalık rapor şablonunu doldurmaya başla → analist hattı")
I.append("\n## Arşiv\n(biten işler buraya taşınır — silinmez)")
W("IS_LISTESI.md", "\n".join(I) + "\n")

# ============================================================================
# 7) loop + commands
# ============================================================================
W("components/loops/operations/ajans-7-24-loop.md", f"""---
name: ajans-7-24-loop
description: 7/24 agency heartbeat — chains nightly-improve, daily standup/work-list/article, weekly leadership + revenue reviews, monthly board into one unbroken loop.
---
# Ajans 7/24 Döngüsü
**TR:** Ajansın kalp atışı. Cron zinciri: 03:00 nightly → 07:30 standup → 07:35 iş listesi → 07:40 makale → hafta içi review'lar → ayın 1'i kurul.

## Chain
1. nightly-improve (00:00 UTC) — read→distill→produce→validate→stamp→commit
2. gunluk-operasyon (04:30 UTC) — standup + IS_LISTESI + article + tracking
3. haftalik-toplanti (Mon 06:00 UTC) — leadership minutes + weekly consolidation
4. aylik-kurul (1st, 06:00 UTC) — OKR scoring + phase-gate decisions

## Invariants
- Every run appends AUDIT_LOG.jsonl and one learning line to BILGI_TABANI.md.
- A red run must be triaged within 24h (INF on-call), escalated to cto-platform at 48h.
""")

W("components/commands/agency/gunluk-standup.md", """---
description: Produce today's 20-department standup — one line each (yesterday/today/blocker) plus deep-dives for the 3 on-duty departments, written to gundem/.
---
# /gunluk-standup
Read data/org.json and IS_LISTESI.md. Output gundem/YYYY-MM-DD-standup.md:
one line per department (dün/bugün/blocker), deep-dive for the 3 on-duty departments
(rotation: day-of-year mod 20), unresolved blockers escalated per MASTER-PROMPT BÖLÜM V.
**TR:** Günlük standup üretir; nöbetçi 3 departmana derin dalış.
""")

W("components/commands/agency/toplanti-tutanagi.md", """---
description: Generate meeting minutes (participants, decisions, actions with owner+deadline, risks) in the standard template and file them under toplantilar/.
---
# /toplanti-tutanagi
Given meeting type (dept sync / liderlik / gelir / kurul) and agenda, produce minutes using
docs/TOPLANTI-PROTOKOLU.md template. Decisions get K-numbers when board-level. File under toplantilar/.
**TR:** Standart şablonla tutanak üretir; kurul kararlarına K-no verir.
""")

W("components/commands/agency/makale-uret.md", """---
description: Produce the daily article (performance marketing / programmatic / Claude Code ecosystem) into makaleler/ with sources, TR summary, and a repo-relevant CTA.
---
# /makale-uret
Pick next topic from the editorial rotation (SEO dept owns it). Output makaleler/YYYY-MM-DD-<slug>.md:
600-1200 words, sources cited, 3-line TR özet, one CTA linking back to the repo (inbound funnel K5).
**TR:** Günlük makale; kaynaklı, TR özetli, CTA'lı.
""")

print("DOCS DONE")
