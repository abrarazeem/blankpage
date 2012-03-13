from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from piston.models import Token, Nonce, Consumer

#admin.site.register(Consumer)
#admin.site.register(Nonce)
#admin.site.register(Token)
import os.path

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'accounts.views.home', name='home'),
    # url(r'^accounts/', include('accounts.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$','views.Index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include("accounts.urls")),
    url(r'applications/',include('application.urls')),
    url(r'^api/',include('api.urls')),
    url(r'dashboard/',include('dashboard.urls')),
    url(r'^linked/',include('linked.urls')),
)


urlpatterns+=patterns('piston.authentication.oauth.views',
    url(r'^oauth/request_token/$','get_request_token'),
    url(r'^oauth/authorize/$','authorize_request_token'),
    url(r'^oauth/access_token/$','get_access_token'),
)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
urlpatterns += patterns('django.views.static',
    url(r'^images/(?P<path>.*)$','serve',{'document_root':os.path.join(PROJECT_PATH,'static/images/')}),
    url(r'^css/(?P<path>.*)$','serve',{'document_root':os.path.join(PROJECT_PATH,'static/css/')}),

)