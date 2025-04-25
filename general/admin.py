from django.contrib import admin
from .models import Institucional, ArchivosInstitucional, Eventos, ArchivosEventos, Implementaciones, ArchivosImplementaciones

class BaseArchivoAdmin(admin.TabularInline):
    extra = 1
    fields = ('archivo', 'archivo_url','tipo_archivo')

class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo', 'fecha')
    ordering = ['-fecha']

class ArchivosInstitucionalAdmin(BaseArchivoAdmin):
    model = ArchivosInstitucional

class InstitucionalAdmin(BaseModelAdmin):
    inlines = [ArchivosInstitucionalAdmin]

class ArchivosEventosAdmin(BaseArchivoAdmin):
    model = ArchivosEventos

class EventosAdmin(BaseModelAdmin):
    inlines = [ArchivosEventosAdmin]

class ArchivosImplementacionesAdmin(BaseArchivoAdmin):
    model = ArchivosImplementaciones

class ImplementacionesAdmin(BaseModelAdmin):
    inlines = [ArchivosImplementacionesAdmin]

admin.site.register(Institucional, InstitucionalAdmin)
admin.site.register(Eventos, EventosAdmin)
admin.site.register(Implementaciones, ImplementacionesAdmin)

admin.site.site_title = "Panel de administración"
admin.site.site_header = "INETERPO ADMIN"
admin.site.index_title = "Bienvenido al panel de administración del INETERPO"