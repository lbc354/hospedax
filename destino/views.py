from django.shortcuts import render, get_object_or_404, redirect
from .models import Destino
from .forms import DestinoForm


# LIST
def destino_list(request):
    search_term = request.GET.get("s")

    if search_term:
        destinos = Destino.objects.filter(titulo__icontains=search_term)
    else:
        destinos = Destino.objects.filter(created_by=request.user)

    return render(request, "destino/list.html", {"destinos": destinos})


# RETRIEVE
def destino_retrieve(request, id):
    destino = get_object_or_404(Destino, id=id)
    return render(request, "destino/details.html", {"destino": destino})


# CREATE
def destino_create(request):
    form = DestinoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        destino = form.save(commit=False)
        destino.created_by = request.user
        destino.updated_by = request.user
        destino.save()
        return redirect("destino_list")

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
