from rest_framework import viewsets
from API.models.paymentMethodModel import PaymentMethod
from API.serializers.paymentMethodSerializer import PaymentMethodSerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
