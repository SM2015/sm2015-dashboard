from django.conf.urls import patterns, url
from sm2015_calendar import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/?$', views.index, name="calendar"),
)
