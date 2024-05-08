from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from Apps.parking import views as parkingViews
from Apps.authentication import views as authenticationViews

router = DefaultRouter()
router.register(r"parkings", parkingViews.ParkingViewSet)
router.register(r"users", authenticationViews.UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/", include("API.urls")),
    path("docs/", include_docs_urls(title="Four_Parks_CO API Documentation")),
    path("api/", include(router.urls)),
    # path("api-auth/", UserLoginView.as_view(), name="user-login"),
]
