from django.urls import path,include
from rest_framework import routers
import API.views as v

router = routers.DefaultRouter()
router.register(r'parkinglots', v.ParkingLotViewSet, basename='parkinglot')
router.register(r'users', v.UserViewSet, basename='user')
router.register(r'reservations', v.BookingViewSet, basename='reservations')
router.register(r'cities', v.CityViewSet, basename='city')
router.register(r'parking_types', v.ParkingTypeViewSet, basename='parking_type')
router.register(r'loyalties', v.LoyaltyViewSet, basename='loyalty')
router.register(r'vehicles', v.VehicleViewSet, basename='vehicle')
urlpatterns = [
   path('', include(router.urls)),
]
