from rest_framework.routers import DefaultRouter
from .views import FeeTypeViewSet, FeeViewSet, LoyaltyViewSet


router = DefaultRouter()
router.register(r"feetypes", FeeTypeViewSet)
router.register(r"fees", FeeViewSet)
router.register(r"loyalties", LoyaltyViewSet)

urlpatterns = router.urls
