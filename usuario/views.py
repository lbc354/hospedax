from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
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
@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")


# LIST
@login_required
def usuario_list(request):
    if not request.user.is_staff:
        print("retornar erro exigindo permissão")
        return redirect("home")  # aqui será render

    usuarios = Usuario.objects.all()
    return render(request, "usuario/list.html", {"usuarios": usuarios})


# RETRIEVE
@login_required
def usuario_retrieve(request, pk):
    user_pk = pk

    if request.user.pk != pk and not request.user.is_staff:
        user_pk = request.user.pk

    usuario = get_object_or_404(Usuario, pk=user_pk)
    return render(request, "usuario/retrieve.html", {"usuario": usuario})


# CREATE
def usuario_create(request):
    form = UsuarioCreateForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)  # já loga após cadastro
        return redirect("home")

    return render(request, "usuario/create.html", {"form": form})


# UPDATE
@login_required
def usuario_update(request, pk):
    user_pk = pk

    if request.user.pk != pk and not request.user.is_staff:
        user_pk = request.user.pk

    usuario = get_object_or_404(Usuario, pk=user_pk)
    form = UsuarioUpdateForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        if request.user.is_staff:
            return redirect("usuario_list")
        return redirect("usuario_retrieve", user_pk)

    return render(request, "usuario/update.html", {"form": form})


# DELETE
@login_required
def usuario_delete(request, pk):
    if not request.user.is_staff:
        print("retornar erro exigindo permissão")
        return redirect("home")  # aqui será render

    usuario = get_object_or_404(Usuario, pk=pk)

    if request.method == "POST":
        if request.user.pk == pk:
            logout(request)
            usuario.delete()
            return redirect("home")
        else:
            usuario.delete()
            return redirect("usuario_list")

    return render(request, "usuario/delete.html", {"usuario": usuario})
