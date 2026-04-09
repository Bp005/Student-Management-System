from django.db import models
from teacher.models import Teacher
from course.models import Course
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=100)
    address=models.CharField(max_length=100 )
    phone=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    age=models.IntegerField(null=True)

    is_deleted=models.BooleanField(default=False)

    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="student")
    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name="student")
    

    def __str__(self):
        return self.name
    