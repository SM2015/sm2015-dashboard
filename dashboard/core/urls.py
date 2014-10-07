from django.conf.urls import patterns, include, url
from django.contrib import admin

from website import urls as website_urls
from tables import urls as tables_urls
from graphs import urls as graphs_urls
from countries import urls as countries_urls
from reports import urls as reports_urls
from core import views
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tables/', include(tables_urls)),
    url(r'^graphs/', include(graphs_urls)),
    url(r'^countries/', include(countries_urls)),
    url(r'^reports/', include(reports_urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^country/list/?$', views.list_country),
    url(r'^elfinder/', include('elfinder.urls')),
    url(r'^calendar/', include('sm2015_calendar.urls')),

    url(r'', include(website_urls)),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
