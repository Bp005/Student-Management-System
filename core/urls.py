"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from student.views import StudentViewSet
from rest_framework.routers import DefaultRouter
from teacher.views import TeacherViewSet
from subject.views import SubjectViewSet
from course.views import CourseViewSet
# Create a router and register our viewset

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'course',CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # This handles /students/, /students/1/, etc.
    path('api/',include(router.urls)),
]
# Django does:
# Checks ROOT_URLCONF
# Opens urls.py
# Reads urlpatterns
# Finds match: 'dashboard/'
# Calls:
# dashboard(request)
# View returns HTML
# Browser displays page