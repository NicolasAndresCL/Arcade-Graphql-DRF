from django.urls import path
from .views import (
    UsuarioCreateView, UsuarioListView, UsuarioDetailView,
    UsuarioUpdateView, UsuarioDeleteView, CustomTokenObtainPairView, CustomTokenRefreshView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/create/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuarios/<int:id>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('usuarios/<int:id>/update/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('usuarios/<int:id>/delete/', UsuarioDeleteView.as_view(), name='usuario-delete'),

    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'), 

]
