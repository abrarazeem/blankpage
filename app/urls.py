from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()
import os.path
urlpatterns = patterns('dashboard.views',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(admin.site.urls)),
     url(r'^$','Home'),
     url(r'^home/$','Home'),
     url(r'^authorize/$','Authorized'),
     url(r'^authorize/data/','GetData'),
     url(r'^dashboard/profile/$','Profile'),
     url(r'^dashboard/education/$','Education'),
     url(r'^dashboard/education/add/$','AddEducation'),
     url(r'^dashboard/work/$','Work'),
     url(r'^dashboard/work/add/$','AddWork'),
     url(r'^dashboard/work/update/(?P<id>\d+)/$','UpdateWork'),
     url(r'^dashboard/work/delete/(?P<id>\d+)/$','DeleteWork'),
     url(r'^dashboard/$','Dashboard'),
     url(r'^dashboard/connect/$','Connect'),
     url(r'dashboard/callback/','CallBack'),
)

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
urlpatterns += patterns('django.views.static',
    url(r'^images/(?P<path>.*)$','serve',{'document_root':os.path.join(PROJECT_PATH,'static/images/')}),
    url(r'^css/(?P<path>.*)$','serve',{'document_root':os.path.join(PROJECT_PATH,'static/css/')}),
    url(r'^js/(?P<path>.*)$','serve',{'document_root':os.path.join(PROJECT_PATH,'static/js/')}),
)
