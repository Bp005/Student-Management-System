#converts student db objects to json format
from rest_framework import serializers
from .models import Student
from teacher.serializer import TeacherSerializer
from course.serializer import CourseSerializer

class StudentSerializer(serializers.ModelSerializer):
    # Overriding the fields to use Nested Serializers
    # read_only=True ensures we don't break the POST/PUT methods
    teacher= TeacherSerializer(read_only=True)
    course= CourseSerializer(read_only=True)
    
    
    #This automatically includes all fields of the Student model in the serializer
    class Meta:#setting for the serializer ho yo chai 
        model= Student#model lai link gareko
        fields="__all__"#include all fields of the model


# Client sends request (JSON)
# Serializer validates data
# Saves to DB
# Returns JSON response