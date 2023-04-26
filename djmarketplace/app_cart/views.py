from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from app_shop.models import ProductShop
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, shop_id, product_id):
    cart = Cart(request, shop_id)
    product = get_object_or_404(ProductShop, shop_id=shop_id, product_id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if cd['quantity'] > product.quantity:
            messages.warning(request, "Not enough products in shop's stock")
            return redirect('app_cart:cart_detail', shop_id)
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    return redirect('app_cart:cart_detail', shop_id)

def cart_remove(request, shop_id, product_id):
    cart = Cart(request, shop_id)
    product = get_object_or_404(ProductShop, id=product_id)
    cart.remove(product)
    return redirect('app_cart:cart_detail', shop_id)

def cart_detail(request, shop_id):
    cart = Cart(request, shop_id)
    return render(request, 'app_cart/detail.html', {'cart': cart})