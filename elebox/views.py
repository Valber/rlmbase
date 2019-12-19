# -*- coding: utf-8 -*-
from elebox.models import Corpus, Placekeep, Radioelem, Device
from django.template import loader, Context
from django.http import HttpResponse
# Воспользуемся следующим примером
# http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap
import re
from django.db.models import Q


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
    t = loader.get_template("start.html")
    c = Context({'title': 'RLMbase Start Page'})
    return HttpResponse(t.render(c))


# Страница со списком моделей корпусов
def corpusview(request, aname):
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
    t = loader.get_template("model.html")
    c = Context({
        'title_page': 'Corpus',
        'search_home': '/rlmbase/model3d/',
        'models': corpus
    })
    return HttpResponse(t.render(c))


# Страница с местами хранения
def placeview(request, aname):
    places = None
    query_string = ''
    if (request.GET):
        if ('q' in request.GET) and request.GET['q'].strip():
            query_string = request.GET['q']
            entry_query = get_query(query_string, [
                'name',
            ])
            places = Radioelem.objects.filter(entry_query)
    elif (request.POST):
        print(request.POST)
    else:
        if aname:
            if aname[-1] == '/':
                aname = aname[:-1]
            places = Placekeep.objects.filter(name=aname)
        else:
            places = Placekeep.objects.all()
    t = loader.get_template("model.html")
    c = Context({
        'title_page': 'Place',
        'models': places,
        'search_home': '/rlmbase/place/',
        'typedata': 'places'
    })
    return HttpResponse(t.render(c))


# Страница с радиоэлектронными компонентами
def element(request, aname):
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
    t = loader.get_template("element.html")
    c = Context({
        'title_page': 'Моё барахло',
        'search_home': '/rlmbase/element/',
        'models': elements
    })
    return HttpResponse(t.render(c))


# Страница устройств
def device(request, aname):
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
    t = loader.get_template("model.html")
    c = Context({
        'title_page': 'Устройства',
        'models': devices,
        'search_home': '/rlmbase/device/',
        'typedata': 'devices'
    })
    return HttpResponse(t.render(c))
