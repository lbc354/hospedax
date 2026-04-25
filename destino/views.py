from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Destino
from .forms import DestinoForm


# LIST
def destino_list(request):
    search_action = reverse("destino_list")
    search_term = request.GET.get("s")

    if search_term:
        destinos = Destino.objects.filter(titulo__icontains=search_term)
    else:
        search_term = ""
        destinos = Destino.objects.all()

    return render(
        request,
        "destino/list.html",
        {
            "destinos": destinos,
            "search_action": search_action,
            "search_term": search_term,
        },
    )


def destino_list_meus_anuncios(request):
    search_action = reverse("destino_list_meus_anuncios")
    search_term = request.GET.get("s")

    meus_destinos = Destino.objects.filter(created_by=request.user)

    if search_term:
        meus_destinos = meus_destinos.filter(titulo__icontains=search_term)
    else:
        search_term = ""

    return render(
        request,
        "destino/list.html",
        {
            "destinos": meus_destinos,
            "search_action": search_action,
            "search_term": search_term,
            "show_actions": "show",
        },
    )


# RETRIEVE
def destino_retrieve(request, id):
    destino = get_object_or_404(Destino, id=id)
    if destino and destino.created_by == request.user:
        show_actions = "show"
    return render(
        request,
        "destino/details.html",
        {"destino": destino, "show_actions": show_actions},
    )


# CREATE
def destino_create(request):
    form = DestinoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        destino = form.save(commit=False)
        destino.created_by = request.user
        destino.updated_by = request.user
        destino.save()
        return redirect("destino_list_meus_anuncios")

    return render(request, "destino/form.html", {"form": form})


# UPDATE
def destino_update(request, id):
    destino = get_object_or_404(Destino, id=id)
    form = DestinoForm(request.POST or None, request.FILES or None, instance=destino)

    if form.is_valid():
        destino = form.save(commit=False)
        destino.updated_by = request.user
        destino.save()
        return redirect("destino_list")

    return render(request, "destino/form.html", {"form": form})


# DELETE
def destino_delete(request, id):
    destino = get_object_or_404(Destino, id=id)

    if request.method == "POST":
        destino.delete()
        return redirect("destino_list")

    return render(request, "destino/confirm_delete.html", {"destino": destino})
