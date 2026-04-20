from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
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
def logout_view(request):
    if request.method == "POST" and request.user.is_authenticated:
        logout(request)
    return redirect("home")


# LIST
@login_required
def usuario_list(request):
    if not request.user.is_staff:
        print("retornar erro exigindo permissão")
        return redirect("home")

    usuarios = Usuario.objects.filter(is_active=True)
    return render(request, "usuario/list.html", {"usuarios": usuarios})


@login_required
def usuario_inactive_list(request):
    if not request.user.is_staff:
        print("retornar erro exigindo permissão")
        return redirect("home")

    usuarios = Usuario.objects.filter(is_active=False)
    return render(request, "usuario/inactive_list.html", {"usuarios": usuarios})


# RETRIEVE
@login_required
def usuario_retrieve(request, pk=None):
    if pk and not request.user.is_staff:
        return redirect("usuario_retrieve")

    user_pk = pk or request.user.pk

    usuario = get_object_or_404(Usuario, pk=user_pk)
    return render(request, "usuario/retrieve.html", {"usuario": usuario})


# CREATE
def usuario_create(request):
    form = UsuarioCreateForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    return render(request, "usuario/create.html", {"form": form})


# UPDATE
@login_required
def usuario_update(request, pk=None):
    if pk and not request.user.is_staff:
        return redirect("usuario_update")

    user_pk = pk or request.user.pk

    usuario = get_object_or_404(Usuario, pk=user_pk)
    form = UsuarioUpdateForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        if request.user.is_staff:
            return redirect("usuario_list")
        return redirect("usuario_retrieve")

    return render(request, "usuario/update.html", {"form": form})


# DELETE
@login_required
def usuario_delete(request, pk):
    if not request.user.is_staff:
        print("retornar erro exigindo permissão")
        return redirect("home")

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
