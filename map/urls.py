from django import urls
from django.urls import path 
from . import views

urlpatterns = [
    path('Map', views.Map, name = 'Map'),
    path('email',views.Email,name='email')        
]