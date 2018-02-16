# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render

from .models import HomeSliderImages, Press, Proyect, SingleInformation


def home(request):
    p_list = HomeSliderImages.objects.all()
    context = {'p_list': p_list}
    return render(request, 'index.html', context)


def about(request):
    print(request.LANGUAGE_CODE)
    info = SingleInformation.objects.filter(published=True)
    if len(info) > 0:
        info = info[0]
    else:
        info = {}
    context = {"info": info}
    return render(request, 'about.html', context)


def press(request):
    p_list = Press.objects.order_by('-pub_date')
    context = {'p_list': p_list}
    return render(request, 'press.html', context)


def proyects(request):
    p_list = Proyect.objects.filter(proyects=True).order_by('order')
    context = {"p_list": p_list}
    return render(request, 'proyects.html', context)


def singleProyect(request, proyect_name):
    proyect = get_object_or_404(Proyect, slug=proyect_name)
    context = {'proyect': proyect}
    return render(request, 'single.html', context)
