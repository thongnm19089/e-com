from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductList,DetailProduct

router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>',DetailProduct.as_view(), name='product-detail'),
   
]
