from django.db import models
from uuid import uuid4
import os
from tinymce.models import HTMLField

TIPO_EVENTO = (
    ('Dia del Idioma', 'Dia del Idioma'),
    ('Afrocolombianidad', 'Afrocolombianidad'),
    ('English Day', 'English Day'),
    ('Dia del Maestro', 'Dia del Maestro'),
    ('Dia del Estudiante', 'Dia del Estudiante'),
)

class BaseModel(models.Model):
    titulo = models.CharField("Titulo", max_length=100)
    descripcion = HTMLField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.titulo

    def formatted_fecha(self):
        return self.fecha.strftime('%d %b %Y')

    def delete(self, *args, **kwargs):
        for imagen in self.imagenes.all():
            imagen.imagen.delete()
        super().delete(*args, **kwargs)

class Institucional(BaseModel):
    class Meta:
        verbose_name = "Institucional"
        verbose_name_plural = "Institucional"

class Eventos(BaseModel):
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class Implementaciones(BaseModel):
    class Meta:
        verbose_name = "Implementación"
        verbose_name_plural = "Implementaciones"

class ImagenesInstitucional(models.Model):
    institucional = models.ForeignKey(Institucional, on_delete=models.CASCADE, related_name="imagenes")

    def imagen_ruta(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join(f'institucional/{instance.institucional.fecha.year}/{instance.institucional.fecha.month}/{instance.institucional.fecha.day}/{instance.institucional.id}', filename)

    imagen = models.ImageField(upload_to=imagen_ruta)

    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imagenes de institucional"

    def __str__(self):
        return self.institucional.titulo

class ImagenesEventos(models.Model):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE, related_name="imagenes")

    def imagen_ruta(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join(f'eventos/{instance.evento.fecha.year}/{instance.evento.fecha.month}/{instance.evento.fecha.day}/{instance.evento.id}', filename)

    imagen = models.ImageField(upload_to=imagen_ruta)

    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imagenes de eventos"

    def __str__(self):
        return self.evento.titulo

class ImagenesImplementaciones(models.Model):
    implementacion = models.ForeignKey(Implementaciones, on_delete=models.CASCADE, related_name="imagenes")

    def imagen_ruta(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join(f'implementaciones/{instance.implementacion.fecha.year}/{instance.implementacion.fecha.month}/{instance.implementacion.fecha.day}/{instance.implementacion.id}', filename)

    imagen = models.ImageField(upload_to=imagen_ruta)

    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imagenes de implementaciones"

    def __str__(self):
        return self.implementacion.titulo