import graphene
from graphene_django.types import DjangoObjectType
from usuarios.models import Usuario

# Tipo GraphQL para el modelo Usuario
class UsuarioType(DjangoObjectType):
    class Meta:
        model = Usuario
        fields = ("id", "username", "email", "telefono", "direccion")

# Queries relacionadas a usuarios
class UsuarioQuery(graphene.ObjectType):
    all_usuarios = graphene.List(UsuarioType)
    usuario_por_id = graphene.Field(UsuarioType, id=graphene.Int(required=True))

    def resolve_all_usuarios(root, info):
        return Usuario.objects.all()

    def resolve_usuario_por_id(root, info, id):
        try:
            return Usuario.objects.get(id=id)
        except Usuario.DoesNotExist:
            return None

# Tu query original
class HelloQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hello from Arcade!")

    def resolve_hello(self, info):
        return "Hello from Arcade!"

# Query principal que hereda ambas
class Query(UsuarioQuery, HelloQuery, graphene.ObjectType):
    pass

# Esquema final
schema = graphene.Schema(query=Query)
