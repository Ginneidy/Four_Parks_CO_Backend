from rest_framework.routers import DefaultRouter
from .views import CreditCardViewSet, BookingViewSet


router = DefaultRouter()
router.register(r"creditCards", CreditCardViewSet)
router.register(r"bookings", BookingViewSet)
urlpatterns = router.urls
