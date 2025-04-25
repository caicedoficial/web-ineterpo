from django.shortcuts import render, get_object_or_404
from django.apps import apps
from django.http import HttpResponseServerError
from .models import Institucional, Eventos, Implementaciones
from django.utils.timezone import localtime
from django.db.models import Q

def institucional(request):
    try:
        queryset = request.GET.get('search')
        institucional = Institucional.objects.all().order_by('-fecha')[:10]

        if queryset:
            institucional = Institucional.objects.filter(
                Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset) | Q(tipo__icontains=queryset)
            ).distinct().order_by('-fecha')

        
        for ins in institucional:
            ins.fecha = localtime(ins.fecha)

        return render(request, 'general.html', {'objetos': institucional, 'modelo': 'Institucional'})

    except Exception as e:
        return HttpResponseServerError("Error al obtener datos institucionales")

def eventos(request):
    try:
        queryset = request.GET.get('search')
        eventos = Eventos.objects.all().order_by('-fecha')[:10]

        if queryset:
            eventos = Eventos.objects.filter(
                Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset) | Q(tipo__icontains=queryset)
            ).distinct().order_by('-fecha')

        for evento in eventos:
            evento.fecha = localtime(evento.fecha)

        return render(request, 'general.html', {'objetos': eventos, 'modelo': 'Eventos'})
    except Exception as e:
        return HttpResponseServerError(f"Error al obtener datos de eventos: {e}")

def implementaciones(request):
    try:
        queryset = request.GET.get('search')
        implementaciones = Implementaciones.objects.all().order_by('-fecha')[:10]

        if queryset:
            implementaciones = Implementaciones.objects.filter(
                Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset)
            ).distinct().order_by('-fecha')

        for implementacion in implementaciones:
            implementacion.fecha = localtime(implementacion.fecha)

        return render(request, 'general.html', {'objetos': implementaciones, 'modelo': 'Implementaciones'})
    except Exception as e:
        return HttpResponseServerError("Error al obtener datos de implementaciones")

def total_modelo(request, modelo):
    try:
        queryset = request.GET.get('search')
        if queryset:
            ModelClass = apps.get_model('general', modelo)
            objetos = ModelClass.objects.filter(
                Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset) | Q(tipo__icontains=queryset) if modelo == 'Eventos' else None
            ).distinct().order_by('-fecha')
        else:
            ModelClass = apps.get_model('general', modelo)
            objetos = ModelClass.objects.all().order_by('-fecha')

        return render(request, 'general.html', {'objetos': objetos, 'check': True, 'modelo': modelo})
    except Exception as e:
        return HttpResponseServerError(f"Error al obtener datos del modelo {modelo}: {e}")
    
def objeto_detalle(request, year, month, day, id, modelo):
    ModelClass = apps.get_model('general', modelo)
    objeto = get_object_or_404(ModelClass, id=id, fecha__year=year, fecha__month=month, fecha__day=day)
    objeto.fecha = localtime(objeto.fecha)
    return render(request, 'general_detalle.html', {'objeto': objeto})