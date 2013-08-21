# -*- coding: utf-8 -*-
from elebox.models import Corpus , Placekeep, Radioelem
from django.template import loader, Context
from django.http import HttpResponse
# Стартовая страница базы данных
def index(request):
    t = loader.get_template("start.html")
    c = Context({'title':'RLMbase Start Page'})
    return HttpResponse(t.render(c))

#Страница со списком моделей корпусов
def corpusview(request, aname):
    if aname :
        if aname[-1]=='/':
            aname=aname[:-1]
        corpus= Corpus.objects.filter(name=aname) 
    else:    
        corpus= Corpus.objects.all() 
    t = loader.get_template("model.html")
    c = Context({'title_page':'Corpus','models':corpus })
    return HttpResponse(t.render(c))

def placeview(request, aname):
    if aname :
        if aname[-1]=='/':
            aname=aname[:-1]
            print aname
        places = Placekeep.objects.filter(name=aname) 
    else:
        places = Placekeep.objects.all() 
    t = loader.get_template("model.html")
    c = Context({'title_page':'Place','models':places })
    return HttpResponse(t.render(c))

def element(request, aname):
    if aname :
        if aname[-1]=='/':
            aname=aname[:-1]
        elements= Radioelem.objects.filter(name=aname) 
    else:
        elements= Radioelem.objects.all() 
    t = loader.get_template("element.html")
    c = Context({'title_page':'Моё барахло','models':elements })
    return HttpResponse(t.render(c))

