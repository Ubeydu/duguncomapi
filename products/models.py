from django.db import models
from djmoney.models.fields import MoneyField
#from django.core.validators import MinValueValidator
#from decimal import *
#from djmoney.money import Money
#from djmoney.models.validators import MinMoneyValidator

AVAILABLE_STATUS = (
    ("Aktif","Aktif"),
    ("Pasif", "Pasif"),
    ("Bilinmiyor","Bilinmiyor"),
)


class Product(models.Model):
    isim = models.CharField(max_length=200)
    durum = models.CharField(max_length=10, choices= AVAILABLE_STATUS, default='Aktif')
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    fiyat = MoneyField(max_digits=10, decimal_places=2, default_currency='TRY')
    

    def __str__(self):
        return self.isim


        
    
    

