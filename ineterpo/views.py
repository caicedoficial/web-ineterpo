from django.shortcuts import render
from noticias.models import Noticias

def inicio(request):
    # Obtener ultima noticia
    noticia = Noticias.objects.order_by('-fecha')[:1]

    return render(request, "inicio.html", 
                  {"noticia": noticia,}
                )