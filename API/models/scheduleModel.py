from django.db import models
from API.models.baseModel import BaseModel

class Schedule(BaseModel):
    week_day = models.IntegerField()
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'schedule'