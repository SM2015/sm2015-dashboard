from core.settings import *
import logging

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'sm2015_dashboard',
        'USER': 'sm2015_dashboard',
        'PASSWORD': '$Sm2015_dashboarD$',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

BASE_URL = "http://sm2015dashboard.org"

ALLOWED_HOSTS = ['sm2015dashboard.org']

ADMINS = (
    ('Rafael Soares', 'rafaelsantos88@gmail.com'),
)
EMAIL_SUBJECT_PREFIX = '[SM2015-Dashboard] - ERROR'

STATIC_ROOT = "/static/sm2015dashboard.org/"
MEDIA_ROOT = "/media/sm2015dashboard.org/"

FILES_STATIC_PATH = MEDIA_ROOT

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
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/var/www/sm2015dashboard.org/logs/app/dashboard.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },  
        'request_handler': {
                'level':'INFO',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': '/var/www/sm2015dashboard.org/logs/app/dashboard_request.log',
                'maxBytes': 1024*1024*5, # 5 MB
                'backupCount': 5,
                'formatter':'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'django.request': { # Stop SQL debug from logging to main logger
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': False
        },
    }
}
