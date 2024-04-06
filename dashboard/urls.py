from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('charge/<int:order_id>/', views.charge, name='charge'),
]