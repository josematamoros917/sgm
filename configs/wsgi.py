"""
WSGI config for configs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/skullgaragemotorcycle/sgm'  # Ruta al directorio raíz de tu proyecto en PythonAnywhere
if path not in sys.path:
    sys.path.append(path)

# Aquí indicamos que las configuraciones están en el directorio 'configs' y el archivo se llama 'settings.py'
os.environ['DJANGO_SETTINGS_MODULE'] = 'configs.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


