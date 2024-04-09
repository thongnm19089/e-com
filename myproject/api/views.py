from rest_framework import viewsets
from .models import Category, Store, Product, ProductImages
from .serializers import CategorySerializer, StoreSerializer, ProductSerializer, ProductImagesSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class DetailProduct(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)

        products = Product.objects.exclude(pk=pk)
        related_products = products.filter(category=product.category)
        data = serializer.data

        for store in Store.objects.filter():
            shop = related_products.filter(store=store)
            data[store.name] = ProductSerializer(shop, many=True).data
        
        data['related_products'] = ProductSerializer(related_products, many=True).data

        return Response(data)