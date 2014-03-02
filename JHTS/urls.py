from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog', include('main.urls')),
    url(r'^login/$', 'JHTS.views.loginview'),
    url(r'^logout/$', 'JHTS.views.logout'),
	url(r'^auth/$', 'JHTS.views.auth_and_login'),
    url(r'^$', include('pages.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    
	
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
