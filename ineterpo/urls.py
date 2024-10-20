"""
URL configuration for ineterpo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='principal'),
    path('Eventos/', views.eventos, name='eventos'),
    path('<str:modelo>/', views.titulo_imagen, name='titulo-imagen'),
    path('<str:modelo>/<int:id>+<str:titulo>/', views.detalle_objeto, name='detalle-objeto'),
    path('<str:modelo>/<str:tipo>/', views.titulo_imagen_tipo, name='titulo-imagen-tipo'),
    path('<str:modelo>/<str:tipo>/<int:id>/', views.detalle_objeto_tipo, name='detalle-objeto-tipo'),
    path('ineterpo.ico', RedirectView.as_view(url='/static/icons/ineterpo.ico', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


