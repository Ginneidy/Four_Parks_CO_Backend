from django.db import models
from Apps.authentication.models import User
from Apps.parking.models import Parking
from Apps.vehicle.models import Vehicle
from Apps.baseModel import BaseModel


class Booking(BaseModel):
    check_in = models.DateTimeField()
    user = models.ForeignKey(
        User, models.DO_NOTHING, db_comment="Es el usuario que hizo la reserva"
    )
    parking = models.ForeignKey(Parking, models.DO_NOTHING)
    vehicle = models.ForeignKey(Vehicle, models.DO_NOTHING)
    check_out = models.DateTimeField()

    @property
    def total_amount(self):
        vehicle_type = self.vehicle.vehicle_type
        parking = self.parking
        fees = parking.fee.filter(vehicle_type=vehicle_type)

        # Obtenemos las tarifas
        hourly_fee = fees.get(fee_type__description="hora").amount
        daily_fee = fees.get(fee_type__description="dia").amount
        minute_fee = fees.get(fee_type__description="minuto").amount
        reservation_fee = fees.get(fee_type__description="reserva").amount

        duration = self.check_out - self.check_in

        # Cálculo del total
        total = reservation_fee

        if duration.days > 0:
            total += duration.days * daily_fee

        remaining_seconds = duration.seconds
        total += (remaining_seconds // 3600) * hourly_fee
        remaining_seconds %= 3600
        total += (remaining_seconds // 60) * minute_fee

        return total

    class Meta:
        managed = False
        db_table = "booking"


class PaymentMethod(BaseModel):
    description = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = "payment_method"


class Bill(BaseModel):
    code = models.CharField(unique=True, max_length=20)
    vehicle_entry = models.DateTimeField()
    vehicle_exit = models.DateTimeField()
    total_time = models.TimeField()
    points_used = models.IntegerField(blank=True, null=True)
    total_amount = models.IntegerField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "bill"


class CreditCard(BaseModel):
    cardholder_name = models.CharField(max_length=40)
    expiration_date = models.DateField()
    cvv = models.IntegerField()
    client = models.ForeignKey(User, models.DO_NOTHING)
    card_number = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "credit_card"
