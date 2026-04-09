from rest_framework import viewsets
from .models import Student
from rest_framework.permissions import IsAuthenticated

from .serializers import StudentSerializer
#No need to write separate crud. ModelViewSet handles all get,post,put,delete operations
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes = [IsAuthenticated] 


    def get_queryset(self):
        # request.user is automatically the logged-in user from the JWT token
        user = self.request.user
        return Student.objects.filter(teacher__user=user)
        # This means: only return students whose teacher is linked to this logged-in use




# from .models import Course, Teacher

# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'course_list.html', {'courses': courses})

# def teacher_list(request):
#     teachers = Teacher.objects.all()
#     return render(request, 'teacher_list.html', {'teachers': teachers})

# def subject_list(request):
#     # select_related makes the database query efficient for ForeignKeys
#     subjects = Subject.objects.select_related('course', 'teacher').all()
#     return render(request, 'subject_list.html', {'subjects': subjects})
# Create your views here.
