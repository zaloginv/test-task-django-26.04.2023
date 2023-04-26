from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from app_cart.cart import Cart
from app_users.models import Profile


@transaction.atomic
def order_create(request, shop_id):
    cart = Cart(request, shop_id)

    if request.method == 'POST':
        user_profile = Profile.objects.get(user=request.user)
        balance = user_profile.balance
        total_sum = cart.get_total_price()
        result = balance - total_sum
        if result < 0:
            messages.warning(request, "You doesn't have enough money. Replenish your balance")
            return redirect('app-users:profile')

        user_profile.balance -= total_sum
        user_profile.purchases_sum += total_sum

        if user_profile.purchases_sum >= Profile.gold:
            user_profile.status = Profile.STATUS_CHOICES[2][0]
        elif user_profile.purchases_sum >= Profile.silver:
            user_profile.status = Profile.STATUS_CHOICES[1][0]

        user_profile.save()

        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

                print(item['product'])
                product_in_shop = item['product']
                product_in_shop.quantity -= item['quantity']
                product_in_shop.save()

            cart.clear()
            return render(request, 'app_orders/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'customer': request.user.id,
            'shop': shop_id
        })
    return render(request, 'app_orders/create.html',
                  {'cart': cart, 'form': form})