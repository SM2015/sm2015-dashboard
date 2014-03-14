from django.conf.urls import patterns, url
from countries import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/?$',
        views.countries, name="countries"),
    url(r'^country_details/?$',
        views.country_details, name="countries_details"),
)
