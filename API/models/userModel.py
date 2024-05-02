from django.db import models
from API.models.baseModel import BaseModel

class User(models.Model):
    user_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField(unique=True, max_length=40)
    user_password = models.CharField(max_length=30)
    document_type = models.CharField()
    user_document = models.CharField(unique=True, max_length=20)
    user_token = models.CharField(max_length=10, blank=True, null=True)
    ip_address = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'