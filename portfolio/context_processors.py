__author__ = 'marioc'
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

def menu(request):
    menu = {"menu": [
        {'name': 'About', 'url': reverse('about')},
        {'name': _('Proyectos'), 'url': reverse('proyects')},
        {'name': _('Noticias'), 'url': reverse('press')},
        {'name': _('Instagram'), 'url': "http://instagram.com/potro01/"},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu
