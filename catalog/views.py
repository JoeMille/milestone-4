# views.py
import stripe
from django import forms
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product, Basket, BasketItem, Review 
from django.contrib.auth import logout as auth_logout
from django.db.models import Prefetch
from django.core.mail import send_mail
from .forms import ContactForm
from .models import ContactMessage, Order, CompletedOrder
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# Index page view
def index(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        contact_form = ContactForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        elif contact_form.is_valid():
            message = contact_form.cleaned_data['message']
            ContactMessage.objects.create(message=message)  
            return redirect('index')
    else:
        form = AuthenticationForm()

    # Fetch the basket for the current user
    basket = None
    if request.user.is_authenticated:
        basket, created = Basket.objects.get_or_create(user=request.user)
    
    # Fetch featured products 
    featured_products = Product.objects.filter(featured=True)[:4]

    # Fetch legendary products
    legendary_products = Product.objects.filter(category__name='Legendary')

    return render(request, 'catalog/index.html', {'form': form, 'basket': basket, 'featured_products': featured_products, 'legendary_products': legendary_products, 'contact_form': contact_form})


# Add products to user basket
@login_required
def add_to_basket(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    basket, created = Basket.objects.get_or_create(user=request.user)
    basket_item, created = BasketItem.objects.get_or_create(product=product, basket=basket)
    if not created:
        basket_item.quantity += 1
        basket_item.save()

    # Update the 'basket' session variable
    request.session['basket'] = list(basket.basketitem_set.values())

    return redirect('products')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'catalog/register.html', {'form': form})

# Custom Login View
class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

# Logout view

def logout(request):
    auth_logout(request)
    return redirect('index')

# Products page view
def products(request):
    categories = Category.objects.prefetch_related(
        Prefetch('product_set', queryset=Product.objects.all(), to_attr='products')
    )
    return render(request, 'catalog/products.html', {'categories': categories})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})


def checkout(request):
    if request.user.is_authenticated:
        basket, created = Basket.objects.get_or_create(user=request.user)
        if request.method == 'POST':
            form = CheckoutForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                messages.success(request, 'Order placed successfully.')
                return redirect('order_success')
        else:
            form = CheckoutForm()
        return render(request, 'catalog/checkout.html', {'basket': basket, 'form': form})
    else:
        return redirect('login')

class CheckoutForm(forms.Form):
    house = forms.CharField(max_length=255)
    street = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    county = forms.CharField(max_length=255)
    eircode = forms.CharField(max_length=255)

def basket(request):
    basket = request.session.get('basket', {})
    products = Product.objects.filter(id__in=basket.keys())
    total = sum([product.price for product in products])
    return render(request, 'basket.html', {'products': products, 'total': total})

# Add items to checkout basket
def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket = request.session.get('basket', {})
    basket[product_id] = basket.get(product_id, 0) + 1
    request.session['basket'] = basket
    return redirect('basket')

# Remove items from checkout basket 
def remove_from_basket(request, item_id):
    if request.method == 'POST':
        item = BasketItem.objects.get(id=item_id)
        item.delete()
    return redirect('checkout')

def payment(request):
    if request.method == 'POST':
        # Get the order details from the form
        house = request.POST.get('house')
        street = request.POST.get('street')
        city = request.POST.get('city')
        county = request.POST.get('county')
        eircode = request.POST.get('eircode')

        # Get the basket for the current user
        basket = Basket.objects.get(user=request.user)

        # Create a string representation of the order items
        order_items = ', '.join([f'{item.product.title} (Quantity: {item.quantity})' for item in basket.basketitem_set.all()])

        # Create a new completed order
        order = CompletedOrder(
            user=request.user,
            order_items=order_items,
            address=f'{house}, {street}, {city}, {county}, {eircode}',
            payment_type='Card'
        )
        order.save()

        messages.success(request, 'Your order has been placed successfully!')

    # Your payment processing code here
    return render(request, 'catalog/payment.html')

# Payment page view
@csrf_exempt
def charge(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST['stripeToken']

        # Create Order object
        try:
            order = Order.objects.create(
                user=request.user,
                # Add other necessary fields here
            )
        except Exception as e:
            return HttpResponse(f'Error: {str(e)}', status=400)

        # Create Stripe charge
        try:
            charge =  stripe.Charge.create(
                amount=1000,
                currency='usd',
                description='Example charge',
                source=token,
            )
        except InvalidRequestError as e:
            return HttpResponse(f'Error: {str(e)}', status=400)

        # Redirect to a "payment complete" page after a successful charge
        return redirect('payment_complete')

    return render(request, 'catalog/charge.html')
# Reviews page view

def reviews(request):
    reviews = Review.objects.all()  
    products = Product.objects.all() 
    print(reviews) # Print all reviews to the terminal test REMOVE THIS LINE 
    return render(request, 'catalog/reviews.html', {'reviews': reviews, 'products': products})

def create_review(request):
    products = Product.objects.all()  
    print(products) # Print all products to the terminal test REMOVE THIS LINE
    if request.method == 'POST':
        review = Review()
        review.user = request.user
        review.product = Product.objects.get(pk=request.POST['product_id'])
        review.rating = request.POST['rating']
        review.comment = request.POST['comment']
        review.save()
        return redirect('reviews')
    return render(request, 'catalog/create_review.html', {'products': products})

def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        if request.user == review.user:
            review.rating = request.POST['rating']
            review.comment = request.POST['comment']
            review.save()
        return redirect('reviews')
    else:
        if request.user != review.user:
            return redirect('reviews')
        return render(request, 'catalog/edit_review.html', {'review': review})

def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user == review.user:
        review.delete()
    return redirect('reviews')

def payment_complete(request):
    return render(request, 'catalog/payment_complete.html')
