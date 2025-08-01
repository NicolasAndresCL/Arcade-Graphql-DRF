from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from drf_spectacular.utils import extend_schema_view, extend_schema
from .models import ItemInventario
from .serializers import ItemInventarioSerializer
from drf_spectacular.utils import OpenApiExample

@extend_schema_view(
    post=extend_schema(
        operation_id="crear_item_inventario",
        summary="Crear ítem de inventario",
        description="Registra un nuevo ítem en el sistema de inventario arcade.",
        request=ItemInventarioSerializer,
        responses={201: ItemInventarioSerializer},
        tags=["Inventario"]
    )
)
class ItemCreateView(mixins.CreateModelMixin, GenericAPIView):
    queryset = ItemInventario.objects.all()
    serializer_class = ItemInventarioSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

item_example = OpenApiExample(
    name="Ejemplo de ítem arcade",
    value={
        "nombre": "Power-Up Turbo",
        "tipo": "powerup",
        "rareza": 4,
        "efecto": "Duplica la velocidad durante 10 segundos",
        "cantidad_disponible": 15,
        "imagen_url": "https://miapi.com/media/items/turbo.png",
        "tiempo_duracion": 10,
        "nivel_minimo": 2,
        "activo_en_juego": True
    },
    request_only=True,
    response_only=False
)


@extend_schema_view(
    get=extend_schema(
        operation_id="listar_items_inventario",
        summary="Listar ítems de inventario",
        description="Devuelve todos los ítems registrados en el sistema.",
        responses={200: ItemInventarioSerializer(many=True)},
        tags=["Inventario"]
    )
)
class ItemListView(mixins.ListModelMixin, GenericAPIView):
    queryset = ItemInventario.objects.all()
    serializer_class = ItemInventarioSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

@extend_schema_view(
    get=extend_schema(
        operation_id="detalle_item_inventario",
        summary="Detalle de ítem",
        description="Obtiene la información de un ítem por ID.",
        responses={200: ItemInventarioSerializer},
        tags=["Inventario"]
    )
)
class ItemDetailView(mixins.RetrieveModelMixin, GenericAPIView):
    queryset = ItemInventario.objects.all()
    serializer_class = ItemInventarioSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

@extend_schema_view(
    put=extend_schema(
        operation_id="actualizar_item_inventario",
        summary="Actualización total de ítem",
        description="Reemplaza completamente los datos del ítem de inventario.",
        request=ItemInventarioSerializer,
        responses={200: ItemInventarioSerializer},
        tags=["Inventario"]
    ),
    patch=extend_schema(
        operation_id="actualizar_item_inventario_parcial",
        summary="Actualización parcial de ítem",
        description="Modifica parcialmente los datos del ítem.",
        request=ItemInventarioSerializer,
        responses={200: ItemInventarioSerializer},
        tags=["Inventario"]
    )
)
class ItemUpdateView(mixins.UpdateModelMixin, GenericAPIView):
    queryset = ItemInventario.objects.all()
    serializer_class = ItemInventarioSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

@extend_schema_view(
    delete=extend_schema(
        operation_id="eliminar_item_inventario",
        summary="Eliminar ítem",
        description="Elimina un ítem específico del inventario arcade.",
        responses={204: None},
        tags=["Inventario"]
    )
)
class ItemDeleteView(mixins.DestroyModelMixin, GenericAPIView):
    queryset = ItemInventario.objects.all()
    serializer_class = ItemInventarioSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
