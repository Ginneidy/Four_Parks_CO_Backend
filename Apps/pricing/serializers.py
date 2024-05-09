from rest_framework import serializers
from .models import Fee, FeeType,Loyalty,Points

class FeeSerializer(serializers.ModelSerializer):
   class Meta:
      model = Fee
      fields = ['amount', 'fee_type', 'vehicle_type']
      
class FeeTypeSerializer(serializers.ModelSerializer):
   class Meta:
      model = FeeType
      fields = '__all__'

class LoyaltySerializer(serializers.ModelSerializer):
   class Meta:
      model = Loyalty
      fields = '__all__'
      
class PointsSerializer(serializers.ModelSerializer):
   class Meta:
      model = Points
      fields = ["amount"]