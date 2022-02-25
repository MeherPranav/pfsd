from django.db import models
from .places import Places

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=50)
    number_of_tables = models.IntegerField(default=0)
    Places = models.ForeignKey(Places, on_delete=models.CASCADE, default=0)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_restaurants_by_id(ids):
        return Restaurant.objects.filter(id__in=ids)

    @staticmethod
    def get_all_restaurants():
        return Restaurant.objects.all()
    
    @staticmethod
    def get_all_restaurants_by_placesid(places_id):
        if places_id:
            return Restaurant.objects.filter(category = places_id)
        else:
            return Restaurant.get_all_restaurants()