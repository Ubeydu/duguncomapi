from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
#from django_filters.rest_framework import DjangoFilterBackend
from urllib.parse import unquote
from products.models import ProductFilters

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-olusturulma_tarihi')
    serializer_class = ProductSerializer
    rql_filter_class = ProductFilters
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['isim', 'durum', 'olusturulma_tarihi', 'guncelleme_tarihi', 'fiyat']

def search_products_by_name(request):
    query = unquote(request.meta['QUERY_STRING'])
    base_queryset = Product.objects.all()
    my_filter = ProductFilters(base_queryset)
    _, filtered_qs = my_filter.apply_filters(query)
    return render(request, 'products/search.html', {'products': filtered_qs})