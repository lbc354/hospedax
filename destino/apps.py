from django.apps import AppConfig


class DestinoConfig(AppConfig):
    name = "destino"

    def ready(self):
        import destino.signals

        return super().ready()
