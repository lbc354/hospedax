from django.urls import path
from . import views

urlpatterns = [
    path("", views.destino_list, name="destino_list"),
    path("<int:pk>/", views.destino_retrieve, name="destino_retrieve"),
    path("criar/", views.destino_create, name="destino_create"),
    path("editar/<int:pk>/", views.destino_update, name="destino_update"),
    path("deletar/<int:pk>/", views.destino_delete, name="destino_delete"),
]
