from courses.models import CoursesModel
from rest_framework import serializers

class CoursesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoursesModel
        exclude = ('id', )