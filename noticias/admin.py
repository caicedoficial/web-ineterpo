from django.contrib import admin
from .models import Noticias, ImagenesNoticias

class ImagenesNoticiasAdmin(admin.TabularInline):
    model = ImagenesNoticias
    extra = 1

class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'id')
    search_fields = ('titulo', 'fecha', 'id')
    ordering = ['-fecha']
    inlines = [ImagenesNoticiasAdmin]

admin.site.register(Noticias, NoticiasAdmin)
admin.site.site_title = "Panel de administración"
admin.site.site_header = "INETERPO ADMIN"
admin.site.index_title = "Bienvenido al panel de administración del INETERPO"