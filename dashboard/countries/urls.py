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

    url(r'^api/list_location/?$',
        views.api_list_location, name="country_list_location"),
    url(r'^api/list_isech/?$',
        views.api_list_isech, name="country_list_isech"),
    url(r'^api/list_level/?$',
        views.api_list_level, name="country_list_level"),
    url(r'^api/list_pago/?$',
        views.api_list_pago, name="country_list_pago"),
)
