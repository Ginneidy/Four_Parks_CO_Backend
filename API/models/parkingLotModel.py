from django.db import models
from API.models.loyalityModel import Loyality
from API.models.userModel import User
from API.models.cityModel import City
from API.models.parkingTypeModel import Parking_type


#
class ParkingLot(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    spaces = models.IntegerField()
    statuts = models.BooleanField(default=True, blank=True)
    address = models.CharField(max_length=30)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    parking_type_id = models.ForeignKey(Parking_type, on_delete=models.CASCADE)
    loyalty_id = models.ForeignKey(Loyality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
