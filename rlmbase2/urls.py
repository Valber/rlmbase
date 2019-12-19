# -*- coding: utf-8 -*-
from django.urls import include, path
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'rlmbase2.views.home', name='home'),
    path('rlmbase/', include('elebox.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns = [
#         path(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT,
#             'show_indexes': True
#         }),
#         path(r'', include('django.contrib.staticfiles.urls')),
#     ] + urlpatterns
