from django.db import models
from API.models.baseModel import BaseModel

class City(BaseModel):
    city_name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'city'