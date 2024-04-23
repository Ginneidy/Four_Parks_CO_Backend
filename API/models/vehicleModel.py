from django.db import models
from API.models.vehicleTypeModel import VehicleType

class Vehicle(models.Model):
   id = models.AutoField(primary_key=True)
   plate = models.CharField(max_length=30)
   vehicle_type_id = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
   