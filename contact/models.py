from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    file = models.FileField(blank=True)
    answered = models.BooleanField()
    send_date = models.DateTimeField(auto_now=True)
