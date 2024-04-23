from django.db import models
from API.models.parkingLotModel import ParkingLot
from API.models.scheduleModel import Schedule

class Parking_schedule(models.Model):
    parking_id = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
