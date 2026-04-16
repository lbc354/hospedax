from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.usuario_list, name="usuario_list"),
    path("<int:pk>/", views.usuario_retrieve, name="usuario_retrieve"),
    path("novo/", views.usuario_create, name="usuario_create"),
    path("editar/<int:pk>/", views.usuario_update, name="usuario_update"),
    path("deletar/<int:pk>/", views.usuario_delete, name="usuario_delete"),
]
