from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from general.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio, name="inicio"),
    path("noticias/", include("noticias.urls", namespace='noticias')),
    path("eventos/", eventos, name="eventos"),
    path("implementaciones/", implementaciones, name="implementaciones"),
    path("institucional/", institucional, name="institucional"),
    path("<str:modelo>/all", total_modelo, name="total_modelo"),
    path("<str:modelo>/<int:year>/<int:month>/<int:day>/<int:id>/", objeto_detalle, name="objeto_detalle"),
    path('tinymce/', include('tinymce.urls')),
]

# Solo servir archivos estáticos/media localmente en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)