#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ÖZ-DENETİM SORU BANKASI — 560+ soru üretir.
Çıktı: docs/OZ-DENETIM-SORU-BANKASI.md (insan) + data/soru_bankasi.json (jeneratör girdisi).
Her ajan kartı buradan departman+kademe alt-setini çeker; günlük döngü her koşumda örnekler."""
import json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
org = json.load(open(os.path.join(ROOT, "data", "org.json"), encoding="utf-8"))

# --- Evrensel kategoriler (elle yazılmış, tüm rollere uygulanır) ---
UNIVERSAL = {
"Strateji": [
 "Bu iş ajansın çeyreklik OKR'ının hangisine hizmet ediyor; edmiyorsa neden kuyrukta?",
 "Bugünkü en yüksek etkili 3 aksiyonu doğru sıraladım mı; kanıt ne?",
 "Bu kararı 3 ay sonra savunabilir miyim; hangi varsayıma dayanıyor?",
 "Rakip/pazar hareketine 7 gün içinde POV ürettim mi?",
 "Kaynağı en yüksek marjinal getiriye mi tahsis ettim, alışkanlığa mı?",
 "Bu hedef matematiksel olarak mümkün mü; değilse 🚩 verdim mi?",
],
"Yürütme": [
 "Çıktı kopyala-yapıştır hazır mı; alıcı ek iş yapmadan kullanabilir mi?",
 "Bir sonraki adımın sahibi ve tarihi net mi?",
 "Bloklayıcı 4 saati aştı mı; aştıysa eskale ettim mi?",
 "Bu görevi tekrarlanabilir bir checklist'e dönüştürebilir miyim?",
 "Dünkü taahhüdümü bugün kapattım mı; kapatmadıysam neden?",
 "İşi en küçük çalışan parçaya böldüm mü?",
],
"Kalite-Doğrulama": [
 "6 katmanın (structural/integrity/semantic/reference/known-patterns/review) hepsinden geçti mi?",
 "SHA256 bütünlük satırı VERSIONS.md'de güncel mi?",
 "Bağımsız bir gözle (ikinci ajan) review aldım mı?",
 "Rework oranım artıyor mu; kök neden ne?",
 "Bu çıktıda tehlikeli desen (enjeksiyon/SSRF) taraması yaptım mı?",
],
"Veri-Dürüstlüğü": [
 "Sunduğum her sayı gerçek bir kaynaktan mı; tahminleri açıkça etiketledim mi?",
 "Örneklem büyüklüğü sonucu taşıyacak kadar mı?",
 "Anomaliyi büyüklük + hipotezle mi raporladım?",
 "KPI'nın tanımı yazılı mı; tanımsız metrik yayınlamadım değil mi?",
 "Korelasyonu nedensellik gibi sunmadım değil mi?",
],
"Güvenlik-5Kural": [
 "Resmi kaynak (Anthropic/MCP) varken topluluk kaynağına mı gittim?",
 "Script bundle eden bileşeni okumadan/özetlemeden çalıştırdım mı?",
 "'Son commit dün' diye güvenlik varsaydım mı (güncellik yanılgısı)?",
 "Kurulumu kanonik org'dan mı yaptım, fork'tan mı?",
 "Marketplace-öncelik katmanını kontrol ettim mi?",
],
"Gelir": [
 "Bu iş 5 gelir kanalından (sponsorluk/placement/referral/premium/inbound) hangisini ilerletiyor?",
 "Inbound lead yolu (README→iletişim) çalışır durumda mı?",
 "Referral fırsatını (Supermetrics vb.) kaçırdım mı?",
 "Pipeline değerini bu hafta güncelledim mi?",
 "Bir sponsor/vendor görüşmesini ilerletmek için bugün ne yaptım?",
],
"Öğrenme": [
 "Bugün en az 1 kaynak (changelog/makale) okudum mu; öğrenimi damıttım mı?",
 "Bu öğrenim BILGI_TABANI.md'ye tek satır olarak girdi mi?",
 "Departmanımın platformunda (panel) bu hafta ne değişti; takip ettim mi?",
 "İlgili sertifika/eğitimden bir modül tamamladım mı?",
 "Bir beta/yeni ürün özelliğini test edip not aldım mı?",
 "Önceki koşumun çıktısını okudum mu (zincir 🔗 kırılmadı mı)?",
],
"Toplantı": [
 "Standup satırım dün/bugün/blocker formatında ve tek satır mı?",
 "Tutanakta karar + aksiyon(sahip+tarih) + risk + 🚩 var mı?",
 "Kurul kararına K-no verdim mi?",
 "Toplantı çıktısız mı bitti (çıktısız toplantı yok)?",
],
"Eskalasyon": [
 "Bütçe/politika riskini fin/leg'e ilettim mi?",
 "İmkânsız hedefi 🚩 [ne]·[neden]·[alternatif] formatında mı verdim?",
 "Sessiz kalıp riski gömdüm mü?",
 "Cross-departman çakışmayı doğru mercie taşıdım mı?",
],
"Ölçümleme": [
 "Bu aksiyonun başarısını hangi metrikle ve ne zaman ölçeceğim?",
 "Atıf modeli/ölçüm yöntemi playbook'ta belgeli mi?",
 "Holdout/artımsallık düşündüm mü?",
 "Dashboard SLA'sını tutturdum mu?",
],
"Dokümantasyon": [
 "Bu işi başka bir ajan benim yardımım olmadan tekrarlayabilir mi?",
 "Artefaktı zaman damgaladım mı?",
 "Playbook'u güncel tuttum mu?",
],
"Önceliklendirme": [
 "P0 işleri gerçekten P0 mı; yoksa kolay olanı mı önce yaptım?",
 "Biten işi arşive taşıdım mı?",
 "IS_LISTESI'ni bugün yeniden önceliklendirdim mi?",
],
"Risk": [
 "Bu değişikliğin geri-alma (rollback) planı var mı?",
 "En kötü senaryo ne; sinyalini nasıl erken yakalarım?",
 "Tek nokta bağımlılık yarattım mı?",
],
"İşbirliği": [
 "Yukarı/yatay/aşağı arayüzlerimi bugün bilgilendirdim mi?",
 "Başka bir departmanın işini kolaylaştırmak için ne yaptım?",
 "Devrettiğim işin sahibi net mi?",
],
"Etik-Uyum": [
 "Reklam politikası açısından bu çıktı temiz mi?",
 "KVKK/GDPR açısından veri işleme uygun mu?",
 "Lisans (MIT) hijyenine uydum mu?",
 "Gerçek kişilere atfen sahte içerik üretmedim değil mi?",
],
"Otomasyon": [
 "Bu manuel işi bir workflow'a çevirebilir miyim?",
 "Actions yeşil mi; kırmızıysa 24h içinde müdahale ettim mi?",
 "Idempotent mi çalışıyor (yeniden koşum bozmuyor mu)?",
],
"Müşteri": [
 "Bu çıktı bir müşteri sorusunu/ihtiyacını gerçekten çözüyor mu?",
 "Rapor anlatısı sayı+bağlam+sonraki adım içeriyor mu?",
 "Churn/риск sinyalini 14 gün önceden işaretledim mi?",
],
"İnovasyon-Beta": [
 "Bu hafta hangi beta ürünü/özelliği denedim; bulgum ne?",
 "Rakiplerin denemediği bir açı buldum mu?",
 "Deneyi hipotez→tasarım→koşum→öğrenim döngüsüyle mi yürüttüm?",
],
"Makale-İçerik": [
 "Bugünün makalesi kaynaklı, TR özetli ve CTA'lı mı?",
 "İçerik ajansın inbound hunisine (K5) hizmet ediyor mu?",
 "Editoryal rotasyondan sıradaki konuyu seçtim mi?",
],
"Öz-Gelişim": [
 "Bu rolün ilk-30-gün hedeflerinin neresindeyim?",
 "Anti-desenlerimden birine bugün düştüm mü?",
 "Bir sonraki kademeye hazırlık için hangi beceriyi geliştiriyorum?",
],
"Eğitim-Sertifika": [
 "Rolümle ilgili bir sertifika (Skillshop/Blueprint vb.) modülünü bu hafta ilerlettim mi?",
 "Yeni öğrendiğim bir tekniği bir çıktıya uyguladım mı?",
 "Ekipteki başka bir ajana öğrettiğim/aktardığım bir şey oldu mu?",
 "Bilgi açığımı (skill gap) isimlendirdim mi; kapatma planı ne?",
],
"Panel-Güncelleme-Takibi": [
 "Departmanımın platform changelog'unu bu hafta okudum mu?",
 "Bir API/politika değişikliği mevcut kurulumu etkiliyor mu; migration gerekli mi?",
 "Deprecation/sunset uyarısı var mı; takvime aldım mı?",
 "Yeni bir panel özelliği iş akışımı hızlandırır mı?",
],
"Kaynak-Okuma": [
 "Bugün okuduğum kaynağın URL'ini nota ekledim mi?",
 "Okuduğumdan çıkan tek somut aksiyon ne?",
 "Kaynağın güvenilirliğini (resmi>çapraz-konsensüs>geçmiş>yıldız) değerlendirdim mi?",
 "Çelişen iki kaynağı nasıl uzlaştırdım?",
],
"Süreç-Zinciri": [
 "Bu koşum önceki koşumun çıktısını girdi aldı mı (🔗)?",
 "ts_start ve ts_end damgaladım mı?",
 "Zincir kırılırsa DENETÇİ bulgusu düşer mi; kontrol ettim mi?",
 "Bir sonraki koşuma net bir girdi bıraktım mı?",
],
"Pazar-Rekabet": [
 "Rakip bir hamle yaptı mı; 7 gün içinde POV çıkardım mı?",
 "Sektör benchmark'ımı bu ay tazeledim mi?",
 "Rakiplerin sahiplenmediği bir konumlanma açığı var mı?",
 "Bir pazar sinyalini erken yakalayıp aksiyona çevirdim mi?",
],
"Verimlilik-Token": [
 "Çıktıyı minimum token ile (progressive disclosure) mı ürettim?",
 "Aynı analizi tekrarladım mı; BILGI_TABANI'nda zaten var mıydı?",
 "Ağır içeriği docs/'a koyup kartı kısa mı tuttum?",
 "Çoklu benzer işlemi tek çağrıda grupladım mı?",
 "Dolgu cümle ürettim mi; sinyal/uzunluk oranım iyi mi?",
],
"Toparlama-Retro": [
 "Bu iş bölümünün retrosundan tek satır öğrenim çıktı mı?",
 "Tekrar eden bir hatayı kalıcı düzelttim mi (kök neden)?",
 "Bir sonraki sprint için taşınacak riski işaretledim mi?",
],
"Sahiplik-Hesapverebilirlik": [
 "Bu işin tek net sahibi ben miyim; belirsizlik bıraktım mı?",
 "Bir hatayı savunmaya geçmeden sahiplendim mi?",
 "Taahhüt ettiğim tarihi tutuyor muyum; tutmuyorsam erken haber verdim mi?",
 "Başkasının işini beklerken kendi tarafımı hazır tuttum mu?",
 "Sessiz kalarak bir riski gömdüm mü?",
 "Kararımın kanıtını (link/commit/dosya) bıraktım mı?",
 "Bu çıktı için 'definition of done' karşılandı mı?",
 "Bugün ajansı bir adım ileri götüren en somut şey neydi?",
 "Yarına devrettiğim en kritik açık madde ne; sahibi kim?",
 "Bu işi baştan yapsam neyi farklı yapardım?",
 "Ölçebildiğim bir ilerleme kaydettim mi, yoksa sadece meşgul mü göründüm?",
],
}

# --- Departman-özel sorular (unit/topic/kpi'dan üretilir) ---
by_dept = {}
for d in org["departments"]:
    qs = []
    for u in d["units"]:
        qs.append(f"{u} birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?")
        qs.append(f"{u} çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?")
        qs.append(f"{u} alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?")
    for k in d["kpis"]:
        qs.append(f"KPI '{k}' hedefte mi; sapma varsa kök neden ve düzeltme ne?")
        qs.append(f"'{k}' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?")
    by_dept[d["code"]] = qs

# --- Kademe-özel sorular ---
by_tier = {
"C-LEVEL": [
 "Ajans OKR attainment'ı %80 üstünde mi; değilse kurtarma planı ne?",
 "Bir faz kapısını kanıtsız GEÇTİ saymadım değil mi?",
 "Mikro-yönetime kaydım mı; yetkiyi doğru devrettim mi?",
 "Sahibe danışmadan bir taahhüt verdim mi?",
 "5 gelir kanalının hepsinin sahibi ve durumu net mi?",
 "Kurul gündemini kanıt-linkli hazırladım mı?",
],
"EVP": [
 "Departman OKR skoru güncel mi; kırmızı OKR için plan var mı?",
 "Kadroyu aşırı yükledim mi; kapasite dengeli mi?",
 "Playbook'u merge öncesi onayladım mı?",
 "Haftalık departman raporu yayınlandı mı?",
 "Sponsor C-level'a haftalık raporladım mı?",
],
"DIRECTOR": [
 "Birim backlog'u doğru önceliklendi mi?",
 "Uzman çıktısını publish öncesi review ettim mi?",
 "Birim retrosundan öğrenim damıttım mı?",
 "Cross-unit çakışmayı EVP'ye taşıdım mı?",
],
"LEAD": [
 "İş akışı standardı/checklist güncel mi?",
 "Uzman görevlerini günlük atadım/review ettim mi?",
 "Haftalık iş akışı özetini yazdım mı?",
 "Riski metrik kanıtıyla mı bayrakladım?",
],
"SPECIALIST": [
 "Çıktım kopyala-hazır ve checklist'li mi?",
 "Bu hafta playbook'a 1 iyileştirme önerdim mi?",
 "İşi metrik gerekçesi olmadan mı sundum?",
 "Damgasız çıktı bıraktım mı?",
],
"ANALYST": [
 "Veri kesitim tanım-ekli mi?",
 "Anomaliyi büyüklük+hipotezle mi işaretledim?",
 "Tahmini açıkça etiketledim mi?",
 "Veri uydurmadım değil mi?",
],
}

# --- Yaz ---
os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
bank = {"generated_utc": NOW, "universal": UNIVERSAL, "by_dept": by_dept, "by_tier": by_tier}
json.dump(bank, open(os.path.join(ROOT, "data", "soru_bankasi.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

total = sum(len(v) for v in UNIVERSAL.values()) + sum(len(v) for v in by_dept.values()) + sum(len(v) for v in by_tier.values())
L = [f"# ÖZ-DENETİM SORU BANKASI ({total} soru)",
     f"> Üretim: {NOW} · Kaynak: scripts/build_question_bank.py · data/soru_bankasi.json",
     "Her ajan her süreçte kendine bu soruları sorar. Günlük döngü (scripts/daily_ops.py) her koşumda örnek çeker ve standup'ta yanıtlar. Kart başına alt-set: departman + kademe blokları.",
     ""]
n = 0
L.append("## A. Evrensel sorular (tüm roller)")
for cat, qs in UNIVERSAL.items():
    L.append(f"### {cat}")
    for q in qs:
        n += 1; L.append(f"{n}. {q}")
L.append("\n## B. Departman soruları")
for d in org["departments"]:
    L.append(f"### {d['code'].upper()} — {d['name_tr']}")
    for q in by_dept[d["code"]]:
        n += 1; L.append(f"{n}. {q}")
L.append("\n## C. Kademe soruları")
for tier, qs in by_tier.items():
    L.append(f"### {tier}")
    for q in qs:
        n += 1; L.append(f"{n}. {q}")
open(os.path.join(ROOT, "docs", "OZ-DENETIM-SORU-BANKASI.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print(f"SORU BANKASI: {total} soru -> docs/OZ-DENETIM-SORU-BANKASI.md + data/soru_bankasi.json")
assert total >= 500, total
