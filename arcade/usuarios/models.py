from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    puntaje_inicial = models.PositiveIntegerField(default=0)
