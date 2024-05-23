from django.shortcuts import render
from Apps.baseViewSet import BaseViewSet  
from .models import FeeType
from .serializers import FeeTypeSerializer
# Create your views here.

class FeeTypeViewSet(BaseViewSet):
    queryset = FeeType.objects.all()
    serializer_class = FeeTypeSerializer

