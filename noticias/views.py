from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from django.http import HttpResponseServerError
from .models import Noticias

def noticias(request):
    noticias = Noticias.objects.all().order_by('-fecha')[:7]

    # Convertir fechas a zona horaria local
    for noticia in noticias:
        noticia.fecha = localtime(noticia.fecha)

    return render(request, 'noticias.html', {'noticias': noticias, 'modelo': 'Noticias'})

def total_noticias(request):
    try:
        noticias = Noticias.objects.all().order_by('-fecha')

        # Convertir fechas a zona horaria local
        for noticia in noticias:
            noticia.fecha = localtime(noticia.fecha)

        return render(request, 'all_noticias.html', {'noticias': noticias, 'check': True, 'modelo': 'Noticias'})

    except Exception as e:
        return HttpResponseServerError(f"Error al obtener datos del modelo Noticias: {e}")

def noticia_detalle(request, year, month, day, id):
    noticia = get_object_or_404(Noticias, id=id, fecha__year=year, fecha__month=month, fecha__day=day)
    
    # Convertir fecha a zona horaria local
    noticia.fecha = localtime(noticia.fecha)

    return render(request, 'general_detalle.html', {'objeto': noticia})
