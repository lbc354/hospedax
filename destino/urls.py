from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>/", views.destino_retrieve, name="destino_retrieve"),
    path("novo/", views.destino_create, name="destino_create"),
    path("editar/<int:pk>/", views.destino_update, name="destino_update"),
    path("deletar/<int:pk>/", views.destino_delete, name="destino_delete"),
]
