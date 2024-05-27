from rest_framework.routers import DefaultRouter
from .views import VehicleTypeViewSet, VehicleViewSet


router = DefaultRouter()
router.register(r"vehiclestype", VehicleTypeViewSet)
router.register(r"vehicles", VehicleViewSet)

urlpatterns = router.urls
