"""
WSGI config for toimittajatJaTuotteet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

###################### Lisätty ####################################

# If WEBSITE_HOSTNAME is defined as an environment variable, then we're running
# on Azure App Service and should use the production settings in production.py.
settings_module = "toimittajatJaTuotteet.production" if 'WEBSITE_HOSTNAME' in os.environ else 'toimittajatJaTuotteet.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
######################################################################

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toimittajatJaTuotteet.settings')

application = get_wsgi_application()
