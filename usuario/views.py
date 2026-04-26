from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Usuario
from .forms import LoginForm, UsuarioCreateForm, UsuarioUpdateForm


# LOGIN
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = LoginForm(request, data=request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("home")

    return render(request, "usuario/login.html", {"form": form})


# LOGOUT
def logout_view(request):
    if request.method == "POST" and request.user.is_authenticated:
        logout(request)
    return redirect("home")


# LIST
def get_users(request, *args, **kwargs):
    usuarios = Usuario.objects.all()

    if kwargs.get("is_active") is True:
        usuarios = usuarios.filter(is_active=True)

    if kwargs.get("is_active") is False:
        usuarios = usuarios.filter(is_active=False)

    return usuarios


@login_required
def usuario_list(request, is_active=True):
    if not request.user.is_staff:
        print("retornar erro exigindo permissão")
        return redirect("home")

    usuarios = get_users(request, is_active=is_active)
    return render(
        request, "usuario/list.html", {"usuarios": usuarios, "is_active": is_active}
    )


# RETRIEVE
@login_required
def usuario_retrieve(request, id=None):
    if id and not request.user.is_staff:
        return redirect("usuario_retrieve")

    user_id = id or request.user.id

    usuario = get_object_or_404(Usuario, id=user_id)
    return render(request, "usuario/retrieve.html", {"usuario": usuario})


# CREATE
def usuario_create(request):
    form = UsuarioCreateForm(request.POST or None)

    if form.is_valid():
        with transaction.atomic():
            user = form.save()
            login(request, user)
        return redirect("home")

    return render(request, "usuario/create.html", {"form": form})


# UPDATE
@login_required
def usuario_update(request, id=None):
    if id and not request.user.is_staff:
        return redirect("usuario_update")

    user_id = id or request.user.id
    usuario = get_object_or_404(Usuario, id=user_id)
    form = UsuarioUpdateForm(request.POST or None, instance=usuario)

    if form.is_valid():
        with transaction.atomic():
            form.save()
        if request.user.is_staff:
            return redirect("usuario_list")
        return redirect("usuario_retrieve")

    return render(request, "usuario/update.html", {"form": form})


# DELETE
@login_required
def usuario_delete(request, id):
    if not request.user.is_staff:
        print("retornar erro exigindo permissão")
        return redirect("home")

    usuario = get_object_or_404(Usuario, id=id)

    if request.method == "POST":
        with transaction.atomic():
            if request.user.id == id:
                usuario.delete()
                logout(request)
                return redirect("home")
            else:
                usuario.delete()
                return redirect("usuario_list")

    return render(request, "usuario/delete.html", {"usuario": usuario})
