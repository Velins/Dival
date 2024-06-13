import base64
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.db import transaction
from django.forms import ValidationError
from django.contrib import messages

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from carts.models import Cart

from liqpay3.liqpay import LiqPay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            phone=form.cleaned_data['phone'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостатня к-сть товару {name} на складі\
                                                       В наявності - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        cart_items.delete()

                        if order.payment_on_get == '0':
                            return redirect('orders:liqpay_checkout', order_id=order.id)
                        else:
                            messages.success(request, 'Замовлення сформовано!')
                            return redirect('users:profile')

            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('users:user_cart')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Формування замовлення',
        'form': form,
        'orders': True,
    }
    return render(request, 'orders/create_order.html', context=context)

@login_required
def liqpay_checkout(request, order_id):

    order_items = OrderItem.objects.filter(order=order_id)
    total_price = sum(item.price * item.quantity for item in order_items)  # Підрахунок загальної суми замовлення

    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)

    params = {
        'action': 'pay',
        'amount': str(total_price),
        'currency': 'UAH',
        'description': f'Order #{order_id}',
        'order_id': str(order_id),
        'version': '3',
        'sandbox': 1,  # Увімкнути тестовий режим
        'server_url': request.build_absolute_uri('/liqpay-callback/'),
        'result_url': request.build_absolute_uri('/user/orders/'),
    }

    form_html = liqpay.cnb_form(params)  # Генерація HTML-форми для оплати

    context = {
        'title': 'Оплата',
        'form_html': form_html
    }
    return render(request, 'orders/checkout.html', context)

@csrf_exempt
def liqpay_callback(request):
    data = request.POST.get('data')
    signature = request.POST.get('signature')

    print(f"Received data: {data}")
    print(f"Received signature: {signature}")

    if not data or not signature:
        return HttpResponse('Missing data or signature', status=400)

    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    is_valid = liqpay.verify_signature(signature, data)

    if is_valid:
        response_data = json.loads(liqpay.decode_data_from_str(data))
        if response_data['status'] == 'success':
            order_id = response_data['order_id']
            order = Order.objects.get(id=order_id)
            order.is_paid = True
            order.save()
            return HttpResponse('Payment successful', status=200)
        
    return HttpResponse('Payment verification failed', status=400)

