from core.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sm2015_dashboard_homolog',
        'USER': 'sm2015_dashboard_homolog',
        'PASSWORD': '$Sm2015_dashboarD$HomoloG',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

BASE_URL = "http://homolog.sm2015dashboard.org"

ALLOWED_HOSTS = ['.sm2015dashboard.org', '66.228.41.76']

ADMINS = (
    ('Rafael Soares', 'rafaeltravel88@gmail.com'),
)
EMAIL_SUBJECT_PREFIX = '[SM2015-Dashboard - Homolog] - ERROR'

STATIC_ROOT = "/static/homolog/sm2015dashboard.org/"
MEDIA_ROOT = "/media/homolog/sm2015dashboard.org/"

FILES_STATIC_PATH = MEDIA_ROOT

import locale
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/www/homolog.sm2015dashboard.org/logs/app/dashboard.log',
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'request_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/www/homolog.sm2015dashboard.org/logs/app/ \
                        dashboard_request.log',
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'django.request': {  # Stop SQL debug from logging to main logger
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': False
        },
    }
}
