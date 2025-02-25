from django.db import models

class LahoreHotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default="Lahore")
    rating = models.FloatField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class IslamabadHotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default="Islamabad")
    rating = models.FloatField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
