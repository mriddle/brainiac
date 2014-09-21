from django.conf.urls import patterns, url

import brainiac.views

urlpatterns = patterns('', url(r'^$', brainiac.views.index, name='index'),
                       url(r'^sorts', brainiac.views.sorts, name='sorts'))
