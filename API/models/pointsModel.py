from django.db import models
from API.models.baseModel import BaseModel
from API.models.userModel import User

class Points(BaseModel):
    amount = models.IntegerField(db_comment='La cantidad de puntos que tiene una persona')
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'points'