"""
WSGI config for Chatbot_de_atendimento_simulado_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "Chatbot_de_atendimento_simulado_backend.chatbot_project.settings")

application = get_wsgi_application()
