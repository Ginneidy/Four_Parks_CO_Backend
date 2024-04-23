from django.urls import path,include
from rest_framework import routers
import API.views as v

router = routers.DefaultRouter()
router.register(r'parkinglots', v.ParkingLotViewSet, basename='parkinglot')
router.register(r'users', v.UserViewSet, basename='user')

urlpatterns = [
   path('', include(router.urls)),
]
