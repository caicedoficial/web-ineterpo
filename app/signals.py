import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Imagenes

@receiver(post_delete, sender=Imagenes)
def eliminar_imagen(sender, instance, **kwargs):
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)

