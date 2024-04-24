from django.urls import path,include
from rest_framework import routers
import API.views as v

router = routers.DefaultRouter()
router.register(r'parkinglots', v.ParkingLotViewSet, basename='parkinglot')
router.register(r'users', v.UserViewSet, basename='user')
router.register(r'bookings', v.BookingViewSet, basename='booking')
router.register(r'cities', v.CityViewSet, basename='city')
router.register(r'parking_types', v.ParkingTypeViewSet, basename='parking_type')
router.register(r'loyalties', v.LoyaltyViewSet, basename='loyalty')
urlpatterns = [
   path('', include(router.urls)),
]
