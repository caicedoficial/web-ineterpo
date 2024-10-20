from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from django.apps import apps
from django.http import Http404
from django.db.models import Prefetch
from .models import Imagenes

def principal(request):
    return render(request, 'principal.html')

def eventos(request):
    return render(request, 'eventos.html')

def titulo_imagen(request, modelo):
    try:
        # Obtener el modelo dinámicamente
        modelo_class = apps.get_model(app_label='app', model_name=modelo)
        
        # Obtener el ContentType para el modelo actual
        content_type = ContentType.objects.get_for_model(modelo_class)
        
        # Prefetch de la primera imagen relacionada
        imagenes_prefetch = Prefetch(
            'imagenes_relacionadas',
            queryset=Imagenes.objects.filter(content_type=content_type).order_by('id'),
            to_attr='todas_imagenes'
        )
        
        # Obtener todos los objetos del modelo con sus imágenes
        objetos = modelo_class.objects.prefetch_related(imagenes_prefetch).all()
        
        objetos_simplificados = [
            {
                'id': obj.id,
                'titulo': obj.titulo,
                'primera_imagen': obj.todas_imagenes[0].imagen.url if obj.todas_imagenes else None,
            }
            for obj in objetos
        ]

        # Obtener la primera imagen relacionada con cualquier objeto del modelo, si existe
        primera_imagen_modelo = next((obj['primera_imagen'] for obj in objetos_simplificados if obj['primera_imagen']), None)
        
        # Obtener el nombre del modelo
        nombre_modelo = modelo_class._meta.verbose_name_plural.title()
        
        # Preparar el contexto
        contexto = {
            'nombre_modelo': nombre_modelo,
            'objetos_simplificados': objetos_simplificados,
            'primera_imagen_modelo': primera_imagen_modelo,
        }
        
        # Renderizar la plantilla
        return render(request, 'titulo-imagen.html', contexto)
    
    except LookupError:
        # Si el modelo no existe, lanzar un error 404
        raise Http404(f"El modelo '{modelo}' no existe")

def detalle_objeto(request, modelo, id, titulo):
    try:
        # Obtener el modelo dinámicamente
        modelo = apps.get_model(app_label='app', model_name=modelo)
        
        # Obtener el ContentType para el modelo actual
        content_type = ContentType.objects.get_for_model(modelo)
        
        # Prefetch de todas las imágenes relacionadas
        imagenes_prefetch = Prefetch(
            'imagenes_relacionadas',
            queryset=Imagenes.objects.filter(content_type=content_type).order_by('id'),
            to_attr='todas_imagenes'
        )
        
        # Obtener el objeto específico con sus imágenes
        objeto = get_object_or_404(modelo.objects.prefetch_related(imagenes_prefetch), id=id)
        
        # Preparar los datos del objeto
        objeto_detallado = {
            'titulo': objeto.titulo,
            'descripcion': objeto.descripcion if hasattr(objeto, 'descripcion') else '',
            'fecha': objeto.fecha if hasattr(objeto, 'fecha') else None,
            'imagenes': [img.imagen.url for img in objeto.todas_imagenes] if objeto.todas_imagenes else [],
        }
        
        # Obtener el nombre del modelo
        nombre_modelo = modelo._meta.verbose_name_plural.title()
        
        # Preparar el contexto
        contexto = {
            'nombre_modelo': nombre_modelo,
            'objeto': objeto_detallado,
        }
        
        # Renderizar la plantilla
        return render(request, 'detalle-objeto.html', contexto)
    
    except LookupError:
        # Si el modelo no existe, lanzar un error 404
        raise Http404(f"El modelo '{modelo}' no existe")

def titulo_imagen_tipo(request, modelo, tipo):
    try:
        # Obtener el modelo dinámicamente
        modelo = apps.get_model(app_label='app', model_name=modelo)
        
        # Obtener el ContentType para el modelo actual
        content_type = ContentType.objects.get_for_model(modelo)
        
        # Prefetch de todas las imágenes relacionadas
        imagenes_prefetch = Prefetch(
            'imagenes_relacionadas',
            queryset=Imagenes.objects.filter(content_type=content_type).order_by('id'),
            to_attr='todas_imagenes'
        )
        
        # Filtrar por tipo y obtener objetos con todas las imágenes
        objetos = modelo.objects.filter(tipo=tipo).prefetch_related(imagenes_prefetch)
        
        objetos_simplificados = [
            {
                'id': obj.id,
                'titulo': obj.titulo,
                'primera_imagen': obj.todas_imagenes[0].imagen.url if obj.todas_imagenes else None
            }
            for obj in objetos
        ]
        
        # Obtener la primera imagen relacionada con cualquier objeto del modelo, si existe
        primera_imagen_modelo = next((obj['primera_imagen'] for obj in objetos_simplificados if obj['primera_imagen']), None)
        
        # Obtener el nombre del modelo
        nombre_modelo = modelo._meta.verbose_name_plural.title()
        
        # Preparar el contexto
        contexto = {
            'nombre_modelo': nombre_modelo,
            'objetos_simplificados': objetos_simplificados,
            'primera_imagen_modelo': primera_imagen_modelo,
        }
        
        # Renderizar la plantilla
        return render(request, 'titulo-imagen.html', contexto)
    
    except LookupError:
        # Si el modelo no existe, lanzar un error 404
        raise Http404(f"El modelo '{modelo}' no existe")

def detalle_objeto_tipo(request, modelo, tipo, id):
    try:
        # Obtener el modelo dinámicamente
        modelo = apps.get_model(app_label='app', model_name=modelo)
        
        # Obtener el ContentType para el modelo actual
        content_type = ContentType.objects.get_for_model(modelo)
        
        # Prefetch de todas las imágenes relacionadas
        imagenes_prefetch = Prefetch(
            'imagenes_relacionadas',
            queryset=Imagenes.objects.filter(content_type=content_type).order_by('id'),
            to_attr='todas_imagenes'
        )
        
        # Obtener el objeto específico con sus imágenes, filtrando por tipo
        objeto = get_object_or_404(modelo.objects.prefetch_related(imagenes_prefetch), id=id, tipo=tipo)
        
        # Preparar los datos del objeto
        objeto_detallado = {
            'titulo': objeto.titulo,
            'descripcion': objeto.descripcion if hasattr(objeto, 'descripcion') else '',
            'fecha': objeto.fecha if hasattr(objeto, 'fecha') else None,
            'imagenes': [img.imagen.url for img in objeto.todas_imagenes] if objeto.todas_imagenes else [],
            'tipo': tipo,
        }
        
        # Obtener el nombre del modelo
        nombre_modelo = modelo._meta.verbose_name.title()
        
        # Preparar el contexto
        contexto = {
            'nombre_modelo': nombre_modelo,
            'objeto': objeto_detallado,
        }
        
        # Renderizar la plantilla
        return render(request, 'detalle-objeto.html', contexto)
    
    except LookupError:
        # Si el modelo no existe, lanzar un error 404
        raise Http404(f"El modelo '{modelo}' no existe")
