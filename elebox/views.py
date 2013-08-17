# -*- coding: utf-8 -*-
#from django.conf.elebox.models import 
from django.template import loader, Context
from django.http import HttpResponse
# Стартовая страница базы данных
def index(request):
        t = loader.get_template("start.html")
        c = Context({'title':'RLMbase Start Page'})
        return HttpResponse(t.render(c))
#Страница со списком моделей корпусов
# def models(request):
#         models3d= model3D.objects.all() 
#         t = loader.get_template("model.html")
#         c = Context({'title_page':'3D Models','models':models3d })
#         return HttpResponse(t.render(c))

# def footprint(request):
#         footprints= Footprint.objects.all() 
#         t = loader.get_template("model.html")
#         c = Context({'title_page':'Footprints','models':footprints })
#         return HttpResponse(t.render(c))

# def component(request):
#         shems= Schematic.objects.all() 
#         t = loader.get_template("model.html")
#         c = Context({'title_page':'Schematics','models':shems })
#         return HttpResponse(t.render(c))

# def element(request):
#         elements= RealElement.objects.all() 
#         t = loader.get_template("model.html")
#         c = Context({'title_page':'Real Devices','models':elements })
#         return HttpResponse(t.render(c))

