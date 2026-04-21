# https://docs.djangoproject.com/pt-br/3.2/ref/models/fields/

from django.db import models
from django.conf import settings
from PIL import Image
import os


class Destino(models.Model):
    class Meta:
        db_table = "destino"

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    imagem = models.ImageField(upload_to="destinos/imagens/%Y/%m/%d/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="destinos_criados",
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="destinos_atualizados",
    )

    def save(self, *args, **kwargs):
        saved = super().save(*args, **kwargs)

        if self.imagem:
            try:
                self.resize_image(self.imagem, 800)
            except FileNotFoundError:
                ...

        return saved

    @staticmethod
    def resize_image(image, new_width=800):
        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        image_pillow = Image.open(image_full_path)
        original_width, original_height = image_pillow.size

        if original_width <= new_width:
            image_pillow.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)
        new_image.save(
            image_full_path,
            optimize=True,
            quality=50,
        )

    def __str__(self):
        return self.titulo
