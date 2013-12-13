from django.conf.urls import patterns, include, url
from tables import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^milestone/?$', views.milestone, name="milestone"),
    url(r'^save-milestone-data/?$', views.save_milestone_data, name="save_milestone_data"),
)
