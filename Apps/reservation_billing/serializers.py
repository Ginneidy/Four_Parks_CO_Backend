from rest_framework import serializers

from Apps.authentication.models import User
from .models import Booking, PaymentMethod, Bill, CreditCard
from Apps.authentication.serializers import UserSerializer
from Apps.vehicle.serializers import VehicleSerializer
from Apps.vehicle.models import Vehicle
from Apps.parking.models import Parking
from Apps.parking.serializers import ParkingSerializer

from helpers.get_helpers import get_current_datetime


class BookingWriteSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data):
        # Validar que check_in sea anterior a check_out
        if data["check_in"] >= data["check_out"]:
            raise serializers.ValidationError(
                "El check-in debe ser antes del check-out."
            )
        return data

    def create(self, validated_data):
        vehicle_data = validated_data.pop("vehicle")
        vehicle, created = Vehicle.objects.get_or_create(
            plate=vehicle_data["plate"],
            defaults={**vehicle_data, "created_date": get_current_datetime()},
        )
        booking = Booking.objects.create(
            vehicle=vehicle, created_date=get_current_datetime(), **validated_data
        )
        return booking


class BookingReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    parking = ParkingSerializer()
    vehicle = VehicleSerializer()

    class Meta:
        model = Booking
        fields = "__all__"



class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = "__all__"
