from django.db import models


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
