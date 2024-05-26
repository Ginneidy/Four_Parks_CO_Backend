from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from django.db import transaction
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.http import HttpResponse

from Apps.reservation_billing.models import Booking, PaymentMethod, Bill, CreditCard
from Apps.reservation_billing.serializers import (
    BookingSerializer,
    PaymentMethodSerializer,
    BillSerializer,
    CreditCardSerializer,
)
from Apps.vehicle.models import Vehicle
from Apps.baseViewSet import BaseViewSet
from Apps.authentication.models import User
from Apps.parking.models import Parking, Fee
from Apps.vehicle.models import VehicleType

from helpers.get_helpers import get_current_datetime
from helpers.validate_helpers import validate_credit_card
from helpers.email_helpers import (
    send_mail_confirmation_reservation,
    send_payment_confirmation_mail,
)


# views.py


def hacer_reserva(user, credit_card, booking):
    return HttpResponse("Reserva exitosa")


class BookingViewSet(BaseViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        user = get_object_or_404(User, id=request.data.get("user"))
        parking = get_object_or_404(Parking, id=request.data.get("parking"))
        credit_card = get_object_or_404(CreditCard, client=user)
        booking = get_object_or_404(Booking, id=serializer.data.get("id"))

        send_mail_confirmation_reservation(user, parking, serializer.data)

        # TODO: Implementar la fidelización
        send_payment_confirmation_mail(user, credit_card, booking)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    # [POST] api/reservation/booking_total/
    @action(detail=False, methods=["POST"])
    def booking_total(self, request, *args, **kwargs):
        data = request.data
        vehicle_type_id = data.get(
            "vehicle_type", 3
        )  # Usar el tipo de vehículo predeterminado si no se proporciona

        try:
            vehicle_type = VehicleType.objects.get(id=vehicle_type_id)
        except VehicleType.DoesNotExist:
            return Response({"error": "Invalid vehicle type"}, status=400)

        parking_id = data.get("parking_id")

        try:
            parking = Parking.objects.get(id=parking_id)
        except Parking.DoesNotExist:
            return Response({"error": "Invalid parking ID"}, status=400)

        check_in = datetime.fromisoformat(data.get("check_in"))
        check_out = datetime.fromisoformat(data.get("check_out"))

        fees = parking.fee.filter(vehicle_type=vehicle_type)

        # Obtenemos las tarifas
        try:
            hourly_fee = fees.get(fee_type__description="hora").amount
            daily_fee = fees.get(fee_type__description="dia").amount
            minute_fee = fees.get(fee_type__description="minuto").amount
            reservation_fee = fees.get(fee_type__description="reserva").amount
        except Fee.DoesNotExist:
            return Response(
                {"error": "Fee information is incomplete for the given vehicle type"},
                status=400,
            )

        duration = check_out - check_in

        # Cálculo del total
        total = reservation_fee

        if duration.days > 0:
            total += duration.days * daily_fee

        remaining_seconds = duration.seconds
        total += (remaining_seconds // 3600) * hourly_fee
        remaining_seconds %= 3600
        total += (remaining_seconds // 60) * minute_fee

        return Response({"total_amount": total})


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
