# startwars/views.py
#from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CharacterSerializers
from .models import Character

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('name')
    serializer_class =CharacterSerializers
