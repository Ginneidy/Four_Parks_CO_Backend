from django.db import models
from API.models.baseModel import BaseModel

class FeeType(BaseModel):
    description = models.CharField(unique=True, max_length=30, db_comment='El tipo de tarifa que es (hora, dia, minuto)')

    class Meta:
        managed = False
        db_table = 'fee_type'