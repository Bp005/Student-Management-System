from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    join_date=models.DateField()
    is_active=models.BooleanField(default=True)    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name