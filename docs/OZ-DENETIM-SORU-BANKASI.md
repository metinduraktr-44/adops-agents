# ÖZ-DENETİM SORU BANKASI (501 soru)
> Üretim: 2026-07-17T10:48:31Z · Kaynak: scripts/build_question_bank.py · data/soru_bankasi.json
Her ajan her süreçte kendine bu soruları sorar. Günlük döngü (scripts/daily_ops.py) her koşumda örnek çeker ve standup'ta yanıtlar. Kart başına alt-set: departman + kademe blokları.

## A. Evrensel sorular (tüm roller)
### Strateji
1. Bu iş ajansın çeyreklik OKR'ının hangisine hizmet ediyor; edmiyorsa neden kuyrukta?
2. Bugünkü en yüksek etkili 3 aksiyonu doğru sıraladım mı; kanıt ne?
3. Bu kararı 3 ay sonra savunabilir miyim; hangi varsayıma dayanıyor?
4. Rakip/pazar hareketine 7 gün içinde POV ürettim mi?
5. Kaynağı en yüksek marjinal getiriye mi tahsis ettim, alışkanlığa mı?
6. Bu hedef matematiksel olarak mümkün mü; değilse 🚩 verdim mi?
### Yürütme
7. Çıktı kopyala-yapıştır hazır mı; alıcı ek iş yapmadan kullanabilir mi?
8. Bir sonraki adımın sahibi ve tarihi net mi?
9. Bloklayıcı 4 saati aştı mı; aştıysa eskale ettim mi?
10. Bu görevi tekrarlanabilir bir checklist'e dönüştürebilir miyim?
11. Dünkü taahhüdümü bugün kapattım mı; kapatmadıysam neden?
12. İşi en küçük çalışan parçaya böldüm mü?
### Kalite-Doğrulama
13. 6 katmanın (structural/integrity/semantic/reference/known-patterns/review) hepsinden geçti mi?
14. SHA256 bütünlük satırı VERSIONS.md'de güncel mi?
15. Bağımsız bir gözle (ikinci ajan) review aldım mı?
16. Rework oranım artıyor mu; kök neden ne?
17. Bu çıktıda tehlikeli desen (enjeksiyon/SSRF) taraması yaptım mı?
### Veri-Dürüstlüğü
18. Sunduğum her sayı gerçek bir kaynaktan mı; tahminleri açıkça etiketledim mi?
19. Örneklem büyüklüğü sonucu taşıyacak kadar mı?
20. Anomaliyi büyüklük + hipotezle mi raporladım?
21. KPI'nın tanımı yazılı mı; tanımsız metrik yayınlamadım değil mi?
22. Korelasyonu nedensellik gibi sunmadım değil mi?
### Güvenlik-5Kural
23. Resmi kaynak (Anthropic/MCP) varken topluluk kaynağına mı gittim?
24. Script bundle eden bileşeni okumadan/özetlemeden çalıştırdım mı?
25. 'Son commit dün' diye güvenlik varsaydım mı (güncellik yanılgısı)?
26. Kurulumu kanonik org'dan mı yaptım, fork'tan mı?
27. Marketplace-öncelik katmanını kontrol ettim mi?
### Gelir
28. Bu iş 5 gelir kanalından (sponsorluk/placement/referral/premium/inbound) hangisini ilerletiyor?
29. Inbound lead yolu (README→iletişim) çalışır durumda mı?
30. Referral fırsatını (Supermetrics vb.) kaçırdım mı?
31. Pipeline değerini bu hafta güncelledim mi?
32. Bir sponsor/vendor görüşmesini ilerletmek için bugün ne yaptım?
### Öğrenme
33. Bugün en az 1 kaynak (changelog/makale) okudum mu; öğrenimi damıttım mı?
34. Bu öğrenim BILGI_TABANI.md'ye tek satır olarak girdi mi?
35. Departmanımın platformunda (panel) bu hafta ne değişti; takip ettim mi?
36. İlgili sertifika/eğitimden bir modül tamamladım mı?
37. Bir beta/yeni ürün özelliğini test edip not aldım mı?
38. Önceki koşumun çıktısını okudum mu (zincir 🔗 kırılmadı mı)?
### Toplantı
39. Standup satırım dün/bugün/blocker formatında ve tek satır mı?
40. Tutanakta karar + aksiyon(sahip+tarih) + risk + 🚩 var mı?
41. Kurul kararına K-no verdim mi?
42. Toplantı çıktısız mı bitti (çıktısız toplantı yok)?
### Eskalasyon
43. Bütçe/politika riskini fin/leg'e ilettim mi?
44. İmkânsız hedefi 🚩 [ne]·[neden]·[alternatif] formatında mı verdim?
45. Sessiz kalıp riski gömdüm mü?
46. Cross-departman çakışmayı doğru mercie taşıdım mı?
### Ölçümleme
47. Bu aksiyonun başarısını hangi metrikle ve ne zaman ölçeceğim?
48. Atıf modeli/ölçüm yöntemi playbook'ta belgeli mi?
49. Holdout/artımsallık düşündüm mü?
50. Dashboard SLA'sını tutturdum mu?
### Dokümantasyon
51. Bu işi başka bir ajan benim yardımım olmadan tekrarlayabilir mi?
52. Artefaktı zaman damgaladım mı?
53. Playbook'u güncel tuttum mu?
### Önceliklendirme
54. P0 işleri gerçekten P0 mı; yoksa kolay olanı mı önce yaptım?
55. Biten işi arşive taşıdım mı?
56. IS_LISTESI'ni bugün yeniden önceliklendirdim mi?
### Risk
57. Bu değişikliğin geri-alma (rollback) planı var mı?
58. En kötü senaryo ne; sinyalini nasıl erken yakalarım?
59. Tek nokta bağımlılık yarattım mı?
### İşbirliği
60. Yukarı/yatay/aşağı arayüzlerimi bugün bilgilendirdim mi?
61. Başka bir departmanın işini kolaylaştırmak için ne yaptım?
62. Devrettiğim işin sahibi net mi?
### Etik-Uyum
63. Reklam politikası açısından bu çıktı temiz mi?
64. KVKK/GDPR açısından veri işleme uygun mu?
65. Lisans (MIT) hijyenine uydum mu?
66. Gerçek kişilere atfen sahte içerik üretmedim değil mi?
### Otomasyon
67. Bu manuel işi bir workflow'a çevirebilir miyim?
68. Actions yeşil mi; kırmızıysa 24h içinde müdahale ettim mi?
69. Idempotent mi çalışıyor (yeniden koşum bozmuyor mu)?
### Müşteri
70. Bu çıktı bir müşteri sorusunu/ihtiyacını gerçekten çözüyor mu?
71. Rapor anlatısı sayı+bağlam+sonraki adım içeriyor mu?
72. Churn/риск sinyalini 14 gün önceden işaretledim mi?
### İnovasyon-Beta
73. Bu hafta hangi beta ürünü/özelliği denedim; bulgum ne?
74. Rakiplerin denemediği bir açı buldum mu?
75. Deneyi hipotez→tasarım→koşum→öğrenim döngüsüyle mi yürüttüm?
### Makale-İçerik
76. Bugünün makalesi kaynaklı, TR özetli ve CTA'lı mı?
77. İçerik ajansın inbound hunisine (K5) hizmet ediyor mu?
78. Editoryal rotasyondan sıradaki konuyu seçtim mi?
### Öz-Gelişim
79. Bu rolün ilk-30-gün hedeflerinin neresindeyim?
80. Anti-desenlerimden birine bugün düştüm mü?
81. Bir sonraki kademeye hazırlık için hangi beceriyi geliştiriyorum?
### Eğitim-Sertifika
82. Rolümle ilgili bir sertifika (Skillshop/Blueprint vb.) modülünü bu hafta ilerlettim mi?
83. Yeni öğrendiğim bir tekniği bir çıktıya uyguladım mı?
84. Ekipteki başka bir ajana öğrettiğim/aktardığım bir şey oldu mu?
85. Bilgi açığımı (skill gap) isimlendirdim mi; kapatma planı ne?
### Panel-Güncelleme-Takibi
86. Departmanımın platform changelog'unu bu hafta okudum mu?
87. Bir API/politika değişikliği mevcut kurulumu etkiliyor mu; migration gerekli mi?
88. Deprecation/sunset uyarısı var mı; takvime aldım mı?
89. Yeni bir panel özelliği iş akışımı hızlandırır mı?
### Kaynak-Okuma
90. Bugün okuduğum kaynağın URL'ini nota ekledim mi?
91. Okuduğumdan çıkan tek somut aksiyon ne?
92. Kaynağın güvenilirliğini (resmi>çapraz-konsensüs>geçmiş>yıldız) değerlendirdim mi?
93. Çelişen iki kaynağı nasıl uzlaştırdım?
### Süreç-Zinciri
94. Bu koşum önceki koşumun çıktısını girdi aldı mı (🔗)?
95. ts_start ve ts_end damgaladım mı?
96. Zincir kırılırsa DENETÇİ bulgusu düşer mi; kontrol ettim mi?
97. Bir sonraki koşuma net bir girdi bıraktım mı?
### Pazar-Rekabet
98. Rakip bir hamle yaptı mı; 7 gün içinde POV çıkardım mı?
99. Sektör benchmark'ımı bu ay tazeledim mi?
100. Rakiplerin sahiplenmediği bir konumlanma açığı var mı?
101. Bir pazar sinyalini erken yakalayıp aksiyona çevirdim mi?
### Verimlilik-Token
102. Çıktıyı minimum token ile (progressive disclosure) mı ürettim?
103. Aynı analizi tekrarladım mı; BILGI_TABANI'nda zaten var mıydı?
104. Ağır içeriği docs/'a koyup kartı kısa mı tuttum?
105. Çoklu benzer işlemi tek çağrıda grupladım mı?
106. Dolgu cümle ürettim mi; sinyal/uzunluk oranım iyi mi?
### Toparlama-Retro
107. Bu iş bölümünün retrosundan tek satır öğrenim çıktı mı?
108. Tekrar eden bir hatayı kalıcı düzelttim mi (kök neden)?
109. Bir sonraki sprint için taşınacak riski işaretledim mi?
### Sahiplik-Hesapverebilirlik
110. Bu işin tek net sahibi ben miyim; belirsizlik bıraktım mı?
111. Bir hatayı savunmaya geçmeden sahiplendim mi?
112. Taahhüt ettiğim tarihi tutuyor muyum; tutmuyorsam erken haber verdim mi?
113. Başkasının işini beklerken kendi tarafımı hazır tuttum mu?
114. Sessiz kalarak bir riski gömdüm mü?
115. Kararımın kanıtını (link/commit/dosya) bıraktım mı?
116. Bu çıktı için 'definition of done' karşılandı mı?
117. Bugün ajansı bir adım ileri götüren en somut şey neydi?
118. Yarına devrettiğim en kritik açık madde ne; sahibi kim?
119. Bu işi baştan yapsam neyi farklı yapardım?
120. Ölçebildiğim bir ilerleme kaydettim mi, yoksa sadece meşgul mü göründüm?

## B. Departman soruları
### PRG — Programatik Satın Alma
121. Open Auction & Curation birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
122. Open Auction & Curation çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
123. Open Auction & Curation alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
124. PMP & Deals birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
125. PMP & Deals çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
126. PMP & Deals alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
127. CTV / OTT birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
128. CTV / OTT çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
129. CTV / OTT alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
130. DOOH & Audio birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
131. DOOH & Audio çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
132. DOOH & Audio alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
133. Bid Algorithms birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
134. Bid Algorithms çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
135. Bid Algorithms alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
136. KPI 'Viewability ≥ 70%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
137. 'Viewability ≥ 70%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
138. KPI 'Supply-path cost ≤ 15%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
139. 'Supply-path cost ≤ 15%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
140. KPI 'PMP share of spend on target' hedefte mi; sapma varsa kök neden ve düzeltme ne?
141. 'PMP share of spend on target' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
142. KPI 'eCPM/CPA vs plan' hedefte mi; sapma varsa kök neden ve düzeltme ne?
143. 'eCPM/CPA vs plan' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### SEA — Ücretli Arama
144. Google Ads Core birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
145. Google Ads Core çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
146. Google Ads Core alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
147. SA360 & Automation birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
148. SA360 & Automation çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
149. SA360 & Automation alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
150. PMax & Shopping birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
151. PMax & Shopping çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
152. PMax & Shopping alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
153. Microsoft Ads birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
154. Microsoft Ads çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
155. Microsoft Ads alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
156. KPI 'Impression share on brand ≥ 90%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
157. 'Impression share on brand ≥ 90%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
158. KPI 'Wasted spend < 5%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
159. 'Wasted spend < 5%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
160. KPI 'tCPA/tROAS attainment' hedefte mi; sapma varsa kök neden ve düzeltme ne?
161. 'tCPA/tROAS attainment' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
162. KPI 'QS trend up' hedefte mi; sapma varsa kök neden ve düzeltme ne?
163. 'QS trend up' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### SOC — Ücretli Sosyal
164. Meta birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
165. Meta çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
166. Meta alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
167. TikTok birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
168. TikTok çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
169. TikTok alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
170. LinkedIn & X birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
171. LinkedIn & X çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
172. LinkedIn & X alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
173. Snap & Pinterest birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
174. Snap & Pinterest çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
175. Snap & Pinterest alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
176. Creative Testing birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
177. Creative Testing çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
178. Creative Testing alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
179. KPI 'Thumbstop/hook rate on target' hedefte mi; sapma varsa kök neden ve düzeltme ne?
180. 'Thumbstop/hook rate on target' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
181. KPI 'CAPI EMQ ≥ 8' hedefte mi; sapma varsa kök neden ve düzeltme ne?
182. 'CAPI EMQ ≥ 8' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
183. KPI 'Creative refresh cadence met' hedefte mi; sapma varsa kök neden ve düzeltme ne?
184. 'Creative refresh cadence met' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
185. KPI 'Blended CPA vs plan' hedefte mi; sapma varsa kök neden ve düzeltme ne?
186. 'Blended CPA vs plan' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### MOB — Mobil UA & Uygulama
187. Apple Search Ads birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
188. Apple Search Ads çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
189. Apple Search Ads alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
190. Google App Campaigns birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
191. Google App Campaigns çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
192. Google App Campaigns alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
193. MMP (Adjust/AppsFlyer) birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
194. MMP (Adjust/AppsFlyer) çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
195. MMP (Adjust/AppsFlyer) alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
196. Retargeting & CRM birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
197. Retargeting & CRM çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
198. Retargeting & CRM alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
199. KPI 'SKAN CV coverage ≥ 85%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
200. 'SKAN CV coverage ≥ 85%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
201. KPI 'Fraud rate < 3%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
202. 'Fraud rate < 3%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
203. KPI 'D7 ROAS vs plan' hedefte mi; sapma varsa kök neden ve düzeltme ne?
204. 'D7 ROAS vs plan' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
205. KPI 'Organic uplift measured' hedefte mi; sapma varsa kök neden ve düzeltme ne?
206. 'Organic uplift measured' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### RET — Perakende Medyası
207. Amazon Ads birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
208. Amazon Ads çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
209. Amazon Ads alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
210. TR Marketplaces (Trendyol/Hepsiburada) birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
211. TR Marketplaces (Trendyol/Hepsiburada) çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
212. TR Marketplaces (Trendyol/Hepsiburada) alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
213. Criteo & Onsite birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
214. Criteo & Onsite çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
215. Criteo & Onsite alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
216. Offsite & DSP birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
217. Offsite & DSP çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
218. Offsite & DSP alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
219. KPI 'ACOS/TACOS on target' hedefte mi; sapma varsa kök neden ve düzeltme ne?
220. 'ACOS/TACOS on target' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
221. KPI 'Share of voice on hero SKUs' hedefte mi; sapma varsa kök neden ve düzeltme ne?
222. 'Share of voice on hero SKUs' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
223. KPI 'PDP conversion uplift' hedefte mi; sapma varsa kök neden ve düzeltme ne?
224. 'PDP conversion uplift' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
225. KPI 'Incremental ROAS' hedefte mi; sapma varsa kök neden ve düzeltme ne?
226. 'Incremental ROAS' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### SEO — SEO & İçerik Motoru
227. Technical SEO birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
228. Technical SEO çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
229. Technical SEO alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
230. Content Production birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
231. Content Production çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
232. Content Production alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
233. Digital PR & Links birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
234. Digital PR & Links çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
235. Digital PR & Links alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
236. Repo Storefront birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
237. Repo Storefront çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
238. Repo Storefront alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
239. KPI '1+ article/day shipped' hedefte mi; sapma varsa kök neden ve düzeltme ne?
240. '1+ article/day shipped' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
241. KPI 'Organic clicks trend up' hedefte mi; sapma varsa kök neden ve düzeltme ne?
242. 'Organic clicks trend up' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
243. KPI 'Core Web Vitals green' hedefte mi; sapma varsa kök neden ve düzeltme ne?
244. 'Core Web Vitals green' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
245. KPI 'Directory listings ≥ 3' hedefte mi; sapma varsa kök neden ve düzeltme ne?
246. 'Directory listings ≥ 3' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### CRO — CRO & Deneyim
247. Experimentation birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
248. Experimentation çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
249. Experimentation alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
250. Landing Systems birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
251. Landing Systems çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
252. Landing Systems alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
253. UX Research birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
254. UX Research çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
255. UX Research alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
256. KPI 'Test velocity ≥ 4/month' hedefte mi; sapma varsa kök neden ve düzeltme ne?
257. 'Test velocity ≥ 4/month' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
258. KPI 'Win rate documented' hedefte mi; sapma varsa kök neden ve düzeltme ne?
259. 'Win rate documented' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
260. KPI 'LP conversion uplift' hedefte mi; sapma varsa kök neden ve düzeltme ne?
261. 'LP conversion uplift' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
262. KPI 'Sample-size discipline 100%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
263. 'Sample-size discipline 100%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### ANA — Analitik & Ölçümleme
264. GA4 & Tagging birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
265. GA4 & Tagging çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
266. GA4 & Tagging alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
267. Attribution birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
268. Attribution çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
269. Attribution alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
270. MMM & Incrementality birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
271. MMM & Incrementality çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
272. MMM & Incrementality alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
273. Clean Rooms & Privacy birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
274. Clean Rooms & Privacy çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
275. Clean Rooms & Privacy alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
276. Dashboards birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
277. Dashboards çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
278. Dashboards alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
279. KPI 'Tracking coverage ≥ 95%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
280. 'Tracking coverage ≥ 95%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
281. KPI 'Attribution doc per client playbook' hedefte mi; sapma varsa kök neden ve düzeltme ne?
282. 'Attribution doc per client playbook' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
283. KPI 'Dashboard SLA met' hedefte mi; sapma varsa kök neden ve düzeltme ne?
284. 'Dashboard SLA met' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
285. KPI '0 unowned KPIs' hedefte mi; sapma varsa kök neden ve düzeltme ne?
286. '0 unowned KPIs' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### DSC — Veri Bilimi & AI
287. Forecasting & LTV birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
288. Forecasting & LTV çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
289. Forecasting & LTV alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
290. Optimization Models birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
291. Optimization Models çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
292. Optimization Models alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
293. AI Tooling & Agents birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
294. AI Tooling & Agents çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
295. AI Tooling & Agents alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
296. KPI 'Forecast MAPE ≤ 15%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
297. 'Forecast MAPE ≤ 15%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
298. KPI '1 model improvement/month' hedefte mi; sapma varsa kök neden ve düzeltme ne?
299. '1 model improvement/month' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
300. KPI 'Agent eval pass rate ≥ 95%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
301. 'Agent eval pass rate ≥ 95%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### OPS — Ad Ops & Trafficking
302. CM360 Trafficking birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
303. CM360 Trafficking çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
304. CM360 Trafficking alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
305. Tag Management birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
306. Tag Management çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
307. Tag Management alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
308. QA & Verification birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
309. QA & Verification çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
310. QA & Verification alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
311. Consent & Privacy Ops birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
312. Consent & Privacy Ops çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
313. Consent & Privacy Ops alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
314. KPI 'Launch error rate < 1%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
315. 'Launch error rate < 1%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
316. KPI 'Tag QA pass 100% pre-launch' hedefte mi; sapma varsa kök neden ve düzeltme ne?
317. 'Tag QA pass 100% pre-launch' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
318. KPI 'Discrepancy < 5%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
319. 'Discrepancy < 5%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### CRE — Kreatif Stüdyo & DCO
320. Concept & Copy birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
321. Concept & Copy çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
322. Concept & Copy alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
323. Video & Motion birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
324. Video & Motion çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
325. Video & Motion alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
326. DCO & Feeds birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
327. DCO & Feeds çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
328. DCO & Feeds alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
329. Ad Format Lab birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
330. Ad Format Lab çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
331. Ad Format Lab alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
332. KPI 'Creative turnaround SLA' hedefte mi; sapma varsa kök neden ve düzeltme ne?
333. 'Creative turnaround SLA' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
334. KPI 'Hook-rate lift per iteration' hedefte mi; sapma varsa kök neden ve düzeltme ne?
335. 'Hook-rate lift per iteration' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
336. KPI '100% assets spec-compliant' hedefte mi; sapma varsa kök neden ve düzeltme ne?
337. '100% assets spec-compliant' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### STR — Strateji & Planlama
338. Audience & Insight birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
339. Audience & Insight çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
340. Audience & Insight alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
341. Media Mix birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
342. Media Mix çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
343. Media Mix alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
344. Playbooks & POVs birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
345. Playbooks & POVs çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
346. Playbooks & POVs alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
347. KPI 'Every plan carries mix rationale' hedefte mi; sapma varsa kök neden ve düzeltme ne?
348. 'Every plan carries mix rationale' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
349. KPI 'POV per major platform change ≤ 7 days' hedefte mi; sapma varsa kök neden ve düzeltme ne?
350. 'POV per major platform change ≤ 7 days' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
351. KPI 'Benchmarks refreshed monthly' hedefte mi; sapma varsa kök neden ve düzeltme ne?
352. 'Benchmarks refreshed monthly' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### CLS — Müşteri Hizmetleri
353. Account Leadership birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
354. Account Leadership çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
355. Account Leadership alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
356. Reporting Cadence birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
357. Reporting Cadence çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
358. Reporting Cadence alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
359. Onboarding birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
360. Onboarding çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
361. Onboarding alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
362. KPI 'Report SLA 100%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
363. 'Report SLA 100%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
364. KPI 'Account health scored weekly' hedefte mi; sapma varsa kök neden ve düzeltme ne?
365. 'Account health scored weekly' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
366. KPI 'Churn risk flagged ≥ 14 days early' hedefte mi; sapma varsa kök neden ve düzeltme ne?
367. 'Churn risk flagged ≥ 14 days early' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### NBD — Yeni İş & Inbound Hunisi
368. Inbound Capture birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
369. Inbound Capture çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
370. Inbound Capture alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
371. Pitch Factory birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
372. Pitch Factory çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
373. Pitch Factory alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
374. Lead Scoring birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
375. Lead Scoring çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
376. Lead Scoring alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
377. KPI 'Inbound path live (README→contact) F2' hedefte mi; sapma varsa kök neden ve düzeltme ne?
378. 'Inbound path live (README→contact) F2' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
379. KPI 'Pitch turnaround ≤ 48h' hedefte mi; sapma varsa kök neden ve düzeltme ne?
380. 'Pitch turnaround ≤ 48h' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
381. KPI 'First qualified lead by F5' hedefte mi; sapma varsa kök neden ve düzeltme ne?
382. 'First qualified lead by F5' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### PRT — Ortaklıklar & Sponsorluklar
383. Infra Sponsors birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
384. Infra Sponsors çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
385. Infra Sponsors alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
386. Referral Programs birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
387. Referral Programs çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
388. Referral Programs alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
389. Ecosystem Relations birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
390. Ecosystem Relations çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
391. Ecosystem Relations alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
392. KPI '10 sponsor conversations by F3' hedefte mi; sapma varsa kök neden ve düzeltme ne?
393. '10 sponsor conversations by F3' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
394. KPI '2 referral agreements by F4' hedefte mi; sapma varsa kök neden ve düzeltme ne?
395. '2 referral agreements by F4' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
396. KPI '3 directory listings by F2' hedefte mi; sapma varsa kök neden ve düzeltme ne?
397. '3 directory listings by F2' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### PRD — Ürün & Premium Paket
398. Premium Components birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
399. Premium Components çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
400. Premium Components alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
401. Packaging & Licensing birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
402. Packaging & Licensing çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
403. Packaging & Licensing alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
404. Docs & DX birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
405. Docs & DX çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
406. Docs & DX alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
407. KPI 'Premium pack v1 by F4' hedefte mi; sapma varsa kök neden ve düzeltme ne?
408. 'Premium pack v1 by F4' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
409. KPI 'Docs coverage 100%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
410. 'Docs coverage 100%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
411. KPI 'Install friction ≤ 2 steps' hedefte mi; sapma varsa kök neden ve düzeltme ne?
412. 'Install friction ≤ 2 steps' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### FIN — Finans & Faturalama
413. Cost Control birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
414. Cost Control çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
415. Cost Control alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
416. Revenue Ops birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
417. Revenue Ops çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
418. Revenue Ops alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
419. KPI 'Weekly cost report shipped' hedefte mi; sapma varsa kök neden ve düzeltme ne?
420. 'Weekly cost report shipped' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
421. KPI 'Revenue entries reconciled' hedefte mi; sapma varsa kök neden ve düzeltme ne?
422. 'Revenue entries reconciled' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
423. KPI 'Variance explained 100%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
424. 'Variance explained 100%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### LEG — Hukuk & Uyum
425. Licensing birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
426. Licensing çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
427. Licensing alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
428. Privacy (KVKK/GDPR) birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
429. Privacy (KVKK/GDPR) çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
430. Privacy (KVKK/GDPR) alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
431. Ad Policy birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
432. Ad Policy çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
433. Ad Policy alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
434. KPI '0 violations' hedefte mi; sapma varsa kök neden ve düzeltme ne?
435. '0 violations' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
436. KPI '100% components screened' hedefte mi; sapma varsa kök neden ve düzeltme ne?
437. '100% components screened' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
438. KPI 'Policy answers ≤ 24h' hedefte mi; sapma varsa kök neden ve düzeltme ne?
439. 'Policy answers ≤ 24h' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### TAL — Yetenek & Ajan Kalitesi
440. Agent Lifecycle birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
441. Agent Lifecycle çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
442. Agent Lifecycle alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
443. Quality Bar birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
444. Quality Bar çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
445. Quality Bar alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
446. Training Loops birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
447. Training Loops çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
448. Training Loops alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
449. KPI 'Quality audit ≥ 95% pass' hedefte mi; sapma varsa kök neden ve düzeltme ne?
450. 'Quality audit ≥ 95% pass' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
451. KPI 'Role gaps closed ≤ 14 days' hedefte mi; sapma varsa kök neden ve düzeltme ne?
452. 'Role gaps closed ≤ 14 days' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
453. KPI 'Roster coverage 100%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
454. 'Roster coverage 100%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
### INF — Teknoloji & Altyapı
455. CI/CD & Actions birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
456. CI/CD & Actions çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
457. CI/CD & Actions alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
458. Validation & Security birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
459. Validation & Security çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
460. Validation & Security alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
461. MCP & Integrations birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
462. MCP & Integrations çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
463. MCP & Integrations alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
464. Repo Hygiene birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?
465. Repo Hygiene çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?
466. Repo Hygiene alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?
467. KPI 'CI green ≥ 99%' hedefte mi; sapma varsa kök neden ve düzeltme ne?
468. 'CI green ≥ 99%' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
469. KPI 'Integrity file current' hedefte mi; sapma varsa kök neden ve düzeltme ne?
470. 'Integrity file current' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
471. KPI '0 secret leaks' hedefte mi; sapma varsa kök neden ve düzeltme ne?
472. '0 secret leaks' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?
473. KPI 'Issue triage ≤ 24h' hedefte mi; sapma varsa kök neden ve düzeltme ne?
474. 'Issue triage ≤ 24h' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?

## C. Kademe soruları
### C-LEVEL
475. Ajans OKR attainment'ı %80 üstünde mi; değilse kurtarma planı ne?
476. Bir faz kapısını kanıtsız GEÇTİ saymadım değil mi?
477. Mikro-yönetime kaydım mı; yetkiyi doğru devrettim mi?
478. Sahibe danışmadan bir taahhüt verdim mi?
479. 5 gelir kanalının hepsinin sahibi ve durumu net mi?
480. Kurul gündemini kanıt-linkli hazırladım mı?
### EVP
481. Departman OKR skoru güncel mi; kırmızı OKR için plan var mı?
482. Kadroyu aşırı yükledim mi; kapasite dengeli mi?
483. Playbook'u merge öncesi onayladım mı?
484. Haftalık departman raporu yayınlandı mı?
485. Sponsor C-level'a haftalık raporladım mı?
### DIRECTOR
486. Birim backlog'u doğru önceliklendi mi?
487. Uzman çıktısını publish öncesi review ettim mi?
488. Birim retrosundan öğrenim damıttım mı?
489. Cross-unit çakışmayı EVP'ye taşıdım mı?
### LEAD
490. İş akışı standardı/checklist güncel mi?
491. Uzman görevlerini günlük atadım/review ettim mi?
492. Haftalık iş akışı özetini yazdım mı?
493. Riski metrik kanıtıyla mı bayrakladım?
### SPECIALIST
494. Çıktım kopyala-hazır ve checklist'li mi?
495. Bu hafta playbook'a 1 iyileştirme önerdim mi?
496. İşi metrik gerekçesi olmadan mı sundum?
497. Damgasız çıktı bıraktım mı?
### ANALYST
498. Veri kesitim tanım-ekli mi?
499. Anomaliyi büyüklük+hipotezle mi işaretledim?
500. Tahmini açıkça etiketledim mi?
501. Veri uydurmadım değil mi?
