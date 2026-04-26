from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Destino
from .forms import DestinoForm


# LIST
def get_destinos(request, *args, **kwargs):
    destinos = Destino.objects.all()

    if kwargs.get("meus_anuncios"):
        destinos = destinos.filter(created_by=request.user)

    if kwargs.get("search_term"):
        search_term = kwargs.get("search_term")
        destinos = destinos.filter(titulo__icontains=search_term)

    return destinos


def destino_list(request, meus_anuncios=False):
    search_action = reverse("destino_list")
    search_term = request.GET.get("s", "")

    destinos = get_destinos(
        request, meus_anuncios=meus_anuncios, search_term=search_term
    )

    return render(
        request,
        "destino/list.html",
        {
            "destinos": destinos,
            "search_action": search_action,
            "search_term": search_term,
            "show_actions": meus_anuncios == True,
        },
    )


# RETRIEVE
def destino_retrieve(request, id):
    destino = get_object_or_404(Destino, id=id)
    show_actions = "show" if destino.created_by == request.user else ""
    return render(
        request,
        "destino/details.html",
        {"destino": destino, "show_actions": show_actions},
    )


# CREATE
def destino_create(request):
    form = DestinoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        with transaction.atomic():
            destino = form.save(commit=False)
            destino.created_by = request.user
            destino.updated_by = request.user
            destino.save()
        return redirect("destino_list_meus_anuncios")

    return render(request, "destino/create.html", {"form": form})


# UPDATE
def destino_update(request, id):
    destino = get_object_or_404(Destino, id=id)
    form = DestinoForm(request.POST or None, request.FILES or None, instance=destino)

    if form.is_valid():
        with transaction.atomic():
            destino = form.save(commit=False)
            destino.updated_by = request.user
            destino.save()
        return redirect("destino_list_meus_anuncios")

    return render(request, "destino/update.html", {"form": form})


# DELETE
def destino_delete(request, id):
    destino = get_object_or_404(Destino, id=id)

    if request.method == "POST":
        with transaction.atomic():
            destino.delete()
        return redirect("destino_list")

    return render(request, "destino/confirm_delete.html", {"destino": destino})
