from django.db import models
from API.models.userModel import User

class Points(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
