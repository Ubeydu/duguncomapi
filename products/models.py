from django.db import models

AVAILABLE_STATUS = (
    ("Aktif","Aktif"),
    ("Pasif", "Pasif"),
    ("Bilinmiyor","Bilinmiyor"),
)


class Product(models.Model):
    isim = models.CharField(max_length=200)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    durum = models.CharField(max_length=10, choices= AVAILABLE_STATUS, default='Aktif')
    olusturulma_tarihi = models.DateTimeField(auto_now=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    
    

