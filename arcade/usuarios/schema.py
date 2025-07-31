import graphene
from graphene_django.types import DjangoObjectType
from usuarios.models import Usuario

# Define el tipo GraphQL basado en tu modelo
class UsuarioType(DjangoObjectType):
    class Meta:
        model = Usuario
        fields = ("id", "username", "email", "telefono", "direccion")

# Define las consultas disponibles
class Query(graphene.ObjectType):
    all_usuarios = graphene.List(UsuarioType)
    usuario_por_id = graphene.Field(UsuarioType, id=graphene.Int(required=True))

    def resolve_all_usuarios(root, info):
        return Usuario.objects.all()

    def resolve_usuario_por_id(root, info, id):
        try:
            return Usuario.objects.get(id=id)
        except Usuario.DoesNotExist:
            return None

# Esquema principal
schema = graphene.Schema(query=Query)
