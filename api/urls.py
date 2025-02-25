from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LahoreHotelViewSet, IslamabadHotelViewSet

router = DefaultRouter()
router.register(r'lahore-hotels', LahoreHotelViewSet)
router.register(r'islamabad-hotels', IslamabadHotelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
