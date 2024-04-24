from django.contrib import admin
import API.models as m  
# Register your models here.

admin.site.register(m.ParkingLot)
admin.site.register(m.User)
admin.site.register(m.Booking)
admin.site.register(m.City)
admin.site.register(m.Parking_type)
admin.site.register(m.Loyalty)

admin.site.site_header = 'Four_Parks_CO'
