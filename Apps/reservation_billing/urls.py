from rest_framework.routers import DefaultRouter
from .views import CreditCardViewSet


router = DefaultRouter()
router.register(r"creditCards", CreditCardViewSet)
urlpatterns = router.urls
