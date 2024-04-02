from django.shortcuts import render
from .models import UserInfo
from django.core.exceptions import ObjectDoesNotExist

def dashboard(request):
    try:
        user_info = UserInfo.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_info = None
    return render(request, 'dashboard/dashboard.html', {'user_info': user_info})