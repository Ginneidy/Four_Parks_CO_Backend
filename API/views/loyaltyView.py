from rest_framework import viewsets
from API.models.loyaltyModel import Loyalty
from API.serializers.loyaltySerializer import LoyaltySerializer

class LoyaltyViewSet(viewsets.ModelViewSet):
    queryset = Loyalty.objects.all()
    serializer_class = LoyaltySerializer