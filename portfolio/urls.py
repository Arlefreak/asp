from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^proyect/(?P<proyect_name>[\w-]+)/$', 'portfolio.views.singleProyect', name='singleProyect'),
)