from django.db import models
from uuid import uuid4
import os
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError
from django.utils import timezone

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

JORNADAS = (
    ('Mañana', 'Mañana'),
    ('Tarde', 'Tarde'),
    ('Nocturna', 'Nocturna'),
    ('General', 'General'),
)

class BaseModel(models.Model):
    titulo = models.CharField("Titulo", max_length=100)
    descripcion = HTMLField()
    fecha = models.DateTimeField(auto_now_add=timezone.now)
    jornada = models.CharField("Jornada", max_length=20, choices=JORNADAS, default='General')

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

class Eventos(models.Model):
    titulo = models.CharField("Titulo", max_length=100)
    descripcion = HTMLField()
    fecha = models.DateTimeField(auto_now_add=timezone.now)
    tipo = models.CharField("Tipo de Evento", max_length=20, choices=TIPO_EVENTO)
    jornada = models.CharField("Jornada", max_length=20, choices=JORNADAS, default='General')

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

    archivo = models.FileField(upload_to=archivo_ruta, blank=True, null=True)
    archivo_url = models.URLField("Enlace directo al archivo", max_length=500, blank=True, null=True,
                                   help_text="Pega aquí la URL si el archivo es muy grande o ya está en S3.")
    tipo_archivo = models.CharField(max_length=20, choices=TIPO_ARCHIVO_CHOICES)

    def delete(self, *args, **kwargs):
        if self.archivo:
            self.archivo.delete(save=False)
        super().delete(*args, **kwargs)

    def clean(self):
        # Evitar que se llenen ambos campos
        if self.archivo and self.archivo_url:
            raise ValidationError("No puedes subir un archivo y también ingresar una URL. Usa solo uno.")
        # Evitar que ambos estén vacíos
        if not self.archivo and not self.archivo_url:
            raise ValidationError("Debes subir un archivo o ingresar una URL.")

    def es_imagen(self):
        nombre = self.archivo.name if self.archivo else self.archivo_url or ""
        return nombre.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))

    def es_video(self):
        nombre = self.archivo.name if self.archivo else self.archivo_url or ""
        return nombre.lower().endswith(('.mp4', '.webm', '.ogg'))

    def es_documento(self):
        nombre = self.archivo.name if self.archivo else self.archivo_url or ""
        return nombre.lower().endswith(('.pdf', '.doc', '.docx', '.txt'))

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

    archivo = models.FileField(upload_to=archivo_ruta, blank=True, null=True)
    archivo_url = models.URLField("Enlace directo al archivo", max_length=500, blank=True, null=True,
                                   help_text="Pega aquí la URL si el archivo es muy grande o ya está en S3.")
    tipo_archivo = models.CharField(max_length=20, choices=TIPO_ARCHIVO_CHOICES)

    def delete(self, *args, **kwargs):
        if self.archivo:
            self.archivo.delete(save=False)
        super().delete(*args, **kwargs)

    def clean(self):
        # Evitar que se llenen ambos campos
        if self.archivo and self.archivo_url:
            raise ValidationError("No puedes subir un archivo y también ingresar una URL. Usa solo uno.")
        # Evitar que ambos estén vacíos
        if not self.archivo and not self.archivo_url:
            raise ValidationError("Debes subir un archivo o ingresar una URL.")

    def es_imagen(self):
        nombre = self.archivo.name if self.archivo else self.archivo_url or ""
        return nombre.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))

    def es_video(self):
        nombre = self.archivo.name if self.archivo else self.archivo_url or ""
        return nombre.lower().endswith(('.mp4', '.webm', '.ogg'))

    def es_documento(self):
        nombre = self.archivo.name if self.archivo else self.archivo_url or ""
        return nombre.lower().endswith(('.pdf', '.doc', '.docx', '.txt'))

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

    archivo = models.FileField(upload_to=archivo_ruta, blank=True, null=True)
    archivo_url = models.URLField("Enlace directo al archivo", max_length=500, blank=True, null=True,
                                   help_text="Pega aquí la URL si el archivo es muy grande o ya está en S3.")
    tipo_archivo = models.CharField(max_length=20, choices=TIPO_ARCHIVO_CHOICES)

    def delete(self, *args, **kwargs):
        if self.archivo:
            self.archivo.delete(save=False)
        super().delete(*args, **kwargs)

    def clean(self):
        # Evitar que se llenen ambos campos
        if self.archivo and self.archivo_url:
            raise ValidationError("No puedes subir un archivo y también ingresar una URL. Usa solo uno.")
        # Evitar que ambos estén vacíos
        if not self.archivo and not self.archivo_url:
            raise ValidationError("Debes subir un archivo o ingresar una URL.")

    def es_imagen(self):
        nombre = self.archivo.name if self.archivo else self.archivo_url or ""
        return nombre.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))

    def es_video(self):
        nombre = self.archivo.name if self.archivo else self.archivo_url or ""
        return nombre.lower().endswith(('.mp4', '.webm', '.ogg'))

    def es_documento(self):
        nombre = self.archivo.name if self.archivo else self.archivo_url or ""
        return nombre.lower().endswith(('.pdf', '.doc', '.docx', '.txt'))

    class Meta:
        verbose_name = "archivo"
        verbose_name_plural = "archivos de implementaciones"

    def __str__(self):
        return self.implementacion.titulo