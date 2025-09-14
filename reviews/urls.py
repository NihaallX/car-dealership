from django.urls import path
from . import views

urlpatterns = [
    path('dealer/<int:dealer_id>/', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('add_review/', views.add_review, name='add_review'),
]