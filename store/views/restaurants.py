from django.contrib.auth.hashers import make_password, check_password
from django.contrib.messages import error
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from store.models.product import Product
from store.models.restaurants import Restaurant
from store.models.places import Places
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

# Create your views here.

class Index_1(View):

    def post(self, request):

        remove = request.POST.get('remove')
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(Restaurant)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(Restaurant)
                    else:
                        cart[Restaurant] = quantity - 1
                else:
                    cart[Restaurant] = quantity + 1

            else:
                cart[Restaurant] = 1
        else:
            cart = {}
            cart[Restaurant] = 1

        request.session['cart'] = cart
        print("kkkkkkkk:",request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        restaurants = None
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        #request.session.get('cart').clear()
        # print(products)
        # return render(request, 'orders/order.html')
        places = Places.get_all_categories()
        PlaceID = request.GET.get('places')
        if PlaceID:
            restaurants = Restaurant.get_all_restaurants_by_placesid(PlaceID)
        else:
            restaurants = Restaurant.get_all_restaurants
        data = {}
        data['restaurants'] = restaurants
        data['places'] = places
        return render(request, 'restaurants.html', data)
