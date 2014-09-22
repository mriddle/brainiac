from django.conf.urls import patterns, url

urlpatterns = patterns('brainiac.views',
                       url(r'^$', 'index'),
                       url(r'^bubble-sort', 'bubble_sort'))
