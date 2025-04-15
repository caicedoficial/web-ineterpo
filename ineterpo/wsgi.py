"""
WSGI config for ineterpo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ineterpo.settings')

# Cambia 'application' por 'app' para que coincida con lo que Vercel espera
app = get_wsgi_application()
app = WhiteNoise(app, root='staticfiles/')