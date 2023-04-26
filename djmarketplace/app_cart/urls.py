
from django.urls import path

from .views import cart_remove, cart_add, cart_detail

app_name = 'app_cart'

urlpatterns = [
    path('<int:shop_id>', cart_detail, name='cart_detail'),
    path('<int:shop_id>/<int:product_id>', cart_add, name='cart_add'),
    path('remove/<int:shop_id>/<int:product_id>', cart_remove, name='cart_remove'),
]