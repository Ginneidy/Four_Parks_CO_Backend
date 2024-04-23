from django.db import models

from API.models.feeTypeModel import FeeType
from API.models.vehicleTypeModel import VehicleType
class Fee(models.Model):
   id = models.AutoField(primary_key=True)
   amount = models.IntegerField()
   fee_type = models.ForeignKey(FeeType, on_delete=models.CASCADE)
   vehicle_type_id = models.ForeignKey(VehicleType, on_delete=models.CASCADE)

