from django.urls import path
from elebox.views import index, corpusview, element, placeview, device


urlpatterns = [
    path('', index),
    path('model3d/<str:aname>/', corpusview),
    path('model3d/', corpusview),
    path('element/', element),
    path('element/<str:aname>/', element),
    path('place/', placeview),
    path('place/<str:aname>/', placeview),
    path('device/', device),
    path('device/<str:aname>/', device),
    # path(r'^component/$', 'component'),
]
