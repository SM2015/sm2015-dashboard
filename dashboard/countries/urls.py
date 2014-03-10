from django.conf.urls import patterns, url
from countries import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'/?$',
        views.countries, name="countries"),
)
