from rest_framework import serializers
from API.models.loyaltyModel import Loyalty

class LoyaltySerializer(serializers.ModelSerializer):
    class Meta:
        model = Loyalty
        fields = '__all__'