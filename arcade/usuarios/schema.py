import graphene

class Query(graphene.ObjectType):
    usuarios_hello = graphene.String(default_value="Hello from Usuarios!")

schema = graphene.Schema(query=Query)