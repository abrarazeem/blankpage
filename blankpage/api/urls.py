'''
Created on Nov 8, 2011

@author: Abrar Azeem
'''
from django.conf.urls.defaults import patterns, include, url
from piston.authentication.oauth import OAuthAuthentication
from piston.resource import Resource
from piston.doc import documentation_view
from api.handlers import *

auth = OAuthAuthentication(realm='BlankPage API')
work = Resource(handler=WorkHandler,authentication=auth)
education = Resource(handler=EducationHandler,authentication=auth)
profile  = Resource(handler=ProfileHandler,authentication=auth)

#profile resource user profile model


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^blankpage/', include('foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    #url(r'profile/',),
    url(r'^doc/$',documentation_view),
    url(r'^work/$',work),
    #url(r'^work/?P<emitter_format>.+/$',work),
    url(r'^work/(?P<id>[^/]+)/$',work),
    url(r'^profile/$',profile),
    url(r'^profile/?P<emitter_format>.+/$',profile),
    url(r'^education/$',education),
    url(r'^education/?P<emitter_format>.+/$',education),

)
