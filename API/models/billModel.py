from django.db import models

from API.models.paymentMethodModel import PaymentMethod
from API.models.bookingModel import Booking


class Bill(models.Model):
   id = models.AutoField(primary_key=True)   
   code = models.CharField(max_length=30)
   vehicle_entry = models.DateTimeField()
   vehicle_exit = models.DateTimeField()
   total_time = models.TimeField()
   points_used = models.IntegerField()
   booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
   payment_method_id = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
  
   