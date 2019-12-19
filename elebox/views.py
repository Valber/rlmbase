# -*- coding: utf-8 -*-
from django.shortcuts import render
from elebox.models import Corpus, Placekeep, Radioelem, Device
# Воспользуемся следующим примером
# http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap
import re
from django.db.models import Q
# Create your views here.


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    '''
    Splits the query string in invidual keywords, getting rid of
    unecessary spaces and grouping quoted words together.

    Example:

    >>> normalize_query('  some random  words "with   quotes  " and   spaces')
    ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    '''
    return [
        normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)
    ]


def get_query(query_string, search_fields):
    '''
    Returns a query, that is a combination of Q objects. That combination
    aims to search keywords within a model by testing the given search fields.
    '''
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


# Стартовая страница базы данных
def index(request):
    context = {'title': 'RLMbase Start Page',
               'search_home': 'index'}
    
    return render(request, 'start.html', context)


# Страница со списком моделей корпусов
def corpusview(request, aname = None):
    corpus = None
    query_string = ''
    if (request.GET):
        if ('q' in request.GET) and request.GET['q'].strip():
            query_string = request.GET['q']
            entry_query = get_query(query_string, [
                'name',
            ])
            corpus = Corpus.objects.filter(entry_query)
    elif (request.POST):
        print(request.POST)
    else:
        if aname:
            if aname[-1] == '/':
                aname = aname[:-1]
            corpus = Corpus.objects.filter(name=aname)
        else:
            corpus = Corpus.objects.all()

    context = {
        'title_page': 'Corpus',
        'search_home': '3dmodels',
        'models': corpus
    }
    return render(request, "model.html", context)


# Страница с местами хранения
def placeview(request, aname = None):
    places = None
    query_string = ''
    if (request.GET):
        print("I am here")
        if ('q' in request.GET) and request.GET['q'].strip():
            query_string = request.GET['q']
            entry_query = get_query(query_string, [
                'name',
            ])
            places = Radioelem.objects.filter(entry_query)
    elif (request.POST):
        print(request.POST)
    else:
        print("Debug here")
        if aname:
            print(aname)
            if aname[-1] == '/':
                aname = aname[:-1]
            places = Placekeep.objects.filter(name=aname)
        else:
            places = Placekeep.objects.all()
    context = {
        'title_page': 'Place',
        'models': places,
        'search_home': 'places',
        'typedata': 'places'
    }
    return render(request, "model.html", context)


# Страница с радиоэлектронными компонентами
def element(request, aname = None):
    elements = None
    query_string = ''
    if (request.GET):
        if ('q' in request.GET) and request.GET['q'].strip():
            query_string = request.GET['q']
            entry_query = get_query(query_string, [
                'name',
                'manufacturer',
                'typedev',
            ])
            elements = Radioelem.objects.filter(entry_query)
    elif (request.POST):
        print(request.POST)
    else:
        if aname:
            if aname[-1] == '/':
                aname = aname[:-1]
            elements = Radioelem.objects.filter(name=aname)
        else:
            elements = Radioelem.objects.all()
    context = {
        'title_page': 'Моё барахло',
        'search_home': 'radioelem',
        'models': elements
    }
    return render(request, "element.html", context)


# Страница устройств
def device(request, aname = None):
    devices = None
    query_string = ''
    if (request.GET):
        if ('q' in request.GET) and request.GET['q'].strip():
            query_string = request.GET['q']
            entry_query = get_query(query_string, [
                'name',
                'bom',
                'typedev',
            ])
            devices = Device.objects.filter(entry_query)
    elif (request.POST):
        print(request.POST)
    else:
        if aname:
            if aname[-1] == '/':
                aname = aname[:-1]
            devices = Device.objects.filter(name=aname)
        else:
            devices = Device.objects.all()
    context = {
        'title_page': 'Устройства',
        'models': devices,
        'search_home': 'devices',
        'typedata': 'devices'
    }
    return render(request, "model.html", context)
