from core.settings import *

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

BASE_URL = "http://sm2015dashboard.org:8000"

ALLOWED_HOSTS = ['sm2015dashboard.org']

ADMINS = (
    ('Rafael Soares', 'rafaelsantos88@gmail.com'),
)
EMAIL_SUBJECT_PREFIX = '[SM2015-Dashboard] - ERROR'

STATIC_ROOT = "/static/"
MEDIA_ROOT = "/media/"

FILES_STATIC_PATH = MEDIA_ROOT
