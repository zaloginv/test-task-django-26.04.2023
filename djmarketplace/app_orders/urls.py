from django.urls import path
from .views import order_create

app_name = 'app_orders'

urlpatterns = [
    path('order/<int:shop_id>', order_create, name='order_create')
]