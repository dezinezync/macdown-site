from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^v(?P<version>\d+(?:\.\d+)+)/$', views.version, name='version'),
)
