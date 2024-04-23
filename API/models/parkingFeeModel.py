from django.db import models

from API.models.feeModel import Fee
from API.models.parkingLotModel import ParkingLot
class ParkingFee(models.Model):
   fee_id = models.ForeignKey(Fee, on_delete=models.CASCADE)
   parking_id = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
