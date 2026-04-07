from .models import Course  # Import your Course model
from rest_framework import viewsets
from .serializer import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset= Course.objects.all()
    serializer_class=CourseSerializer
