from django.db import models
from Apps.authentication.models import User
from Apps.pricing.models import Fee
from Apps.pricing.models import Loyalty


from Apps.baseModel import BaseModel

class Schedule(BaseModel):
    week_day = models.IntegerField()
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'schedule'

class ParkingType(BaseModel):
    description = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'parking_type'

class City(BaseModel):
    city_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'city'
        
class Parking(BaseModel):  
    park_name = models.CharField(unique=True, max_length=40)
    spaces = models.IntegerField()
    street_address = models.CharField(unique=True, max_length=40)
    admin = models.ForeignKey(User, models.DO_NOTHING)
    city = models.ForeignKey(City, models.DO_NOTHING)
    parking_type = models.ForeignKey(ParkingType, models.DO_NOTHING)
    loyalty = models.ForeignKey(Loyalty, models.DO_NOTHING, blank=True, null=True)
    schedule = models.ManyToManyField(Schedule, db_table="parking_schedule")
    fee = models.ManyToManyField(Fee, db_table="parking_fee")

    class Meta:
        managed = False
        db_table = 'parking'