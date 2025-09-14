from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Review
from dealerships.models import Dealership
import json

def get_dealer_reviews(request, dealer_id):
    """Get all reviews for a specific dealer"""
    try:
        dealer = Dealership.objects.get(dealerId=dealer_id)
        reviews = Review.objects.filter(dealership=dealer)
        
        reviews_data = []
        for review in reviews:
            reviews_data.append({
                'id': review.id,
                'name': review.name,
                'dealership': dealer.name,
                'review': review.review,
                'purchase': review.purchase,
                'purchase_date': str(review.purchase_date) if review.purchase_date else None,
                'car_make': review.car_make,
                'car_model': review.car_model,
                'car_year': review.car_year,
                'sentiment': review.sentiment
            })
        
        return JsonResponse({'reviews': reviews_data})
    except Dealership.DoesNotExist:
        return JsonResponse({'error': 'Dealer not found'}, status=404)

@csrf_exempt
@login_required
def add_review(request):
    """Add a new review"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            dealer = Dealership.objects.get(dealerId=data['dealer_id'])
            
            review = Review.objects.create(
                name=data['name'],
                dealership=dealer,
                review=data['review'],
                purchase=data.get('purchase', False),
                purchase_date=data.get('purchase_date'),
                car_make=data.get('car_make'),
                car_model=data.get('car_model'),
                car_year=data.get('car_year'),
                sentiment=data.get('sentiment', 'neutral')
            )
            
            return JsonResponse({
                'status': 'success',
                'review_id': review.id,
                'message': 'Review added successfully'
            })
        except Dealership.DoesNotExist:
            return JsonResponse({'error': 'Dealer not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
