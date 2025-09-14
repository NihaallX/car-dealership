from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import requests
import json

SENTIMENT_API_URL = 'http://localhost:5000'

@csrf_exempt
@require_http_methods(["POST"])
def analyze_sentiment(request):
    """Proxy endpoint to sentiment analyzer service"""
    try:
        data = json.loads(request.body)
        text = data.get('text', '')
        
        if not text:
            return JsonResponse({'error': 'Text is required'}, status=400)
        
        # Call sentiment analyzer service
        response = requests.post(f'{SENTIMENT_API_URL}/analyze', 
                               json={'text': text},
                               timeout=10)
        
        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({'error': 'Sentiment analysis failed'}, status=500)
            
    except requests.exceptions.RequestException as e:
        return JsonResponse({
            'error': 'Sentiment service unavailable',
            'details': str(e)
        }, status=503)
    except Exception as e:
        return JsonResponse({
            'error': 'Internal server error',
            'details': str(e)
        }, status=500)

def sentiment_demo(request):
    """Demo page for sentiment analyzer"""
    return render(request, 'sentiment_service/demo.html')
