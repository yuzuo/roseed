from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

import os

site_media =os.path.join(os.path.dirname(__file__),'..','media').replace('\\','/')             


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
    url(r'',include('app.urls')),
)






