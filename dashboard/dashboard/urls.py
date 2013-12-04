from django.conf.urls import patterns, include, url
from core import views as core_view
from website import views as website_view

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', website_view.index, name="home"),
    url(r'^login/?$', website_view.dashboard_login, name="dashboard_login"),
    url(r'^logout/?$', website_view.dashboard_logout, name="dashboard_logout"),

    #user
    url(r'^user/register/?$', website_view.register_user, name="register_user"),
    url(r'^user/activate/?$', website_view.activate_registered_user, name="activate_user"),
)
