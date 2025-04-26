from django.db import models
from django.utils import timezone
from uuid import uuid4
import os
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError

TIPOS_NOTICIAS = (
    ('General', 'General'),
    ('Politica', 'Política'),
    ('Economia', 'Economía'),
    ('Comunicado Oficial', 'Comunicado Oficial'),
    ('Deportes', 'Deportes'),
    ('Cultura', 'Cultura'),
    ('Tecnologia', 'Tecnología'),
)

TIPO_ARCHIVO_CHOICES = (
        ('imagen', 'Imagen'),
        ('video', 'Video'),
        ('documento', 'Documento'),
        ('otro', 'Otro'),
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
        for archivo in self.archivos.all():
            archivo.delete() 
        super().delete(*args, **kwargs)

    
    def formatted_fecha(self):
        return self.fecha.strftime('%d %b %Y')

class ArchivosNoticias(models.Model):
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE, related_name="archivos")

    def archivo_ruta(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join(f'noticias/{instance.noticia.fecha.year}/{instance.noticia.fecha.month}/{instance.noticia.fecha.day}/{instance.noticia.id}/', filename)
    
    archivo_url = models.URLField("Enlace directo al archivo", max_length=500, blank=True, null=True,
                                   help_text="Pega aquí la URL si el archivo es muy grande o ya está en S3.")
    archivo = models.FileField(upload_to=archivo_ruta, blank=True, null=True)
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
        verbose_name_plural = "archivos de la noticia"

    def __str__(self):
        return self.noticia.titulo