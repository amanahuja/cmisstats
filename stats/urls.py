from django.conf.urls.defaults import *

urlpatterns = patterns('stats.views',
    url(r'^$', 'list'),
    url(r'^list', 'list'),
    url(r'^add', 'addRepo'),
)