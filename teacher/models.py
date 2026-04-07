from django.db import models


class Teacher(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    join_date=models.DateField()
    is_active=models.BooleanField(default=True)    

    

    def __str__(self):
        return self.name