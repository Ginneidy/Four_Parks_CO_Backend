from django.db import models
from API.models.baseModel import BaseModel
from API.models.bookingModel import Booking
from API.models.paymentMethodModel import PaymentMethod

class Bill(BaseModel):
    code = models.CharField(unique=True, max_length=20)
    vehicle_entry = models.DateTimeField()
    vehicle_exit = models.DateTimeField()
    total_time = models.TimeField()
    points_used = models.IntegerField(blank=True, null=True)
    total_amount = models.IntegerField()
    booking = models.ForeignKey(Booking, models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill'