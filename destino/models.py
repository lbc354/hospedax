from django.db import models
from usuario.models import Usuario


class Destino(models.Model):
    class Meta:
        db_table = "destino"

    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.SlugField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        Usuario, on_delete=models.SET_NULL, null=True, related_name="destinos_criados"
    )
    updated_by = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        related_name="destinos_atualizados",
    )

    def __str__(self):
        return self.titulo
