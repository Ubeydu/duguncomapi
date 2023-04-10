from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'url', 'isim', 'durum', 'olusturulma_tarihi', 'guncelleme_tarihi', 'fiyat')