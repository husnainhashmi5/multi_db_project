from rest_framework import viewsets
from .models import LahoreHotel, IslamabadHotel
from .serializers import LahoreHotelSerializer, IslamabadHotelSerializer

class LahoreHotelViewSet(viewsets.ModelViewSet):
    queryset = LahoreHotel.objects.all()
    serializer_class = LahoreHotelSerializer

class IslamabadHotelViewSet(viewsets.ModelViewSet):
    queryset = IslamabadHotel.objects.all()
    serializer_class = IslamabadHotelSerializer
