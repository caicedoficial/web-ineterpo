# Generated by Django 5.1.6 on 2025-02-23 19:27

import django.db.models.deletion
import noticias.models
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descripcion', tinymce.models.HTMLField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(choices=[('General', 'General'), ('Politica', 'Política'), ('Economia', 'Economía'), ('Comunicado Oficial', 'Comunicado Oficial'), ('Deportes', 'Deportes'), ('Cultura', 'Cultura'), ('Tecnologia', 'Tecnología')], default='general', max_length=20, verbose_name='Tipo de Noticia')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
        migrations.CreateModel(
            name='ImagenesNoticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to=noticias.models.ImagenesNoticias.imagen_ruta)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='noticias.noticias')),
            ],
            options={
                'verbose_name': 'imagen',
                'verbose_name_plural': 'imagenes de la noticia',
            },
        ),
    ]
