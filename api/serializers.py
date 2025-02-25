from rest_framework import serializers
from .models import LahoreHotel, IslamabadHotel

class LahoreHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LahoreHotel
        fields = '__all__'

class IslamabadHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IslamabadHotel
        fields = '__all__'
