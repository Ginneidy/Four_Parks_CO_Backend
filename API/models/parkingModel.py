from django.db import models
from API.models.baseModel import BaseModel
from API.models.userModel import User
from API.models.cityModel import City
from API.models.parkingTypeModel import ParkingType
from API.models.loyaltyModel import Loyalty

class Parking(BaseModel):  
    park_name = models.CharField(unique=True, max_length=40)
    spaces = models.IntegerField()
    street_address = models.CharField(unique=True, max_length=40)
    admin = models.ForeignKey(User, models.DO_NOTHING)
    city = models.ForeignKey(City, models.DO_NOTHING)
    parking_type = models.ForeignKey(ParkingType, models.DO_NOTHING)
    loyalty = models.ForeignKey(Loyalty, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parking'