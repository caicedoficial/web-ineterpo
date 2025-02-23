from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('all/', views.total_noticias, name='total_noticias'),
    path('<int:year>/<int:month>/<int:day>/<int:id>/', views.noticia_detalle, name='noticia'),
]