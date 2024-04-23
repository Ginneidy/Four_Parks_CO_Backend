from django.db import models


class Loyality(models.Model):
    id = models.AutoField(primary_key=True)
    amount_points = models.IntegerField()
    amount_per_point = models.IntegerField()
