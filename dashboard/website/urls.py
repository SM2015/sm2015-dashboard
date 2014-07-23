from django.conf.urls import patterns, include, url
from website import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', views.index, name="index"),
    url(r'^external/(?P<language_code>(en|es))/?$', views.index_external, name="index_external"),
    url(r'^user/login/?$', views.dashboard_login, name="dashboard_login"),
    url(r'^user/login/external/(?P<language_code>(en|es))/?$', views.dashboard_login_external, name="dashboard_login_external"),
    url(r'^user/logout/?$', views.dashboard_logout, name="dashboard_logout"),
    url(r'^user/forgot-password/?$', views.forgot_password, name="forgot_password"),
    url(r'^user/forgot-password/external/(?P<language_code>(en|es))/?$', views.forgot_password_external, name="forgot_password_external"),
    url(r'^user/reset-password/token/(?P<forgot_password_token>[0-9a-zA-Z]+)/?$', views.reset_password, name="reset_password"),
    url(r'^user/change-password/?$', views.change_password, name="change_password"),
)
