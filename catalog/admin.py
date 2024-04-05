from django.contrib import admin
from .models import Category, Product, Basket, BasketItem, Review, ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'message', 'created_at')  # fields to display in the list view

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'description', 'price', 'description2', 'image2', 'image3', 'image4']

admin.site.register(ContactMessage, ContactMessageAdmin)  # register ContactMessageAdmin with ContactMessage
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)  # register ProductAdmin with Product
admin.site.site_header = 'Cosmic Commerce Admin Portal'
admin.site.site_title = 'Admin Operations'