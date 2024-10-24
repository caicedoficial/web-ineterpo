# Generated by Django 5.1.1 on 2024-10-08 16:54

import app.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
            ],
            options={
                'verbose_name': 'Comunidad',
                'verbose_name_plural': 'Comunidades',
            },
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('tipo', models.CharField(choices=[('Día del Idioma', 'Día del Idioma'), ('English Day', 'English Day'), ('Afrocolombianidad', 'Afrocolombianidad'), ('Día de la Secretaria', 'Día de la Secretaria'), ('Semana Deportiva', 'Semana Deportiva'), ('Día del Estudiante', 'Día del Estudiante'), ('Día del Maestro', 'Día del Maestro')], max_length=50)),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Implementaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
            ],
            options={
                'verbose_name': 'Implementación',
                'verbose_name_plural': 'Implementaciones',
            },
        ),
        migrations.CreateModel(
            name='Institucional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
            ],
            options={
                'verbose_name': 'Institucional',
                'verbose_name_plural': 'Institucionales',
            },
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo de noticia')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to=app.models.ruta_imagen)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_relacionadas', to='contenttypes.contenttype')),
            ],
        ),
    ]
