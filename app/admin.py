from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Eventos, Implementaciones, Comunidad, Imagenes, Noticias, Institucional

class ImagenAdmin(GenericTabularInline):
    model = Imagenes
    extra = 1

class BaseAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')  # Cambiado para mostrar 'titulo' y 'fecha'
    list_display_links = ('titulo',)  # Cambiado para que 'titulo' sea el enlace
    list_filter = ('fecha',)  # Filtrar por fecha
    search_fields = ('titulo',)  # Buscar por título
    fields = ('titulo', 'descripcion', 'fecha')  # Campos a mostrar en el formulario
    ordering = ('-fecha',)  # Ordenar por fecha descendente
    inlines = [ImagenAdmin]

class EventosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    list_display_links = ('titulo',)
    list_filter = ('fecha',)
    search_fields = ('titulo',)
    fields = ('titulo', 'tipo', 'descripcion', 'fecha')
    ordering = ('-fecha',)
    inlines = [ImagenAdmin]

class ComunidadAdmin(BaseAdmin):
    pass

class ImplementacionesAdmin(BaseAdmin):
    pass

class NoticiasAdmin(BaseAdmin):
    pass

class InstitucionalAdmin(BaseAdmin):
    pass

admin.site.register(Eventos, EventosAdmin)
admin.site.register(Comunidad, ComunidadAdmin)
admin.site.register(Implementaciones, ImplementacionesAdmin)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Institucional, InstitucionalAdmin)

