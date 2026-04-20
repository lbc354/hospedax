from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.usuario_list, name="usuario_list"),
    path("inativos/", views.usuario_inactive_list, name="usuario_inactive_list"),
    path("perfil/<int:pk>/", views.usuario_retrieve, name="usuario_retrieve_id"),
    path("perfil/", views.usuario_retrieve, name="usuario_retrieve"),
    path("criar/", views.usuario_create, name="usuario_create"),
    path("editar/<int:pk>/", views.usuario_update, name="usuario_update_id"),
    path("editar/", views.usuario_update, name="usuario_update"),
    path("deletar/<int:pk>/", views.usuario_delete, name="usuario_delete"),
]
