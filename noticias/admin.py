from django.contrib import admin
from .models import Noticias, ArchivosNoticias

class ArchivosNoticiasAdmin(admin.TabularInline):
    model = ArchivosNoticias
    extra = 1

class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'id')
    search_fields = ('titulo', 'fecha', 'id')
    ordering = ['-fecha']
    inlines = [ArchivosNoticiasAdmin]

admin.site.register(Noticias, NoticiasAdmin)
admin.site.site_title = "Panel de administración"
admin.site.site_header = "INETERPO ADMIN"
admin.site.index_title = "Bienvenido al panel de administración del INETERPO"