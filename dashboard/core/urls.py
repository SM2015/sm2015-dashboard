from django.conf.urls import patterns, include, url
from django.contrib import admin

from website import urls as website_urls
from tables import urls as tables_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tables/', include(tables_urls)),
    url(r'', include(website_urls)),
)
