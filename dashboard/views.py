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

