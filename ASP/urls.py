from django.conf.urls import include, url, i18n
from django.contrib import admin
from django.views.generic import TemplateView
from portfolio.views import *

urlpatterns = (
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^about/', about, name='about'),
    url(r'^news/', press, name='press'),
    url(r'^proyects/', proyects, name='proyects'),
    url(r'^proyect/(?P<proyect_name>[\w-]+)/$', singleProyect, name='singleProyect'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
)
