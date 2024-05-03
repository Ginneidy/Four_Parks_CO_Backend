from rest_framework import viewsets
from API.models.creditCardModel import CreditCard
from API.serializers.creditCardSerializer import CreditCardSerializer

class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer