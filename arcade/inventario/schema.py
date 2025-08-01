import graphene
from graphene_django import DjangoObjectType
from .models import ItemInventario

class ItemInventarioType(DjangoObjectType):
    class Meta:
        model = ItemInventario
        fields = "__all__"

class Query(graphene.ObjectType):
    all_items = graphene.List(ItemInventarioType)
    item_por_id = graphene.Field(ItemInventarioType, id=graphene.Int(required=True))

    def resolve_all_items(root, info):
        return ItemInventario.objects.filter(activo_en_juego=True)

    def resolve_item_por_id(root, info, id):
        return ItemInventario.objects.get(pk=id)

class CreateItem(graphene.Mutation):
    item = graphene.Field(ItemInventarioType)

    class Arguments:
        nombre = graphene.String()
        tipo = graphene.String()
        rareza = graphene.Int()
        efecto = graphene.String()
        cantidad_disponible = graphene.Int()

    def mutate(self, info, nombre, tipo="otro", rareza=1, efecto="", cantidad_disponible=0):
        i = ItemInventario(nombre=nombre, tipo=tipo, rareza=rareza, efecto=efecto, cantidad_disponible=cantidad_disponible)
        i.save()
        return CreateItem(item=i)

class UpdateItem(graphene.Mutation):
    item = graphene.Field(ItemInventarioType)

    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String()
        tipo = graphene.String()
        rareza = graphene.Int()
        efecto = graphene.String()
        cantidad_disponible = graphene.Int()
        activo_en_juego = graphene.Boolean()

    def mutate(self, info, id, **kwargs):
        i = ItemInventario.objects.get(pk=id)
        for key, value in kwargs.items():
            setattr(i, key, value)
        i.save()
        return UpdateItem(item=i)

class DeleteItem(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        ItemInventario.objects.get(pk=id).delete()
        return DeleteItem(ok=True)

class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()
    update_item = UpdateItem.Field()
    delete_item = DeleteItem.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
