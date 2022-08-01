from django.shortcuts import render
from courses.models import CoursesModel
from courses.serializers import CoursesSerializer
from rest_framework import viewsets

class CoursViewSet(viewsets.ModelViewSet):
    
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer
