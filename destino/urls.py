from django.urls import path
from . import views

urlpatterns = [
    path("", views.destino_list, name="destino_list"),
    path(
        "meus-anuncios/",
        views.destino_list,
        {"meus_anuncios": True},
        name="destino_list_meus_anuncios",
    ),
    path("<int:id>/", views.destino_retrieve, name="destino_retrieve"),
    path("criar/", views.destino_create, name="destino_create"),
    path("editar/<int:id>/", views.destino_update, name="destino_update"),
    path("deletar/<int:id>/", views.destino_delete, name="destino_delete"),
]
