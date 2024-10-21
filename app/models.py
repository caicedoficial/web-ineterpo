from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core.exceptions import ValidationError

def ruta_imagen(instance, filename):
    modelo = instance.content_type.model  # Obtener el modelo del tipo de contenido
    tipo = getattr(instance.apartado, 'tipo', 'general')
    
    # Obtener la fecha y manejar el caso en que no exista
    fecha_obj = getattr(instance.apartado, 'fecha', None)
    if fecha_obj and isinstance(fecha_obj, (timezone.datetime, timezone.date)):
        fecha = fecha_obj.strftime('%Y-%m-%d')
    else:
        fecha = 'sin-fecha'

    return f'{modelo}/{tipo}/{fecha}/{filename}'

TIPOS_EVENTOS = (
    ('Día del Idioma', 'Día del Idioma'),
    ('English Day', 'English Day'),
    ('Afrocolombianidad', 'Afrocolombianidad'),
    ('Día de la Secretaria', 'Día de la Secretaria'),
    ('Semana Deportiva', 'Semana Deportiva'),
    ('Día del Estudiante', 'Día del Estudiante'),
    ('Día del Maestro', 'Día del Maestro'),
)

class BaseModel(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título", blank=True, null=True)
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)
    fecha = models.DateField(default=timezone.now, verbose_name="Fecha de publicación", null=False, blank=False)
    imagenes_relacionadas = GenericRelation('Imagenes', related_query_name='apartado')

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.titulo} - {self.fecha.strftime('%d/%m/%Y')}"

    def delete(self, *args, **kwargs):
        # Eliminar las imágenes relacionadas
        self.eliminar_imagenes()
        super().delete(*args, **kwargs)

    def eliminar_imagenes(self):
        content_type = ContentType.objects.get_for_model(self)
        Imagenes.objects.filter(content_type=content_type, object_id=self.id).delete()

class Eventos(BaseModel):
    tipo = models.CharField(max_length=50, choices=TIPOS_EVENTOS)

    class Meta:
        verbose_name = "Eventos"
        verbose_name_plural = "Eventos"

    def clean(self):
        # Validación personalizada si es necesario
        if not self.tipo:
            raise ValidationError('El tipo de evento es obligatorio.')

class Implementaciones(BaseModel):
    class Meta:
        verbose_name = "Implementaciónes"
        verbose_name_plural = "Implementaciones"

class Comunidad(BaseModel):
    class Meta:
        verbose_name = "Comunidad"
        verbose_name_plural = "Comunidad" 

class Institucional(BaseModel):
    class Meta:
        verbose_name = "Institucional" 
        verbose_name_plural = "Institucional"

class Noticias(BaseModel):
    class Meta:
        verbose_name = "Noticias" 
        verbose_name_plural = "Noticias"
        ordering = ['-fecha']

class Imagenes(models.Model):
    imagen = models.ImageField(upload_to=ruta_imagen)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='imagenes_relacionadas')
    object_id = models.PositiveIntegerField()
    apartado = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Imagen de {self.apartado} - ID: {self.object_id}"