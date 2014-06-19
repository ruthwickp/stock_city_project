from django.conf.urls import patterns, url
from stocks import views

urlpatterns = patterns('',

    # Home page reader
    url(r'^$', views.index, name='index'),

    # Link for each stock
    url(r'^(?P<stock_symbol>\w+)/$', views.stock, name='stock'),

    )