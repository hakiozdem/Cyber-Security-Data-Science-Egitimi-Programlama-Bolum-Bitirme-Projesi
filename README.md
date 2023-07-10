# Cyber-Security-Data-Science-Egitimi-Programlama-Bolum-Bitirme-Projesi

## Ön bilgilendirme
CSDS Eğitimi Programlama Bölümü Bitirme Projesinin daha detaylı, eğitime yakışır bir şekilde olmasını istedim. Bu sebeple güvenlik tarafında daha fazla ne kadar önlem alabilirim diye araştırdım ve belirli çözümler buldum:
1. FlaskForms Kullanmak: WTForms ve Flask uyumluluğu ile güvenli formlar oluşturabiliyoruz. Formlar sadece bizim istediğimiz şekillerde ve daha etkin kullanılabiliyor. Ayrıca aynı kütüphanenin CSRF için de bir çözümü var, onu da kullandım.
2. Flask-Login Kütüphanesi: Bu kütüphane ile yetkisiz erişimi ve kullanıcı yetkilendirmesini sağladım. Çok basit bir kullanımı var.
3. Werkzeug.security ile parola hashleri üretmek: Veritabanı üzerinde parolayı sha-256 kullanarak hashleyerek saklama. Bu hem veri tabanına erişen kişinin parolayı bulamamasını, hem de SQL Enjeksiyonu ile yetkisiz kullanıcı girişini önlemek amaçlı yapıldı.
Bunlar haricinde bizden istenen Jinja Template kullanımı, PostgreSQL-Flask-SQLAlchemy kullanımı gibi detaylar mevcuttur. Bunun haricinde Flask-Session kullanmak yerine, daha basit ancak daha az secure olan Flask'ın kendi session özelliğini kullandım. Bunu daha çok kullanıcı id'si kullanılan işlerde session boyunca kullanılabilir olması için kullandım.

## Veritabanı kurulumu ve tam çalıştırma
Öncelikle Flask-SQLAlchemy, Flask-Migrate ve psycopg2 indirilmeli. Daha sonra PGadmin üzerinden veritabanı kurulmalı ve kullanıcı bilgileri app.py üzerinde gerekli yerlere girilmeli.
En son olarak terminal üzerinde sırasıyla:
 - flask db init
 - flask db migrate
 - flask db upgrade
çalıştırılmalı.

## Website Haritası
Web site haritasını şu şekilde gösterebilirim:
- Index
- Kayıt ol
- Giriş Yap
 * User Index
 * Projeleri Göster
  - Projedeki işleri göster
  - Projedeki tek bir işi göster
  - Projedeki işi sil
  - Projedeki işi düzenle
  - Projeye yeni iş ekle
 * Add new Project
 * Kullanıcı bilgilerini düzenle
  - Parolayı düzenle


