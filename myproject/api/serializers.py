from rest_framework import serializers
from .models import Category, Store, Product, ProductImages

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name','logo_img',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('image',)

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    store_name = serializers.CharField(source="store.name")
    store_image = serializers.CharField(source="store.logo_img")
    images = ProductImagesSerializer(source='productimages_set', many=True, read_only=True)
    src = serializers.SerializerMethodField()

    def get_src(self, obj):
        first_image = obj.productimages_set.first()
        if first_image:
            return first_image.image
        return None

    class Meta:
        model = Product
        fields = '__all__'
