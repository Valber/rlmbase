from django.urls import path
from elebox.views import index, corpusview, element, placeview, device


urlpatterns = [
    path('', index, name='index'),
    path('model3d/<str:aname>/', corpusview, name='3dmodels'),
    path('model3d/', corpusview, name='3dmodels'),
    path('element/', element, name='radioelem'),
    path('element/<str:aname>/', element, name='radioelem'),
    path('place/', placeview, name='places'),
    path('place/<str:aname>/', placeview, name='places'),
    path('device/', device, name= 'devices'),
    path('device/<str:aname>/', device, name= 'devices'),
    # path(r'^component/$', 'component'),
]
