from django.contrib.auth.hashers import make_password, check_password
from django.contrib.messages import error
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.places import Places
from .models.restaurants import Restaurant
from django.views import View
from models.orders import Order
# Create your views here.

def post(self, request):
        if (request.method == 'POST'):
            idd=request.POST.get('one1')
            Order.objects.filter(id=idd).delete()
            customer = request.session.get('customer')
            orders = Order.get_orders_by_customer(customer)
            print(orders)
            return render(request, 'orders.html', {'orders': orders})


def index(request):
    products = None
    # print(products)
    # return render(request, 'orders/order.html')
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)

def index_1(request):
    restaurant = None
    # print(products)
    # return render(request, 'orders/order.html')
    Places = Places.get_all_places()
    PlaceID = request.GET.get('places')
    if PlaceID:
        restaurant = Restaurant.get_all_restaurants_by_placesid(PlaceID)
    else:
        restaurant = Restaurant.get_all_restaurants
    data_1 = {}
    data_1['restaurants'] = restaurant
    data_1['places'] = Places
    return HttpResponse(request, 'restaurants.html', data_1)

class Signup(View):

    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)

        if not first_name:
            error_message = "First name required"

        elif first_name:
            if len(first_name) < 4:
                error_message = "First name must be 4 characters long"

        if not last_name:
            error_message = "Last name required"

        elif last_name:
            if len(last_name) < 4:
                error_message = "Last name must be 4 characters long"

        if not phone:
            error_message = 'Phone Number required'

        if len(phone) < 10:
            error_message = 'Phone Number must be not less than 10 char Long'

        if len(phone) > 10:
            error_message = 'Phone Number must be not more than 10 char Long'

        if len(password) < 6:
            error_message = 'Password must be 6 char long'

        if len(email) < 5:
            error_message = 'Email must be 5 char long'

        if customer.isExists():
            error_message = "Email Address already registred"

        # saving
        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

class Login(View):

    def get(self, request):
        return render(request , 'login.html')
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})


