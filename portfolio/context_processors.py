__author__ = 'marioc'
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

def menu(request):
    menu = {"menu": [
        {'name': 'About', 'url': reverse('about')},
        {'name': 'Proyects', 'url': reverse('proyects')},
        {'name': 'Press', 'url': reverse('press')},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu