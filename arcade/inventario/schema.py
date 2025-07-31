import graphene

class Query(graphene.ObjectType):
    inventario_hello = graphene.String(default_value="Hello from Inventario!")

schema = graphene.Schema(query=Query)