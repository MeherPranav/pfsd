from django.db import models


class Places(models.Model):
    place_name = models.CharField(max_length=20)


    @staticmethod
    def get_all_places():
        return Places.objects.all()

    def __str__(self):
        return self.place_name
