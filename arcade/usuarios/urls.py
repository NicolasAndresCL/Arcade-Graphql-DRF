from django.urls import path
from .views import (
    UsuarioCreateView, UsuarioListView, UsuarioDetailView,
    UsuarioUpdateView, UsuarioDeleteView
)

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/create/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuarios/<int:id>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('usuarios/<int:id>/update/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('usuarios/<int:id>/delete/', UsuarioDeleteView.as_view(), name='usuario-delete'),
]
