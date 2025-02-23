from django.db import models
from django.urls import reverse
from django.utils import timezone
from uuid import uuid4
import os
from tinymce.models import HTMLField

TIPOS_NOTICIAS = (
    ('General', 'General'),
    ('Politica', 'Política'),
    ('Economia', 'Economía'),
    ('Comunicado Oficial', 'Comunicado Oficial'),
    ('Deportes', 'Deportes'),
    ('Cultura', 'Cultura'),
    ('Tecnologia', 'Tecnología'),
)

class Noticias(models.Model):
    titulo = models.CharField("Titulo", max_length=100)
    descripcion = HTMLField()
    fecha = models.DateTimeField(auto_now_add=timezone.now)
    tipo = models.CharField("Tipo de Noticia", max_length=20, choices=TIPOS_NOTICIAS, default='general')
    
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.titulo

    def delete(self, *args, **kwargs):
        for imagen in self.imagenes.all():
            imagen.imagen.delete()
        super().delete(*args, **kwargs)
    
    def formatted_fecha(self):
        return self.fecha.strftime('%d %b %Y')

class ImagenesNoticias(models.Model):
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE, related_name="imagenes")

    def imagen_ruta(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join(f'noticias/{instance.noticia.fecha.year}/{instance.noticia.fecha.month}/{instance.noticia.fecha.day}/{instance.noticia.id}/', filename)

    imagen = models.ImageField(upload_to=imagen_ruta)

    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imagenes de la noticia"

    def __str__(self):
        return self.noticia.titulo