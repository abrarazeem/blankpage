__author__ = 'Abrar'

from django.conf.urls.defaults import patterns, include, url


# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('linked.views',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
    url(r'^$','Accounts'),
    ##twitter link account urls
    url(r'twitter/connect/$','TwitterConnect'),
    url(r'twitter/callback/','TwitterCallBack'),
    url(r'twitter/$','Twitter'),
    ##facebook link account urls
    url(r'facebook/$','FaceBook'),
    url(r'facebook/connect$','FacebookConnect'),
    url(r'facebook/callback/$','FacebookCallback'),
)
