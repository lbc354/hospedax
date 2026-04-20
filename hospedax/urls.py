from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve

from django.shortcuts import render
from destino.models import Destino


def home(request):
    destinos = Destino.objects.all()
    return render(request, "home.html", {"destinos": destinos})


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

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += [
        re_path(
            r"^hospedax/static/(?P<path>.*)$",
            serve,
            {"document_root": settings.STATIC_ROOT},
        ),
    ]
