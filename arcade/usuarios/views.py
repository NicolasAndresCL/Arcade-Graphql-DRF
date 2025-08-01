from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UsuarioSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema
from drf_spectacular.utils import OpenApiExample


@extend_schema_view(
    post=extend_schema(
        operation_id="crear_usuario",
        summary="Crear nuevo usuario",
        description="Endpoint para registrar un nuevo usuario en el sistema.",
        request=UsuarioSerializer,
        responses={201: UsuarioSerializer},
        tags=["Usuarios"]
    )
)
class UsuarioCreateView(mixins.CreateModelMixin, GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

usuario_example = OpenApiExample(
    name="Ejemplo de usuario",
    value={
        "username": "jugador_arcade",
        "email": "player@arcade.com",
        "avatar": "https://miapi.com/media/avatar1.png",
        "puntaje_inicial": 5000
    },
    request_only=True,
    response_only=False
)


@extend_schema_view(
    get=extend_schema(
        operation_id="listar_usuarios",
        summary="Listar usuarios",
        description="Devuelve un listado de todos los usuarios registrados.",
        responses={200: UsuarioSerializer(many=True)},
        tags=["Usuarios"]
    )
)
class UsuarioListView(mixins.ListModelMixin, GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

@extend_schema_view(
    get=extend_schema(
        operation_id="obtener_usuario",
        summary="Obtener detalle de usuario",
        description="Devuelve los datos de un usuario según su ID.",
        responses={200: UsuarioSerializer, 404: None},
        tags=["Usuarios"]
    )
)
class UsuarioDetailView(mixins.RetrieveModelMixin, GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'id'  # opcional si usas otro campo

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

@extend_schema_view(
    put=extend_schema(
        operation_id="actualizar_usuario",
        summary="Actualizar usuario",
        description="Actualiza completamente los datos del usuario por ID.",
        request=UsuarioSerializer,
        responses={200: UsuarioSerializer, 400: None},
        tags=["Usuarios"]
    ),
    patch=extend_schema(
        operation_id="actualizar_usuario_parcial",
        summary="Actualizar parcialmente usuario",
        description="Actualiza parcialmente los datos de un usuario por ID.",
        request=UsuarioSerializer,
        responses={200: UsuarioSerializer},
        tags=["Usuarios"]
    )
)
class UsuarioUpdateView(mixins.UpdateModelMixin, GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

@extend_schema_view(
    delete=extend_schema(
        operation_id="eliminar_usuario",
        summary="Eliminar usuario",
        description="Elimina al usuario identificado por ID.",
        responses={204: None, 404: None},
        tags=["Usuarios"]
    )
)
class UsuarioDeleteView(mixins.DestroyModelMixin, GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

