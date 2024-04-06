from django.shortcuts import render, get_object_or_404
from .models import UserInfo, Order
from django.core.exceptions import ObjectDoesNotExist
import stripe

def dashboard(request):
    try:
        user_info = UserInfo.objects.get(user=request.user)
        completed_orders = Order.objects.filter(user=request.user, status='completed')
    except ObjectDoesNotExist:
        user_info = None
        completed_orders = None
    return render(request, 'dashboard/dashboard.html', {'user_info': user_info, 'completed_orders': completed_orders})

def charge(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    stripe.api_key = 'your-stripe-secret-key'

    charge = stripe.Charge.create(
        amount=order.total_amount_cents,
        currency='usd',
        description=f'Order {order.id}',
        source=request.POST['stripeToken']
    )

    if charge.paid:
        order.status = 'completed'
        order.save()

    return render(request, 'charge.html', {'order': order})