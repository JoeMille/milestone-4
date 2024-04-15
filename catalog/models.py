from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Category model, allowing for the creation of categories for products
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Product model, allowing for the creation of products with a description, price, and category
class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=200, default='Default Title')
    description = models.TextField()
    description2 = models.TextField(default='Default Description')
    image2 = models.ImageField(upload_to='products/', default='products/default.jpg')
    image3 = models.ImageField(upload_to='products/', default='products/default.jpg')
    image4 = models.ImageField(upload_to='products/', default='products/default.jpg')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Basket model
class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='BasketItem')

    def total_cost(self):
        return sum(item.total_price() for item in self.basketitem_set.all())
    def get_total_price(self):
        return sum(item.product.price * item.quantity for item in self.basketitem_set.all())

# Basket model, allowing for the creation of a basket for a user
class BasketItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

RATING_CHOICES = [(i, i) for i in range(1, 11)]

# Review model, allowing for the creation of reviews for products
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(default='')

    def __str__(self):
        return f'Review for {self.product.title} by {self.user.username}'

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.name}'

# Order model, allowing for the creation of orders with a user, status, created_at, and updated_at field

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    PAYMENT_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        # Add more payment types as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='catalog_orders')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    address = models.CharField(max_length=255, null=True)  
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES, null=True)
    order_items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id}'

# Defining the completed order model

class CompletedOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='completed_orders')
    order_items = models.TextField()
    address = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Completed Order {self.id} for {self.user.username}'