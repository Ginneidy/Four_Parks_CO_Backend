from django.db import models
from API.models.userModel import User
from API.models.roleModel import Role

class User_role(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
