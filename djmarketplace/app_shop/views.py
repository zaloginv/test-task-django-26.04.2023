from django.views.generic import TemplateView, ListView, DetailView
from .models import Shop, ProductShop
from app_cart.forms import CartAddProductForm
from app_orders.models import OrderItem

class MainView(TemplateView):
    template_name = 'app_shop/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_sum_dict = {}
        last_twenty = OrderItem.objects.all()[:20]
        for object in last_twenty:
            if object.product_id in total_sum_dict:
                total_sum_dict[object.product_id] += object.get_cost()
            else:
                total_sum_dict[object.product_id] = object.get_cost()
        best_product_data = sorted(total_sum_dict.items(), reverse=True, key=lambda item: item[1])[0]
        best_product = ProductShop.objects.get(id=best_product_data[0]).product.name
        context['best_product'] = best_product
        return context

class ShopListView(ListView):
    model = Shop
    context_object_name = 'shop_list'
    template_name = 'app_shop/shop_list.html'


class ShopDetailView(DetailView):
    model = Shop
    context_object_name = 'shop_detail'
    template_name = 'app_shop/shop_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ph_list'] = ProductShop.objects.filter(shop=self.get_object()).all()
        context['cart_product_form'] = CartAddProductForm()
        return context