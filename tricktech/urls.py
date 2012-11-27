from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'static_website.views.index', name='index'),
    url(r'^contact/$', 'static_website.views.contact', name='contact'),
    url(r'^services/$', 'static_website.views.services', name='services'),
    url(r'^admins/$', 'static_website.views.admin', name='admin'),
    url(r'^faq/$', 'static_website.views.faq', name='faq'),
)
