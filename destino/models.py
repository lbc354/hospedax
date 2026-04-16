from django.db import models


class Destino(models.Model):
    class Meta:
        db_table = "destino"

    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
