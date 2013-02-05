from django.conf.urls import patterns, include, url
from googleMapsTestApp.index import basicMap

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
					('^basicMap/$', basicMap),
    # Examples:
    # url(r'^$', 'googleMapsTestApp.views.home', name='home'),
    # url(r'^googleMapsTestApp/', include('googleMapsTestApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
