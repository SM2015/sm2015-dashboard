from django.conf.urls import patterns, include, url
from website import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', views.index, name="index"),
    url(r'^user/login/?$', views.dashboard_login, name="dashboard_login"),
    url(r'^user/logout/?$', views.dashboard_logout, name="dashboard_logout"),
    url(r'^user/forgot-password/?$', views.forgot_password, name="forgot_password"),
    url(r'^user/(?P<dashboard_user_id>[0-9]+)/reset-password/token/(?P<forgot_password_token>[0-9a-zA-Z]+)/?$', views.reset_password, name="reset_password"),
    url(r'^user/change-password/(?P<user_id>[0-9]+)/?$', views.change_password, name="change_password"),
)
