from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from portfolio import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('news/', views.press, name='press'),
    path('proyects/', views.proyects, name='proyects'),
    path(
        'proyect/<slug:proyect_name>/',
        views.singleProyect,
        name='singleProyect'),
    path('robots\.txt',
         TemplateView.as_view(
             template_name='robots.txt', content_type='text/plain')),
]
