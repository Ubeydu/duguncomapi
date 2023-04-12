from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-olusturulma_tarihi')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['isim', 'durum', 'olusturulma_tarihi', 'guncelleme_tarihi', 'fiyat']
