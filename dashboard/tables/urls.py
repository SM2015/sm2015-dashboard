from django.conf.urls import patterns, include, url
from tables import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^milestone/?$', views.milestone, name="milestone"),
    url(r'^save-milestone-data/(?P<model_name>\w+)/?$', views.save_milestone_data, name="save_milestone_data"),
    url(r'^list/estado_actual/?$', views.list_estado_actual, name="list_estado_actual"),

    url(r'render/hitos/(?P<country_slug>[-\w]+)/?$', views.render_hitos, name="table_render_hitos"),
)
