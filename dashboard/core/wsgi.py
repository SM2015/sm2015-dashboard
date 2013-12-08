"""
WSGI config for dashboard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
sys.path.append("/var/www/sm2015dashboard.org/src/dashboard/")

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings_wsgi")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
