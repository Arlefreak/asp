from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'portfolio.views.home', name='home'),
    url(r'^about/', 'portfolio.views.about', name='about'),
    url(r'^press/', 'portfolio.views.press', name='press'),
    url(r'^proyects/', 'portfolio.views.proyects', name='proyects'),
    url(r'^proyect/(?P<proyect_name>[\w-]+)/$', 'portfolio.views.singleProyect', name='singleProyect'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)