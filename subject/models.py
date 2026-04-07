from django.db import models
from course.models import Course
from teacher.models import Teacher

class Subject(models.Model):
    name=models.CharField(max_length=100) #varchar(200)
    course=models.ForeignKey(Course, #foreign key means Many to one towards course
                               on_delete=models.CASCADE,
                               related_name="subjects") #for reverse relation from course to subject
    
    teacher=models.ForeignKey(Teacher, #foreign key means Many to one towards teacher
                               on_delete=models.CASCADE,
                               related_name="subjects") #for reverse relation from teacher to subject

    def __str__(self):
        return self.name

# Create your models here.
