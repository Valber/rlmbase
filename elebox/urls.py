# -*- coding: utf-8 -*-
from django.urls import path
from elebox.views import corpusview, element, placeview, device, index


urlpatterns = [
    path('', index),
    path('model3d/<str:aname>)', corpusview),
    path('element/<str:aname>)', element),
    path('place/<str:aname>)', placeview),
    path('device/<str:aname>)', device),
    # path(r'^component/$', 'component'),
]
