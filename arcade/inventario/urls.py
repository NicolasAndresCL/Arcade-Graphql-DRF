from django.urls import path
from .views import ItemInventarioView

urlpatterns = [
    path("items/", ItemInventarioView.as_view(), name="items_arcade"),
]
