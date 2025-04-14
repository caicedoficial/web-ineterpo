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

TIPO_ARCHIVO_CHOICES = (
        ('imagen', 'Imagen'),
        ('video', 'Video'),
        ('documento', 'Documento'),
        ('otro', 'Otro'),
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

class ArchivosInstitucional(models.Model):
    institucional = models.ForeignKey(Institucional, on_delete=models.CASCADE, related_name="archivos")

    def archivo_ruta(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join(f'institucional/{instance.institucional.fecha.year}/{instance.institucional.fecha.month}/{instance.institucional.fecha.day}/{instance.institucional.id}', filename)
    
    def es_imagen(self):
        return self.archivo.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    
    def es_video(self):
        return self.archivo.name.lower().endswith(('.mp4', '.webm', '.ogg'))
    
    def es_documento(self):
        return self.archivo.name.lower().endswith(('.pdf', '.doc', '.docx', '.txt'))

    archivo = models.FileField(upload_to=archivo_ruta)
    tipo_archivo = models.CharField(max_length=20, choices=TIPO_ARCHIVO_CHOICES)

    class Meta:
        verbose_name = "archivo"
        verbose_name_plural = "archivos institucionales"

    def __str__(self):
        return self.institucional.titulo

class ArchivosEventos(models.Model):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE, related_name="archivos")

    def archivo_ruta(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join(f'eventos/{instance.evento.fecha.year}/{instance.evento.fecha.month}/{instance.evento.fecha.day}/{instance.evento.id}', filename)
    
    def es_imagen(self):
        return self.archivo.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    
    def es_video(self):
        return self.archivo.name.lower().endswith(('.mp4', '.webm', '.ogg'))
    
    def es_documento(self):
        return self.archivo.name.lower().endswith(('.pdf', '.doc', '.docx', '.txt'))

    archivo = models.FileField(upload_to=archivo_ruta)
    tipo_archivo = models.CharField(max_length=20, choices=TIPO_ARCHIVO_CHOICES)

    class Meta:
        verbose_name = "archivo"
        verbose_name_plural = "archivos de eventos"

    def __str__(self):
        return self.evento.titulo

class ArchivosImplementaciones(models.Model):
    implementacion = models.ForeignKey(Implementaciones, on_delete=models.CASCADE, related_name="archivos")

    def archivo_ruta(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join(f'implementaciones/{instance.implementacion.fecha.year}/{instance.implementacion.fecha.month}/{instance.implementacion.fecha.day}/{instance.implementacion.id}', filename)
    
    def es_imagen(self):
        return self.archivo.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    
    def es_video(self):
        return self.archivo.name.lower().endswith(('.mp4', '.webm', '.ogg'))
    
    def es_documento(self):
        return self.archivo.name.lower().endswith(('.pdf', '.doc', '.docx', '.txt'))

    archivo = models.FileField(upload_to=archivo_ruta)
    tipo_archivo = models.CharField(max_length=20, choices=TIPO_ARCHIVO_CHOICES)

    class Meta:
        verbose_name = "archivo"
        verbose_name_plural = "archivos de implementaciones"

    def __str__(self):
        return self.implementacion.titulo