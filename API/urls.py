from rest_framework.routers import DefaultRouter
from django.urls import path, include
import API.views as Views



router = DefaultRouter()
router.register('bills', Views.BillViewSet, basename='bill')
router.register('bookings', Views.BookingViewSet, basename='booking')
router.register('citys', Views.CityViewSet, basename='city')
router.register('creditCards', Views.CreditCardViewSet, basename='fee')
router.register('feeType', Views.FeeTypeViewSet, basename='feeType')
router.register('loyalty', Views.LoyaltyViewSet, basename='loyalty')
router.register('parkingFee', Views.ParkingFeeViewSet, basename='parkingFee')
router.register('parkingSchedule', Views.ParkingScheduleViewSet, basename='parkingSchedule')
router.register('parkingType', Views.ParkingTypeViewSet, basename='parkingType')
router.register('parking', Views.ParkingViewSet, basename='parking')
router.register('paymentMethod', Views.PaymentMethodViewSet, basename='paymentMethod')
router.register('points', Views.PointsViewSet, basename='points')
router.register('role', Views.RoleViewSet, basename='role')
router.register('schedule', Views.ScheduleViewSet, basename='schedule')
router.register('userRole', Views.UserRoleViewSet, basename='userRole')
router.register('users', Views.UserViewSet, basename='user')
router.register('vehicleType', Views.VehicleTypeViewSet, basename='vehicleType')
router.register('vehicle', Views.VehicleViewSet, basename='vehicle')

urlpatterns = [
   path('', include(router.urls)),
]


"""from django.urls import path,include
from rest_framework import routers
import API.views as v

router = routers.DefaultRouter()
router.register(r'parkinglots', v.ParkingLotViewSet, basename='parkinglot')
router.register(r'users', v.UserViewSet, basename='user')
router.register(r'reservations', v.BookingViewSet, basename='reservations')
router.register(r'cities', v.CityViewSet, basename='city')
router.register(r'parking_types', v.ParkingTypeViewSet, basename='parking_type')
router.register(r'loyalties', v.LoyaltyViewSet, basename='loyalty')
router.register(r'vehicles', v.VehicleViewSet, basename='vehicle')
urlpatterns = [
   path('', include(router.urls)),
]
"""