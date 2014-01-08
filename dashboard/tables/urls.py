from django.conf.urls import patterns, include, url
from tables import views, views_render

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^save-milestone-data/(?P<model_name>\w+)/?$', views.save_milestone_data, name="save_milestone_data"),
    
    url(r'^hitos_e_avances/?$', views.hitos_e_avances, name="hitos_e_avances"),
    url(r'^ucmilestone/?$', views.ucmilestone, name="ucmilestone"),
    url(r'^sm2015milestone/?$', views.sm2015milestone, name="sm2015milestone"),

    url(r'render/hitos/(?P<country_slug>[-\w]+)/?$', views_render.render_hitos, name="table_render_hitos"),
    url(r'render/avances_financeiros/(?P<country_slug>[-\w]+)/?$', views_render.render_avances_financeiros, name="table_render_avances_financeiros"),
    url(r'render/ucmilestone/?$', views_render.render_ucmilestone, name="table_render_ucmilestone"),
    url(r'render/sm2015milestone/?$', views_render.render_sm2015milestone, name="table_render_sm2015milestone"),

    url(r'export/(?P<file_format>[\w]+)/test/?$', views.export, name="table_export"),
)
