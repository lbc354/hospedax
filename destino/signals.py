from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Destino
import os


def delete_imagem(instance):
    try:
        os.remove(instance.imagem.path)
    except (ValueError, FileNotFoundError):
        ...


@receiver(pre_delete, sender=Destino)
def destino_imagem_delete(sender, instance, *args, **kwargs):
    # old_instance = Destino.objects.filter(id=instance.id).first()
    # if old_instance:
    #     delete_imagem(old_instance)

    # No pre_delete, a instância já é a do banco — só deletar diretamente
    delete_imagem(instance)


@receiver(pre_save, sender=Destino)
def destino_imagem_update(sender, instance, *args, **kwargs):
    old_instance = Destino.objects.filter(id=instance.id).first()

    if not old_instance:
        return

    is_new_imagem = old_instance.imagem != instance.imagem

    if is_new_imagem:
        delete_imagem(old_instance)
