# 🎮 GraphQL Arcade API – Django + DRF + Graphene

Backend profesional para gestión de usuarios en videojuegos arcade. Integración de Django con GraphQL, DRF, documentación automática con Swagger (drf-spectacular) y control de versiones con Git. Proyecto modular, escalable y orientado a presentación técnica.

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
| Entorno local          | Virtualenv                       |

---

## 📦 Estructura del proyecto

```text
arcade/
├── arcade/             # Configuración global de Django
│   └── settings.py     # Integración DRF, GraphQL y Swagger
├── usuarios/           # App para gestión de usuarios
│   ├── models.py       # Modelo de usuario personalizado
│   ├── views.py        # Vista DRF decorada con @extend_schema
│   ├── schema.py       # Mutaciones y queries GraphQL
│   └── serializers.py  # Serializador REST para el modelo
```

## 🚀 Funcionalidades implementadas
✅ API REST documentada con Swagger vía drf-spectacular

✅ Endpoint DRF con título, descripción y tags personalizados (@extend_schema)

✅ Queries y mutaciones GraphQL funcionales y escalables (schema.py)

✅ Modelo de usuario desacoplado, listo para ampliar funcionalidades

✅ Configuración modular lista para deploy en producción

## 🗂️ Buenas prácticas aplicadas
Separación clara entre REST y GraphQL

Commit semánticos en inglés (git commit -m "Improve GraphQL schema...")

Documentación en línea para entrevistas técnicas

Nombres descriptivos y lógica desacoplada

Código limpio, comentado y extensible

## 📈 Próximos pasos sugeridos
🔐 Integrar autenticación (token o JWT en GraphQL)

📊 Añadir métricas de juego al modelo Usuario (puntaje, niveles completados)

📘 Ampliar el README con ejemplos visuales (Swagger + GraphQL Playground)

🕹️ Conectar API con frontend arcade (React, Pygame web o móvil)

## 👨‍💻 Autor
Nicolás Andrés Cano Leal Backend developer & Arcade game creator 📍 Chile | Documentación clara | Publicación multiplataforma 🎯 Portafolio: APIs REST/GraphQL + videojuegos arcade
