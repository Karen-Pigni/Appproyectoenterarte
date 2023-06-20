"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<<< HEAD:backend/enterarteback/asgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enterarteback.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
>>>>>>>> develop:backend/core/asgi.py

application = get_asgi_application()
