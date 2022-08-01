from django.shortcuts import render
from rest_framework import viewsets
from skill.models import SkillModel
from skill.serializers import SkillSerializer

class SkillViewSet(viewsets.ModelViewSet):
    
    queryset = SkillModel.objects.all()
    serializer_class = SkillSerializer