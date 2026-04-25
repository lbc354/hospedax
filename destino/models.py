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

    # folder: /media/destinos/imagens/%Y/%m/%d/<image_name>.<image_extension>
    # url: /hospedax/media/destinos/imagens/%Y/%m/%d/<image_name>.<image_extension>
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
    def resize_image(image, target_width=800, target_ratio=(16, 9)):
        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        img = Image.open(image_full_path)

        original_width, original_height = img.size
        target_height = int(target_width * target_ratio[1] / target_ratio[0])

        # calcula proporção atual
        current_ratio = original_width / original_height
        desired_ratio = target_ratio[0] / target_ratio[1]

        if current_ratio > desired_ratio:
            # imagem mais larga → corta lateral
            new_width = int(original_height * desired_ratio)
            offset = (original_width - new_width) // 2
            crop_box = (offset, 0, offset + new_width, original_height)
        else:
            # imagem mais alta → corta topo/base
            new_height = int(original_width / desired_ratio)
            offset = (original_height - new_height) // 2
            crop_box = (0, offset, original_width, offset + new_height)

        img = img.crop(crop_box)
        img = img.resize((target_width, target_height), Image.LANCZOS)

        img.save(image_full_path, optimize=True, quality=80)
        img.close()

    def __str__(self):
        return self.titulo
