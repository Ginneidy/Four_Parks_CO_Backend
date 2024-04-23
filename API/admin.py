from django.contrib import admin
from .models.parkingLotModel import ParkingLot
from .models.userModel import User
# Register your models here.

admin.site.register(ParkingLot)
admin.site.register(User)

admin.site.site_header = 'Four_Parks_CO'
