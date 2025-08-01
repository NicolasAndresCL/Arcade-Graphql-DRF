# usuarios/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Usuario

class UsuarioType(DjangoObjectType):
    class Meta:
        model = Usuario
        fields = ("id", "username", "email", "telefono", "direccion", "first_name", "last_name")

# 🔍 Queries
class Query(graphene.ObjectType):
    all_usuarios = graphene.List(UsuarioType)
    usuario_by_id = graphene.Field(UsuarioType, id=graphene.Int(required=True))

    def resolve_all_usuarios(root, info):
        return Usuario.objects.all()

    def resolve_usuario_by_id(root, info, id):
        return Usuario.objects.get(id=id)

# 🧾 Mutaciones
class CreateUsuario(graphene.Mutation):
    usuario = graphene.Field(UsuarioType)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String()
        telefono = graphene.String()
        direccion = graphene.String()

    def mutate(self, info, username, email=None, telefono=None, direccion=None):
        user = Usuario(username=username, email=email, telefono=telefono, direccion=direccion)
        user.set_password("default123")  # Puedes modificar esto
        user.save()
        return CreateUsuario(usuario=user)

class UpdateUsuario(graphene.Mutation):
    usuario = graphene.Field(UsuarioType)

    class Arguments:
        id = graphene.ID(required=True)
        username = graphene.String()
        telefono = graphene.String()
        direccion = graphene.String()

    def mutate(self, info, id, **kwargs):
        user = Usuario.objects.get(pk=id)
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return UpdateUsuario(usuario=user)

class DeleteUsuario(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        user = Usuario.objects.get(pk=id)
        user.delete()
        return DeleteUsuario(ok=True)

# 📦 Registro de mutaciones
class Mutation(graphene.ObjectType):
    create_usuario = CreateUsuario.Field()
    update_usuario = UpdateUsuario.Field()
    delete_usuario = DeleteUsuario.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
