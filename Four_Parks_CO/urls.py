from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", include_docs_urls(title="Four_Parks_CO API Documentation")),
    path("api/auth/", include("Apps.authentication.urls")),
    path("api/parking/", include("Apps.parking.urls")),
    path("api/reservation/", include("Apps.reservation_billing.urls")),
    path("api/pricing/", include("Apps.pricing.urls")),
    path("api/vehicle/", include("Apps.vehicle.urls")),
]
