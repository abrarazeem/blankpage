from django.contrib import admin
from piston.models import Consumer, Nonce , Token

__author__ = 'Abrar'
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#admin.autodiscover()
urlpatterns = patterns('application.views',
    # Examples:
    # url(r'^$', 'accounts.views.home', name='home'),
    # url(r'^accounts/', include('accounts.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^add_app/$', 'add_app'),
    url(r'^(?P<app_id>\d+)/$', 'application'),
    url(r'^$', 'applications'),
    url(r'thanks/$','thanks'),
)
