from django.urls import path
from .views import (
    ItemCreateView,
    ItemListView,
    ItemDetailView,
    ItemUpdateView,
    ItemDeleteView,
)

urlpatterns = [
    path('items/', ItemListView.as_view(), name='listar-items'),
    path('items/create/', ItemCreateView.as_view(), name='crear-item'),
    path('items/<int:id>/', ItemDetailView.as_view(), name='detalle-item'),
    path('items/<int:id>/update/', ItemUpdateView.as_view(), name='actualizar-item'),
    path('items/<int:id>/delete/', ItemDeleteView.as_view(), name='eliminar-item'),
]
