from django.db import models
class CoursesModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    files = models.FileField(blank=True)
    created_date = models.DateField(auto_now=True)