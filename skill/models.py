from django.db import models


class SkillModel(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    
