from django.contrib import admin
from django.conf import settings
from django.urls import path, include, reverse

from django.shortcuts import render
from destino.models import Destino


def home(request):
    search_action = reverse("destino_list")
    destinos = Destino.objects.all().order_by("-created_at")[:5]
    return render(
        request, "home.html", {"destinos": destinos, "search_action": search_action}
    )


urlpatterns = [
    path(
        "hospedax/",
        include(
            [
                path("admin/", admin.site.urls),
                path("", home, name="home"),
                path("destino/", include("destino.urls")),
                path("usuario/", include("usuario.urls")),
            ]
        ),
    ),
]

# if settings.DEBUG:
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
