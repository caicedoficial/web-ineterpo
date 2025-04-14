from django.contrib import admin
from .models import Institucional, ArchivosInstitucional, Eventos, ArchivosEventos, Implementaciones, ArchivosImplementaciones

class BaseImagenAdmin(admin.TabularInline):
    extra = 1

class BaseArchivoAdmin(admin.TabularInline):
    extra = 1
    fields = ('archivo', 'tipo_archivo', 'titulo')

class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo', 'fecha')
    ordering = ['-fecha']

class ArchivosInstitucionalAdmin(BaseArchivoAdmin):
    model = ArchivosInstitucional

class InstitucionalAdmin(admin.ModelAdmin):
    inlines = [ArchivosInstitucionalAdmin]
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo', 'fecha')
    ordering = ['-fecha']

class ArchivosEventosAdmin(BaseImagenAdmin):
    model = ArchivosEventos

class EventosAdmin(BaseModelAdmin):
    inlines = [ArchivosEventosAdmin]

class ArchivosImplementacionesAdmin(BaseImagenAdmin):
    model = ArchivosImplementaciones

class ImplementacionesAdmin(BaseModelAdmin):
    inlines = [ArchivosImplementacionesAdmin]

admin.site.register(Institucional, InstitucionalAdmin)
admin.site.register(Eventos, EventosAdmin)
admin.site.register(Implementaciones, ImplementacionesAdmin)

admin.site.site_title = "Panel de administración"
admin.site.site_header = "INETERPO ADMIN"
admin.site.index_title = "Bienvenido al panel de administración del INETERPO"