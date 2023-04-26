from django.urls import path
from .views import MainView, ShopListView, ShopDetailView

app_name = 'app-shop'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('shop_list/', ShopListView.as_view(), name='shop-list'),
    path('shop/<int:pk>', ShopDetailView.as_view(), name='shop-detail')
]