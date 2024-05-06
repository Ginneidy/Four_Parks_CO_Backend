from django.db import models
from API.models.baseModel import BaseModel
from API.models.feeTypeModel import FeeType
from API.models.vehicleTypeModel import VehicleType

class Fee(BaseModel):
    amount = models.IntegerField()
    fee_type = models.ForeignKey(FeeType, on_delete=models.CASCADE, related_name='fees_related_to_fee_type')
    vehicle_type = models.ForeignKey(FeeType,  on_delete=models.CASCADE, related_name='fees_related_to_vehicle_type')

    class Meta:
        managed = False
        db_table = 'fee'
