from django.db import models
from API.models.baseModel import BaseModel
from API.models.userModel import User
from API.models.parkingModel import Parking
from API.models.vehicleModel import Vehicle

class Booking(BaseModel):
    check_in = models.DateTimeField()
    user = models.ForeignKey(User, models.DO_NOTHING, db_comment='Es el usuario que hizo la reserva')
    parking = models.ForeignKey(Parking, models.DO_NOTHING)
    vehicle = models.ForeignKey(Vehicle, models.DO_NOTHING)
    check_out = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'booking'