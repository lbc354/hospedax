from django.shortcuts import render, get_object_or_404, redirect
from .models import Destino
from .forms import DestinoForm


# LIST
def home(request):
    destinos = Destino.objects.all()
    return render(request, "destino/home.html", {"destinos": destinos})


# RETRIEVE
def destino_retrieve(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    return render(request, "destino/details.html", {"destino": destino})


# CREATE
def destino_create(request):
    form = DestinoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("destino_list")

    return render(request, "destino/form.html", {"form": form})


# UPDATE
def destino_update(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    form = DestinoForm(request.POST or None, instance=destino)

    if form.is_valid():
        form.save()
        return redirect("destino_list")

    return render(request, "destino/form.html", {"form": form})


# DELETE
def destino_delete(request, pk):
    destino = get_object_or_404(Destino, pk=pk)

    if request.method == "POST":
        destino.delete()
        return redirect("destino_list")

    return render(request, "destino/confirm_delete.html", {"destino": destino})
