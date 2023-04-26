from django.db import models
from app_shop.models import ProductShop, Shop
from app_users.models import Profile


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='customer_order')
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop_order')

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductShop, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity
