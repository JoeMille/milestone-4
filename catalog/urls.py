from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views

# URL patterns for the catalog app
urlpatterns = [

    path('', views.index, name='index'), 
    path('register/', views.register, name='register'), 
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout, name = 'logout'),
    path('products/', views.products, name='products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('basket/', views.basket, name='basket'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('charge/', views.charge, name='charge'),
    path('reviews/', views.reviews, name='reviews'),
    path('create_review/', views.create_review, name='create_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('add_to_basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove_from_basket/<int:item_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('payment_complete/', views.payment_complete, name='payment_complete'),
]