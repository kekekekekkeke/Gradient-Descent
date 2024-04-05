# Gradient-Descent
# Giriş:
Kod, gradient descenti lineer regresyon bağlamında göstermeyi amaçlamaktadır, özellikle de yıl, kilometre, motor boyutu ve marka gibi çeşitli özelliklere dayanarak araba fiyatlarını tahmin etmek için. Kategorik özelliği (marka) işlemek için one-hot-encoding eklenmiş ve doğrusal regresyon modelinin parametrelerini optimize etmek için gradient descent kullanılmıştır.

# Metodlar:
# Veri Hazırlığı:
Sağlanan veri, araba listeleri hakkında bilgiler içeren bir sözlük olarak yapılandırılmıştır, bu bilgiler arasında sayısal özellikler (yıl, kilometre, motor boyutu) ve kategorik bir özellik bulunmaktadır.Aynı zamanda oldukça ufak bir veridir.
# Feature Scaling:
Sayısal özellikler, gradient descentin optimize edilmesini kolaylaştırmak için ortalama değeri 0 ve standart sapması 1 olacak şekilde standartlaştırılmıştır. Kategorik özellik, regresyon modeli için uygun bir sayısal formata dönüştürmek için one-hot-encoding kullanılarak nümerik arraye dönüştürülmüştür.
# Model Eğitimi:
Lineer regresyon modelinin parametrelerini optimize etmek için gradient descent uygulanmıştır. Kullanılan cost fonksiyonu ortalama kare hatasıdır ve bu fonksiyonun parametrelerle olan gradyanı, onları iteratif olarak güncellemek için hesaplanmıştır.
# Model Değerlendirmesi:
Eğitilmiş model, farklı alfa değerleri (learning rate) için cost fonksiyonunu iterasyon sayısına karşı çizerek gradient descentin yakınsamasını gösterir. Ayrıca, tahmin edilen fiyatlar, her alfa değeri için yazdırılır ve modelin doğruluğu, tahmin edilen ve gerçek fiyatlar arasındaki karşılaştırmaya dayalı olarak ölçülür.
# Sonuçlar:
Algoritma işini gayet iyi bir şekilde başardı ve verinin ufaklığı sayesinde neredeyse %100 doğruluk oranına ulaşmayı başarmıştır.Cost grafiğinde de seçilen alfa değerleri için eğrinin nasıl değiştiği gayet bariz bir şekilde ortaya çıkmıştır.İterasyon sayısı daha da arttırıldıkça compiler daha küçük float sayı gösteremeyeceği için %100 doğruluğa ulaşmak mümkün olabilir.
