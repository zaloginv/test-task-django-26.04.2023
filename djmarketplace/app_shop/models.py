from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=1000)
    shops = models.ManyToManyField('Shop', through='ProductShop')

class Shop(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=32)

class ProductShop(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)


