from django.conf.urls import patterns, include, url, i18n
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'portfolio.views.home', name='home'),
    url(r'^about/', 'portfolio.views.about', name='about'),
    url(r'^news/', 'portfolio.views.press', name='press'),
    url(r'^proyects/', 'portfolio.views.proyects', name='proyects'),
    url(r'^proyect/(?P<proyect_name>[\w-]+)/$', 'portfolio.views.singleProyect', name='singleProyect'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)
