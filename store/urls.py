# from Eshop.Eshop.store.models.restaurants import Restaurant

from django.contrib import admin
from django.http import response
from django.urls import path

from .views.analysis import Analysis
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.home import Index
from .views.orders import OrderView
from .views.signup import Signup
from .views.login import Login,logout
from .middlewares.auth import auth_middleware
from .views.restaurants import Index_1
from . import views

urlpatterns = [
    path('', Index.as_view(), name = 'homepage'),
    path('signup', Signup.as_view(), name = 'signup'),
    path('login', Login.as_view(), name = 'login'),
    path('logout', logout, name = 'Logout'),
    path('cart', Cart.as_view(), name = 'cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('pie-chart',Analysis.as_view(), name='pie-chart'),
    path('restaurants',Index_1.as_view(), name='restaurants'),
    
]