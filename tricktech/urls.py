from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'static_website.views.index', name='index'),
    url(r'^register/$', 'static_website.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'redirect_field_name': 'index'}),
    url(r'^contact/$', 'static_website.views.contact', name='contact'),
    url(r'^services/$', 'static_website.views.services', name='services'),
    url(r'^tAdmin/$', 'static_website.views.admin', name='tricktechAdmin'),
    url(r'^admins/$', 'static_website.views.admin', name='admin'),
    url(r'^faq/$', 'static_website.views.faq', name='faq'),
    url(r'^chat/$', 'static_website.views.chat', name='chat'),
    url(r'^ajax_chat/(?P<last_message>.*)/$', 'static_website.views.ajax_chat', name='ajax_chat'),
    url(r'^ajax_chat/$', 'static_website.views.ajax_chat', name='ajax_chat_init'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
)
