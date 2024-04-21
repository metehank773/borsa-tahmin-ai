# borsa-tahmin-ai
makine öğrenimi ile borsa fiyat tahmini
 Kod, hisse senedi verilerini almak, verileri analiz etmek, bir lineer regresyon modeli oluşturmak, tahminler yapmak ve modelin performansını değerlendirmek için kullanılır.

Adımlar:
Kodun İndirilmesi ve Çalıştırılması:
Bu GitHub deposunu klonlayarak veya ZIP olarak indirerek bilgisayarınıza kaydedin.
Bilgisayarınızda Python yüklü olduğundan emin olun.
Gerekli kütüphaneleri kurmak için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:
bash
Copy code
pip install pandas numpy matplotlib scikit-learn yfinance
Python Dosyasını Çalıştırma:
Terminal veya komut istemcisinde, kaydettiğiniz klasöre gidin.
Python dosyasını çalıştırmak için aşağıdaki komutu kullanın:
bash
Copy code
python stock_prediction.py
Kullanıcıdan Bilgi Alınması:
Program çalıştırıldığında, bir hisse senedi sembolü girmeniz istenecektir (örneğin, GARAN.IS).
İşlem yapmak istediğiniz hisse senedinin sembolünü girin ve Enter tuşuna basın.
Sonuçları İnceleme:
Program, girilen sembolle ilgili hisse senedi fiyatlarını alacak ve bir grafikte gösterecektir.
Ardından, lineer regresyon modeli oluşturulacak ve gerçek fiyatlarla tahmin edilen fiyatlar bir grafikte karşılaştırılacaktır.
Son olarak, modelin performansı ölçülecek ve MSE (Ortalama Kare Hatası) ve R² (R-kare) değerleri ekrana yazdırılacaktır.
Notlar:
Program, Yahoo Finance API'sini kullanarak hisse senedi verilerini alır. Bu nedenle, internet bağlantınızın olması gerekmektedir.
Eğer hisse sembolü yanlış veya mevcut olmayan bir sembolse, hata mesajı alacaksınız.
