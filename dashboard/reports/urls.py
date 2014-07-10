from django.conf.urls import patterns, url
from reports import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index,
        name='reports'),
)
