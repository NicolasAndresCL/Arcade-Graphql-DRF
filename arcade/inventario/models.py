from django.db import models

class ItemInventario(models.Model):
    TIPOS = [
        ("powerup", "Power-Up"),
        ("arma", "Arma"),
        ("moneda", "Moneda"),
        ("vida", "Vida Extra"),
        ("consumible", "Consumible"),
        ("otro", "Otro"),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS, default="otro")
    rareza = models.IntegerField(default=1)  # 1=común, 5=legendario
    efecto = models.TextField(blank=True, null=True)
    cantidad_disponible = models.IntegerField(default=0)
    imagen_url = models.URLField(blank=True, null=True)  # Opcional para frontend
    tiempo_duracion = models.IntegerField(blank=True, null=True)  # Segundos (para power-ups temporales)
    nivel_minimo = models.IntegerField(default=1)  # Requiere cierto nivel del jugador
    activo_en_juego = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-rareza", "nombre"]
        verbose_name = "Ítem de Inventario"
        verbose_name_plural = "Ítems de Inventario"

    def es_legendario(self):
        return self.rareza >= 5

    def es_temporal(self):
        return self.tiempo_duracion is not None and self.tiempo_duracion > 0


    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"
