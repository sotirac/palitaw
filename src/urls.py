from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover() 

urlpatterns = patterns('',  
	# (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/caritos/webapps/palitaw/lib/python2.5/django/contrib/admin/media'}),
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/eladio/code/palitaw/media'}),
	(r'^/?$', 'src.websites.views.index'),
	(r'^websites/$', 'src.websites.views.index'), 
	
    # Example:
    # (r'^src/', include('src.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
