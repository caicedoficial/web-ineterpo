from django.contrib import admin
from .models import Institucional, ImagenesInstitucional, Eventos, ImagenesEventos, Implementaciones, ImagenesImplementaciones

class BaseImagenAdmin(admin.TabularInline):
    extra = 1

class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo', 'fecha')
    ordering = ['-fecha']

class ImagenesInstitucionalAdmin(BaseImagenAdmin):
    model = ImagenesInstitucional

class InstitucionalAdmin(BaseModelAdmin):
    inlines = [ImagenesInstitucionalAdmin]

class ImagenesEventosAdmin(BaseImagenAdmin):
    model = ImagenesEventos

class EventosAdmin(BaseModelAdmin):
    inlines = [ImagenesEventosAdmin]

class ImagenesImplementacionesAdmin(BaseImagenAdmin):
    model = ImagenesImplementaciones

class ImplementacionesAdmin(BaseModelAdmin):
    inlines = [ImagenesImplementacionesAdmin]

admin.site.register(Institucional, InstitucionalAdmin)
admin.site.register(Eventos, EventosAdmin)
admin.site.register(Implementaciones, ImplementacionesAdmin)

admin.site.site_title = "Panel de administración"
admin.site.site_header = "INETERPO ADMIN"
admin.site.index_title = "Bienvenido al panel de administración del INETERPO"