from django import forms
from django.contrib import admin
from .models import User, Product, Order, Item, Basket, BasketItem, Category, Review, ContactMessage, CompletedOrder

class ProductAdminForm(forms.ModelForm):
    description2 = forms.CharField(widget=forms.TextInput)

class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ['title', 'category', 'image', 'description', 'price', 'short_description2', 'image2', 'image3', 'image4']

    def short_description2(self, obj):
        return obj.description2[:50]  # Truncate to 50 characters
    short_description2.short_description = 'Description 2'  

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'updated_at', 'display_order_items')

    def display_order_items(self, obj):
        return ", ".join([item.name for item in obj.order_items.all()])
    display_order_items.short_description = 'Order Items'

admin.site.register(Product, ProductAdmin) 
admin.site.register(Order, OrderAdmin) 
admin.site.site_header = 'Cosmic Commerce Admin Portal'
admin.site.site_title = 'Admin Operations'
admin.site.register(Item)
admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(ContactMessage)
admin.site.register(CompletedOrder)