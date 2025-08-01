from rest_framework import generics
from .models import ItemInventario
from .serializers import ItemInventarioSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    summary="Items del juego arcade",
    description="Lista, crea y actualiza ítems arcade (power-ups, armas, monedas...)",
    responses={200: ItemInventarioSerializer},
    tags=["Inventario Arcade"]
)
class ItemInventarioView(generics.ListCreateAPIView):
    queryset = ItemInventario.objects.all()
    serializer_class = ItemInventarioSerializer
