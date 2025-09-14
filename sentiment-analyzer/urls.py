from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.analyze_sentiment, name='analyze_sentiment'),
]