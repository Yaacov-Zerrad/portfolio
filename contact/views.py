from django.shortcuts import render
from contact.models import ContactModel
from contact.serializers import ContactSerializer
from rest_framework import viewsets

class ContactViewSet(viewsets.ModelViewSet):
    
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
