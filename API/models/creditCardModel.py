from django.db import models
from API.models.baseModel import BaseModel
from API.models.userModel import User

class CreditCard(BaseModel):
    cardholder_name = models.CharField(max_length=40)
    expiration_date = models.DateField()
    cvv = models.IntegerField()
    client = models.ForeignKey(User, models.DO_NOTHING)
    card_number = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'credit_card'