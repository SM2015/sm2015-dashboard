# coding: utf-8
from django.conf.urls import patterns, include, url
from graphs import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^get_triangle_graph_countries/?$', views.get_triangle_graph_countries, name="get_triangle_graph_countries"),
)
