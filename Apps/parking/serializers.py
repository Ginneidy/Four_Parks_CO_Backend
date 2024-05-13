from rest_framework import serializers
from .models import Parking, City, ParkingType, Schedule
from Apps.authentication.serializers import UserSerializer
from Apps.pricing.serializers import LoyaltySerializer, FeeSerializer
from Apps.reservation_billing.models import Booking
from datetime import datetime

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class ParkingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingType
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["city_name"]


class ParkingSerializer(serializers.ModelSerializer):
    admin = UserSerializer()
    city = serializers.CharField(source="city.city_name")
    parking_type = serializers.CharField(source="parking_type.description")
    loyalty = LoyaltySerializer(allow_null=True)
    schedule = ScheduleSerializer(many=True, read_only=True)
    fee = FeeSerializer(many=True, read_only=True)
    available_capacity = serializers.SerializerMethodField()  # Campo calculado

    class Meta:
        model = Parking
        fields = "__all__"

    def get_available_capacity(self, obj):
        bookings = Booking.objects.filter(parking=obj, check_out__gte=datetime.now())
        total_booked_spaces = bookings.count()
        return obj.spaces - total_booked_spaces
