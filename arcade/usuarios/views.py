from django.shortcuts import render
from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer

# Create your views here.

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
