from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('get_dealers/', views.get_dealers, name='get_dealers'),
    path('dealer/<int:dealer_id>/', views.dealer_details, name='dealer_details'),
    path('add_review/<int:dealer_id>/', views.add_review, name='add_review'),
    path('get_dealers/<str:state>/', views.get_dealers_by_state, name='get_dealers_by_state'),
]