from django.db import models

class VehicleType(models.Model):
   id = models.AutoField(primary_key=True)
   description = models.CharField(max_length=30)

