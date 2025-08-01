# 🎮 GraphQL Arcade API – Django + DRF + Graphene

Backend profesional para gestión de usuarios en videojuegos arcade. Integración de Django con GraphQL, DRF, documentación automática con Swagger (drf-spectacular) y control de versiones con Git. Proyecto modular, escalable y orientado a presentación técnica y entrevistas.

---

## 🧠 Tecnologías utilizadas

| Categoría              | Herramienta/Framework             |
|------------------------|-----------------------------------|
| Lenguaje               | Python 3.x                        |
| Framework principal    | Django 4.x                        |
| APIs REST              | Django REST Framework (DRF)      |
| APIs GraphQL           | Graphene-Django                  |
| Documentación REST     | drf-spectacular + Swagger UI     |
| ORM                    | Django ORM                       |
| Autenticación          | Token / Session (opcional)       |
| Control de versiones   | Git + GitHub                     |
| Entorno local          | Venv                       |

---

## 📦 Estructura del proyecto

```text
arcade/
├── arcade/               # Configuración global de Django
│   └── settings.py       # Integración DRF, GraphQL y Swagger
├── usuarios/             # App para gestión de usuarios
│   ├── models.py         # Modelo de usuario personalizado
│   ├── views.py          # Vista DRF con @extend_schema y examples
│   ├── schema.py         # Mutaciones y queries GraphQL
│   └── serializers.py    # Serializador REST para el modelo
├── inventario/           # App para ítems arcade y lógica de rareza
│   ├── models.py         # Modelo de ítem con rareza, efecto y visualización
│   ├── views.py          # Vista DRF con ejemplos visuales Swagger
│   ├── schema.py         # Mutaciones GraphQL para ítems
│   └── serializers.py    # Serializador REST para inventario

```

## 🚀 Funcionalidades implementadas
✅ API REST documentada con Swagger (drf-spectacular)

✅ Ejemplos visuales en Swagger para usuarios e ítems arcade (OpenApiExample)

✅ GraphQL funcional para queries y mutaciones personalizadas

✅ CRUD completo de usuarios e inventario desde DRF y GraphQL

✅ Modelo de inventario arcade con campos avanzados: rareza, efecto, visualización, nivel mínimo, estado en juego

✅ Configuración modular y extensible, lista para producción

## 🎯 Ejemplos visuales en Swagger UI
Swagger UI muestra payloads prellenados para facilitar pruebas y presentación profesional. Algunos ejemplos:

👤 Crear usuario

```
json
{
  "username": "jugador_arcade",
  "email": "player@arcade.com",
  "avatar": "https://miapi.com/media/avatar1.png",
  "puntaje_inicial": 5000
}
```

🎮 Crear ítem de inventario
```
json
{
  "nombre": "Power-Up Turbo",
  "tipo": "powerup",
  "rareza": 4,
  "efecto": "Duplica la velocidad durante 10 segundos",
  "cantidad_disponible": 15,
  "imagen_url": "https://miapi.com/media/items/turbo.png",
  "tiempo_duracion": 10,
  "nivel_minimo": 2,
  "activo_en_juego": true
}
```

## 🗂️ Buenas prácticas aplicadas

🔹 Separación clara entre REST y GraphQL 🔹 Documentación automática con ejemplos visuales y tags agrupados 🔹 Commits semánticos en inglés ("Add item examples for Swagger") 🔹 Nombres descriptivos, lógica desacoplada y presentación técnica 🔹 Modelo arcade pensado para escalabilidad y entrevistas

## 📈 Próximos pasos sugeridos
🔐 Integrar autenticación JWT en GraphQL 📊 Agregar métricas y logros a modelos de usuario 🧪 Automatizar tests unitarios (Pytest + factory_boy) 🕹️ Conectar API con frontend arcade (React, Pygame Web) 📘 Exportar documentación visual para portafolio online

## 👨‍💻 Autor
Nicolás Andrés Cano Leal Backend developer & Arcade game creator 📍 Chile | Documentación clara | Publicación multiplataforma 🎯 Portafolio: APIs REST/GraphQL + videojuegos arcade
🔗 GitHub: [github.com/nicolasandrescl] Portafolio: [nicolasandrescl.pythonanywhere.com]
