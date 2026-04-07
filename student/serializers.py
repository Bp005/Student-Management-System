#converts student db objects to json format
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    #This automatically includes all fields of the Student model in the serializer
    class Meta:#setting for the serializer ho yo chai 
        model= Student#model lai link gareko
        fields="__all__"#include all fields of the model


# Client sends request (JSON)
# Serializer validates data
# Saves to DB
# Returns JSON response