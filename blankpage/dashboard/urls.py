__author__ = 'Abrar'
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dashboard.views',
    # Examples:
    # url(r'^$', 'accounts.views.home', name='home'),
    # url(r'^accounts/', include('accounts.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$','Dashboard'),
    url(r'profile/$','Profile'),
    url(r'profile/edit/$','ProfileEdit'),
    url(r'work/$','Works'),
    url(r'work/add/$','AddWork'),
    url(r'education/$','Educations'),
    url(r'education/add/$','AddEducation'),
    url(r'email/$','Emails'),
    url(r'email/add/$','AddEmail'),
    
)
