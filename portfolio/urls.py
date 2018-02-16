from django.conf.urls import url

from .views import singleProyect

urlpatterns = (url(
    r'^proyect/(?P<proyect_name>[\w-]+)/$',
    singleProyect,
    name='singleProyect'), )
