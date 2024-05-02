from django.db import models
from API.models.baseModel import BaseModel

class Loyalty(BaseModel):
    amount_points = models.IntegerField(db_comment='La cantidad de dinero que da 1 un punto')
    amount_per_point = models.IntegerField(db_comment='El valor de cada punto')

    class Meta:
        managed = False
        db_table = 'loyalty'