from rest_framework.routers import DefaultRouter
from .views import ParkingViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r"parkings", ParkingViewSet)

urlpatterns = router.urls

