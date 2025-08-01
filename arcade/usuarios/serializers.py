from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar', 'puntaje_inicial']
        read_only_fields = ['id']  
