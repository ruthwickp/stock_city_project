from django.conf.urls import patterns, url
from stocks import views

urlpatterns = patterns('',

    # Home page reader
    url(r'^$', views.index, name='index'),

    )