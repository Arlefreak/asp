# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from models import *

def home(request):
    p_list = Proyect.objects.order_by('-pub_date')
    context = {'p_list': p_list}
    return render(request, 'index.html', context)

def about(request):
    info = singleInformation.objects.all()
    if len(info) > 0:
        info = info[0]
    info = {}
    context = {"info": info}
    return render(request, 'about.html', context)

def press(request):
    p_list = Press.objects.order_by('-pub_date')
    context = {'p_list': p_list}
    return render(request, 'press.html', context)

def proyects(request):
	p_list = Proyect.objects.all()
	context = {"p_list": p_list}
	return render(request, 'proyects.html', context)

def singleProyect(request, proyect_name):
	proyect = get_object_or_404(Proyect, slug=proyect_name)
	context = {'proyect': proyect}
	return render(request, 'single.html', context)