from django.shortcuts import render
from noticias.models import Noticias

def inicio(request):
    # Obtener ultimos comunicados oficiales
    comunicados = Noticias.objects.filter(tipo='Comunicado Oficial').order_by('-fecha')[:4]

    return render(request, "inicio.html", 
                  {"comunicados": comunicados,}
                )