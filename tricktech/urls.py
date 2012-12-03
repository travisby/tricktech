from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'static_website.views.index', name='index'),
                       url(r'^contact/$', 'static_website.views.contact', name='contact'),
                       url(r'^services/$', 'static_website.views.services', name='services'),
                       url(r'^admins/$', 'static_website.views.admin', name='admin'),
                       url(r'^faq/$', 'static_website.views.faq', name='faq'),
                       url(r'^chat/$', 'static_website.views.chat', name='chat'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
)
