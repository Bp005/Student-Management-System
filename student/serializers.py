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
    #read_only=True is critical here — it means:
# GET requests → return the full teacher object ✅
# POST/PUT requests → don't try to create a new Teacher from this data ✅

    #This automatically includes all fields of the Student model in the serializer
    class Meta:#setting for the serializer ho yo chai 
        model= Student#model lai link gareko
        fields=["id","name","roll_no","age","phone","teacher","course"]#include all fields of the model


# Client sends request (JSON)
# Serializer validates data
# Saves to DB
# Returns JSON response

    def validate_age(self,value):
        if value <5 or value >50:
            raise serializers.ValidationError("age must be between 5 and 50")
        return value #always return the value if this valid
    
    def validate_roll_no(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Roll no must contain digits only")
        return value