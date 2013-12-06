from django.conf.urls import patterns, include, url
from core import views as core_view
from website import views as website_view

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', website_view.index, name="index"),
    url(r'^login/?$', website_view.dashboard_login, name="dashboard_login"),
    url(r'^logout/?$', website_view.dashboard_logout, name="dashboard_logout"),
    url(r'^forgot-password/?$', website_view.forgot_password, name="forgot_password"),

    #user
    url(r'^user/(?P<dashboard_user_id>[0-9]+)/reset_password/token/(?P<forgot_password_token>[0-9a-zA-Z]+)/?$', website_view.reset_password, name="reset_password"),
)
