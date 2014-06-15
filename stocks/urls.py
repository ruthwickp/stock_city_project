from django.conf.url import patterns, url
from rango import views

urlpatterns = patterns('',

    # Home page reader
    url(r'^$', views.index, name='index'),

    )