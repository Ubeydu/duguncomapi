from django.db import models

class Product(models.Model):
    isim = models.CharField(max_length=200)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    durum = models.CharField(max_length=10, options=AVAILABLE_STATUS, default='active')
    olusturulma_tarihi = models.DateTimeField()
    guncelleme_tarihi = models.DateTimeField()
    


AVAILABLE_STATUS = (
    ('active','AKTIF'),
    ('passive', 'PASIF'),
    ('other','BILINMIYOR')
)

