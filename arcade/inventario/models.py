from django.db import models

class ItemInventario(models.Model):
    TIPOS = [
        ("powerup", "Power-Up"),
        ("arma", "Arma"),
        ("moneda", "Moneda"),
        ("vida", "Vida Extra"),
        ("otro", "Otro"),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS, default="otro")
    rareza = models.IntegerField(default=1)  # 1=común, 5=legendario
    efecto = models.TextField(blank=True, null=True)
    cantidad_disponible = models.IntegerField(default=0)
    activo_en_juego = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} [{self.get_tipo_display()}]"
