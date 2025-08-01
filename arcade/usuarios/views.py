from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    summary="Listado y creación de usuarios",
    description="Permite obtener el listado de todos los usuarios registrados y crear nuevos usuarios con datos personalizados.",
    responses={200: UsuarioSerializer},
    tags=["Usuarios"]
)

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
