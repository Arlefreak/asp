from django.conf.urls import include, url
from .views import *

urlpatterns = (
    url(r'^proyect/(?P<proyect_name>[\w-]+)/$', singleProyect, name='singleProyect'),
)
