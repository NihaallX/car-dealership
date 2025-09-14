from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cars', views.CarMakeViewSet)
router.register(r'models', views.CarModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('carmakes/', views.get_cars, name='get_cars'),
]