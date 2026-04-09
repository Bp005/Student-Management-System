from .models import Teacher
from .serializer import TeacherSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes = [IsAuthenticated] 


