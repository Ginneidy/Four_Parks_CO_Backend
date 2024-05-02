from django.db import models
from API.models.baseModel import BaseModel
from API.models.vehicleTypeModel import VehicleType

class Vehicle(BaseModel):
    plate = models.CharField(unique=True, max_length=8)
    vehicle_type = models.ForeignKey(VehicleType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vehicle'