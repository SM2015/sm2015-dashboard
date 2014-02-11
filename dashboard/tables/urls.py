from django.conf.urls import patterns, include, url
from tables import views, views_render, views_export

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^save-milestone-data/?$', views.save_milestone_data, name="save_milestone_data"),
    
    url(r'^hitos_e_avances/?$', views.hitos_e_avances, name="hitos_e_avances"),
    url(r'^ucmilestone/?$', views.ucmilestone, name="ucmilestone"),
    url(r'^sm2015milestone/?$', views.sm2015milestone, name="sm2015milestone"),
    url(r'^grants_finances/?$', views.grants_finances, name="grants_finances"),
    url(r'^life_save/?$', views.life_save, name="life_save"),

    url(r'render/hitos/(?P<country_slug>[-\w]+)/?$', views_render.render_hitos, name="table_render_hitos"),
    url(r'render/avances_financeiros/(?P<country_slug>[-\w]+)/?$', views_render.render_avances_financeiros, name="table_render_avances_financeiros"),
    url(r'render/ucmilestone/?$', views_render.render_ucmilestone, name="table_render_ucmilestone"),
    url(r'render/sm2015milestone/?$', views_render.render_sm2015milestone, name="table_render_sm2015milestone"),
    url(r'render/grants_finances/?$', views_render.render_grants_finances, name="table_render_grants_finances"),
    url(r'render/life_save/(?P<country_slug>[-\w]+)/?$', views_render.render_life_save, name="table_render_life_save"),

    url(r'render/export/hitos_y_avances/(?P<country_slug>[-\w]+)/?$', views_export.render_export_hitos_and_avances, name="table_export_hitos_and_avances"),

    url(r'grants_finances/ongoing/(?P<uuid_origin>[\_A-Z]+)/?$', views.grants_finances_ongoing, name="grants_finances_ongoing"),
    url(r'chart_flot/(?P<uuid_type>[\_A-Z]+)/?$', views.chart_flot, name="chart_flot"),

    url(r'import/excel/', views.import_excel, name="table_import_excel"),
)
