from datetime import datetime, time

from rest_framework import serializers

from .models import Parking, City, ParkingType, Schedule
from Apps.pricing.models import FeeType

from Apps.authentication.serializers import UserSerializer
from Apps.pricing.serializers import LoyaltySerializer
from Apps.reservation_billing.models import Booking


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class ParkingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingType
        fields = ["id", "description"]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "city_name"]


class ParkingSerializer(serializers.ModelSerializer):
    admin = UserSerializer()
    city = serializers.CharField(source="city.city_name")
    parking_type = serializers.CharField(source="parking_type.description")
    loyalty = LoyaltySerializer(allow_null=True)
    available_capacity = serializers.SerializerMethodField()  # Campo calculado
    opening_time = serializers.SerializerMethodField()
    closing_time = serializers.SerializerMethodField()
    is_24_hours = serializers.SerializerMethodField()
    hourly_rates = serializers.SerializerMethodField()

    class Meta:
        model = Parking
        fields = "__all__"

    def get_available_capacity(self, obj):
        bookings = Booking.objects.filter(parking=obj, check_out__gte=datetime.now())
        total_booked_spaces = bookings.count()
        return obj.spaces - total_booked_spaces

    def get_opening_time(self, obj):
        first_schedule = obj.schedule.first()
        return first_schedule.opening_time if first_schedule else None

    def get_closing_time(self, obj):
        first_schedule = obj.schedule.first()
        return first_schedule.closing_time if first_schedule else None

    def get_is_24_hours(self, obj):
        first_schedule = obj.schedule.first()
        if first_schedule:
            return first_schedule.opening_time == time(
                0, 0, 0
            ) and first_schedule.closing_time == time(0, 0, 0)
        return False

    def get_hourly_rates(self, obj):
        hourly_rate_fee_type = FeeType.objects.filter(description="hora").first()
        if hourly_rate_fee_type:
            hourly_rates = {}
            fees = obj.fee.filter(fee_type=hourly_rate_fee_type)
            for fee in fees:
                vehicle_type = fee.vehicle_type.description
                hourly_rates[vehicle_type] = fee.amount
            return hourly_rates
        return {}
