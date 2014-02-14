# coding: utf-8
from django.conf.urls import patterns, include, url
from graphs import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^get_triangle_graph_countries/?$', views.get_triangle_graph_countries, name="get_triangle_graph_countries"),
    url(r'^life_save/(?P<country_slug>[-\w]+)/$', views.get_life_save, name="get_life_save_graph"),
    url(r'^country_disbursement/(?P<country_slug>[-\w]+)/$', views.get_country_disbursement, name="get_country_disbursement_graph"),
)
