from rest_framework import serializers
from API.models.creditCardModel import CreditCard

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'

