from django.db import models
from djmoney.models.fields import MoneyField

AVAILABLE_STATUS = (
    ("Aktif","Aktif"),
    ("Pasif", "Pasif"),
    ("Bilinmiyor","Bilinmiyor"),
)


class Product(models.Model):
    isim = models.CharField(max_length=200)
    #fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    durum = models.CharField(max_length=10, choices= AVAILABLE_STATUS, default='Aktif')
    olusturulma_tarihi = models.DateTimeField(auto_now=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    fiyat = MoneyField(max_digits=10, decimal_places=2, default_currency='TRY')

    def __str__(self):
        return self.isim


        
    
    

