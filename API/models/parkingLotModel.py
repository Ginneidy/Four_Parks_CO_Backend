from django.db import models
from API.models.loyalityModel import Loyalty
from API.models.userModel import User
from API.models.cityModel import City
from API.models.parkingTypeModel import Parking_type
#from API.models.bookingModel import Booking


#
class ParkingLot(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    spaces = models.IntegerField()
    current_capacity = models.IntegerField(default=0)
    statuts = models.BooleanField(default=True, blank=True)
    address = models.CharField(max_length=30)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    parking_type_id = models.ForeignKey(Parking_type, on_delete=models.CASCADE)
    loyalty_id = models.ForeignKey(Loyalty, on_delete=models.CASCADE)
    #booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_current_capacity(self):
        return self.current_capacity - self.spaces
