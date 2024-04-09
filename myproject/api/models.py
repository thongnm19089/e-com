from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Store(models.Model):
    name = models.CharField(max_length=100)
    logo_img = models.TextField()

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    price_befor = models.IntegerField()
    price_after = models.IntegerField(null=True,  blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    sales = models.IntegerField(null=True,  blank=True)
    vote = models.IntegerField(null=True,  blank=True)
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.TextField()