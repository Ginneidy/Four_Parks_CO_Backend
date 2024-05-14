from rest_framework import serializers
from .models import Booking, PaymentMethod, Bill, CreditCard
from Apps.authentication.serializers import UserSerializer

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "check_in", "user", "parking", "vehicle", "check_out"]


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
