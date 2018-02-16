__author__ = 'marioc'
from django.urls import reverse
from django.utils.translation import ugettext as _


def menu(request):
    menu = {
        "menu": [
            {
                'name': 'About',
                'url': reverse('about')
            },
            {
                'name': _('Proyectos'),
                'url': reverse('proyects')
            },
            {
                'name': _('Noticias'),
                'url': reverse('press')
            },
        ]
    }
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu
