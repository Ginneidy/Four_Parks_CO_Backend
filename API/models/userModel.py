from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=30, default="0.0.0.0")
    document_type = models.CharField(max_length=30)
    document = models.CharField(max_length=30, default=None)
    name_credit_card = models.CharField(max_length=30, default=None)
    credit_number_card = models.IntegerField(default=None)
    token = models.CharField(max_length=30, default=None)    
    
    def __str__(self):
        return self.name