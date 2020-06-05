from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import StudentsSerializer

from .models import Students
# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer


""" def index(request):
    students = []
    for student in Students.objects.all():
        students.append({
            'name': student.name,
            'course': student.course,
            'rating': student.rating,
        })
    return JsonResponse(students, safe=False) """
