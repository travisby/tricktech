from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'static_website.views.index', name='index'),
)
