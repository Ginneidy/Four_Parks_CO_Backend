from rest_framework.routers import DefaultRouter
from .views import FeeTypeViewSet


router = DefaultRouter()
router.register(r"feetypes", FeeTypeViewSet)

urlpatterns = router.urls
