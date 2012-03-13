__author__ = 'Abrar'
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('accounts.views',
    # Examples:
    # url(r'^$', 'accounts.views.home', name='home'),
    # url(r'^accounts/', include('accounts.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', 'Signup'),
    url(r'^login/$', 'MyLogin'),
    url(r'^logout/$', 'MyLogout'),
    #url(r'^logedin','Success'),
    #url(r'^invalid','Invalid'),
    url(r'thanks/$','thanks'),
)
