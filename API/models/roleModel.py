from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    decription = models.CharField(max_length=30)
