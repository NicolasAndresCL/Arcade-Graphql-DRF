
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graphql_playground.views import GraphQLPlaygroundView
from .views import custom_swagger_ui_view
from django.conf.urls.static import static
from django.conf import settings




def home(request):
    return HttpResponse("¡Bienvenido a la API de Django + GraphQL!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    path('api/', include('usuarios.urls'), name='usuarios'),
    path('api/', include('inventario.urls'), name='inventario'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/schema/swagger-ui/', custom_swagger_ui_view, name='swagger-ui'),

    path('graphql/', GraphQLView.as_view(graphiql=True)), 
    path('playground/', GraphQLPlaygroundView.as_view(endpoint="/graphql/")),



]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)