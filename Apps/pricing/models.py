from django.db import models
from Apps.baseModel import BaseModel
from Apps.vehicle.models import VehicleType
from Apps.authentication.models import User

class FeeType(BaseModel):
    description = models.CharField(unique=True, max_length=30, db_comment='El tipo de tarifa que es (hora, dia, minuto)')

    class Meta:
        managed = False
        db_table = 'fee_type'
        
class Fee(BaseModel):
    amount = models.IntegerField()
    fee_type = models.ForeignKey(FeeType, on_delete=models.CASCADE, related_name='fees_related_to_fee_type')
    vehicle_type = models.ForeignKey(VehicleType,  on_delete=models.CASCADE, related_name='fees_related_to_vehicle_type')

    class Meta:
        managed = False
        db_table = 'fee'
        
class Loyalty(BaseModel):
    amount_points = models.IntegerField(db_comment='La cantidad de dinero que da 1 un punto')
    amount_per_point = models.IntegerField(db_comment='El valor de cada punto')

    class Meta:
        managed = False
        db_table = 'loyalty'

class Points(BaseModel):
    amount = models.IntegerField(db_comment='La cantidad de puntos que tiene una persona')
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'points'
