from dataclasses import field
from django.shortcuts import render
from rest_framework import generics
from .models import Profil
from .serializers import ProfilSerializer

# Create your views here.

class ProfilListView(generics.ListAPIView):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer

class  ProfilDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer