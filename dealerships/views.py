from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from .models import Dealership
import requests
import json

def home(request):
    """Home page view"""
    state_filter = request.GET.get('state')
    
    if state_filter:
        dealers = Dealership.objects.filter(state__iexact=state_filter)
    else:
        dealers = Dealership.objects.all()
    
    dealers_list = []
    for dealer in dealers:
        dealers_list.append({
            'id': dealer.dealerId,
            'name': dealer.name,
            'city': dealer.city,
            'state': dealer.state,
            'zip': dealer.zip_code,
            'address': dealer.address,
        })
    
    context = {
        'dealers': dealers_list,
        'state_filter': state_filter,
        'user': request.user if request.user.is_authenticated else None
    }
    return render(request, 'dealerships/home.html', context)

def about_us(request):
    """About Us page view"""
    return render(request, 'dealerships/about.html')

def contact_us(request):
    """Contact Us page view"""
    return render(request, 'dealerships/contact.html')

def login_user(request):
    """User login view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'dealerships/login.html', {'error': 'Invalid credentials'})
    return render(request, 'dealerships/login.html')

def logout_user(request):
    """User logout view"""
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    # Show logout confirmation page for GET request
    return render(request, 'dealerships/logout_confirm.html')

def signup_user(request):
    """User signup view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'dealerships/signup.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        login(request, user)
        return redirect('home')
    return render(request, 'dealerships/signup.html')

def get_dealers(request, state=None):
    """Get dealers - from external API or database"""
    if state:
        # Filter by state
        dealers = Dealership.objects.filter(state__iexact=state)
    else:
        dealers = Dealership.objects.all()
    
    dealers_list = []
    for dealer in dealers:
        dealers_list.append({
            'id': dealer.dealerId,
            'name': dealer.name,
            'city': dealer.city,
            'state': dealer.state,
            'zip': dealer.zip_code,
            'address': dealer.address,
            'lat': float(dealer.lat) if dealer.lat else None,
            'long': float(dealer.long) if dealer.long else None,
            'short_name': dealer.short_name,
            'st': dealer.st
        })
    
    context = {
        'dealers': dealers_list,
        'state_filter': state,
        'user': request.user if request.user.is_authenticated else None
    }
    return render(request, 'dealerships/dealers.html', context)

def get_dealers_by_state(request, state):
    """Get dealers filtered by state"""
    return get_dealers(request, state)

def dealer_details(request, dealer_id):
    """Get specific dealer details with reviews"""
    try:
        dealer = Dealership.objects.get(dealerId=dealer_id)
        # Get reviews for this dealer
        from reviews.models import Review
        reviews = Review.objects.filter(dealership=dealer)
        
        reviews_list = []
        for review in reviews:
            reviews_list.append({
                'id': review.id,
                'name': review.name,
                'review': review.review,
                'purchase': review.purchase,
                'purchase_date': review.purchase_date,
                'car_make': review.car_make,
                'car_model': review.car_model,
                'car_year': review.car_year,
                'sentiment': review.sentiment
            })
        
        context = {
            'dealer': {
                'id': dealer.dealerId,
                'name': dealer.name,
                'city': dealer.city,
                'state': dealer.state,
                'zip': dealer.zip_code,
                'address': dealer.address
            },
            'reviews': reviews_list,
            'user': request.user if request.user.is_authenticated else None
        }
        return render(request, 'dealerships/dealer_detail.html', context)
    except Dealership.DoesNotExist:
        return render(request, 'dealerships/error.html', {'message': 'Dealer not found'})

@login_required
def add_review(request, dealer_id):
    """Add review for a dealer"""
    if request.method == 'POST':
        try:
            dealer = Dealership.objects.get(dealerId=dealer_id)
            from reviews.models import Review
            
            review = Review.objects.create(
                name=request.POST.get('name'),
                dealership=dealer,
                review=request.POST.get('review'),
                purchase=request.POST.get('purchase') == 'on',
                purchase_date=request.POST.get('purchase_date') if request.POST.get('purchase_date') else None,
                car_make=request.POST.get('car_make'),
                car_model=request.POST.get('car_model'),
                car_year=int(request.POST.get('car_year')) if request.POST.get('car_year') else None,
                sentiment='positive'  # Will be analyzed later
            )
            return redirect('dealer_details', dealer_id=dealer_id)
        except Dealership.DoesNotExist:
            return render(request, 'dealerships/error.html', {'message': 'Dealer not found'})
    else:
        try:
            dealer = Dealership.objects.get(dealerId=dealer_id)
            context = {
                'dealer': dealer,
                'user': request.user
            }
            return render(request, 'dealerships/add_review.html', context)
        except Dealership.DoesNotExist:
            return render(request, 'dealerships/error.html', {'message': 'Dealer not found'})
