from rest_framework.routers import DefaultRouter
from .views import ParkingViewSet, ScheduleViewSet, CityViewSet, ParkingTypeViewSet


router = DefaultRouter()
router.register(r"parkings", ParkingViewSet)
router.register(r"schedules", ScheduleViewSet)
router.register(r"cities", CityViewSet)
router.register(r"parkingtypes", ParkingTypeViewSet)

urlpatterns = router.urls
