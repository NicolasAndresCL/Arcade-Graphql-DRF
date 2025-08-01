from rest_framework import serializers
from .models import ItemInventario

class ItemInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInventario
        fields = "__all__"
