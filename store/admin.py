# from Eshop.Eshop.store.models.restaurants import Restaurant
from django.contrib import admin

from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.restaurants import Restaurant
from .models.places import Places


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
class AdminRestaurant(admin.ModelAdmin):
    list_display=['restaurant_name', 'number_of_tables','Places']
class AdminPlaces(admin.ModelAdmin):
    list_display = ['place_name']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Restaurant,AdminRestaurant)
admin.site.register(Places,AdminPlaces)
