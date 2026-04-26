from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.usuario_list, {"is_active": True}, name="usuario_list"),
    path(
        "inativos/",
        views.usuario_list,
        {"is_active": False},
        name="usuario_inactive_list",
    ),
    path("perfil/<int:id>/", views.usuario_retrieve, name="usuario_retrieve_id"),
    path("perfil/", views.usuario_retrieve, name="usuario_retrieve"),
    path("criar/", views.usuario_create, name="usuario_create"),
    path("editar/<int:id>/", views.usuario_update, name="usuario_update_id"),
    path("editar/", views.usuario_update, name="usuario_update"),
    path("deletar/<int:id>/", views.usuario_delete, name="usuario_delete"),
]
