from rest_framework.routers import DefaultRouter
from .views import ParkingViewSet, ScheduleViewSet, CityViewSet


router = DefaultRouter()
router.register(r"parkings", ParkingViewSet)
router.register(r"schedules", ScheduleViewSet)
router.register(r"citys", CityViewSet)

urlpatterns = router.urls

