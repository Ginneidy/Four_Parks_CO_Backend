from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from Apps.reservation_billing.models import Booking, PaymentMethod, Bill, CreditCard
from Apps.reservation_billing.serializers import (
    BookingSerializer,
    PaymentMethodSerializer,
    BillSerializer,
    CreditCardSerializer,
)
from Apps.baseViewSet import BaseViewSet
from Apps.authentication.models import User

from helpers.helpers import get_current_datetime, validate_credit_card


class BookingViewSet(BaseViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class PaymentMethodViewSet(BaseViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class BillViewSet(BaseViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class CreditCardViewSet(BaseViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

    # [POST] api/reservation/creditCards/
    def create(self, request, *args, **kwargs):
        created_date = get_current_datetime()

        with transaction.atomic():
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                if not validate_credit_card(request.data):
                    return Response(
                        {"message": "Tarjeta de Credito invalida"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                else:
                    serializer.save(created_date=created_date)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"error": "Datos no válidos proporcionados"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

    # [GET] api/reservation/creditCards/{user_id}/user_credit_card/
    @action(detail=True, methods=["GET"])
    def user_credit_card(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        credit_card = CreditCard.objects.filter(client=user).first()
        if credit_card:
            serializer = self.serializer_class(credit_card)
            return Response(serializer.data)
        else:
            return Response(
                {
                    "message": "No se encontró ninguna tarjeta de crédito para este usuario"
                },
                status=status.HTTP_404_NOT_FOUND,
            )
