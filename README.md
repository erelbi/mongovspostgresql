# mongovspostgresql
Postgresql mi MongoDB mi?
> Her ne kadar birlikte kullanımı yaygın olarak görülsede merak ettiğim bir soru var...
> Basit bir Projede sadece mongoDB kullansam Postgresql den ne kadar hızlı olurum.
> Bunun için kayıt ve silme işlemleri ile birlikte test ettik
> Kayıt işlemlerinde %20 MongoDB daha hızlı iken Silme İşlemlerinde Hız %80 ü buluyor.

## Ortam 
İki DB de docker üzerinde ayağa kaldırıldı
Çatı Django
djongo==1.3.6
psycopg2==2.9.1
Bağlantı kütüphanleri Kullanıldı.
