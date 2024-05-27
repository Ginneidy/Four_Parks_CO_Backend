from django.shortcuts import render
from Apps.baseViewSet import BaseViewSet
from .models import FeeType, Fee, Loyalty
from .serializers import FeeTypeSerializer, FeeSerializer, LoyaltySerializer

class FeeTypeViewSet(BaseViewSet):
    queryset = FeeType.objects.all()
    serializer_class = FeeTypeSerializer


class FeeViewSet(BaseViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

class LoyaltyViewSet(BaseViewSet):
    queryset = Loyalty.objects.all()
    serializer_class = LoyaltySerializer