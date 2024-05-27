from django.db import models
from Apps.baseModel import BaseModel

class VehicleType(BaseModel):
    description = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = "vehicle_type"



class Vehicle(BaseModel):
    plate = models.CharField(unique=True, max_length=8)
    vehicle_type = models.ForeignKey(VehicleType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "vehicle"
