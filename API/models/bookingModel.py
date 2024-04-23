from django.db import models

from API.models.userModel import User
from API.models.parkingLotModel import ParkingLot
from API.models.vehicleModel import Vehicle

class Booking(models.Model):
   id = models.AutoField(primary_key=True)
   date = models.DateTimeField()
   client_id = models.ForeignKey(User, on_delete=models.CASCADE)
   parking_id = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
   vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)