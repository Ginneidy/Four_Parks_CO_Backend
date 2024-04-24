from rest_framework import serializers
from API.models.loyalityModel import Loyalty
class LoyaltySerializer(serializers.ModelSerializer):
   class Meta:
      model = Loyalty
      fields = ['amount_points', 'amount_per_point']