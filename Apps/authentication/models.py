from django.db import models
from Apps.baseModel import BaseModel

class Role(BaseModel):
    description = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'role'
        
class User(BaseModel):
    user_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField(unique=True, max_length=40)
    user_password = models.CharField(max_length=30)
    document_type = models.CharField()
    user_document = models.CharField(unique=True, max_length=20)
    user_token = models.CharField(max_length=10, blank=True, null=True)
    ip_address = models.CharField(blank=True, null=True)
    role = models.ManyToManyField(Role, db_table="user_role")
    
    class Meta:
        managed = False
        db_table = "user"

