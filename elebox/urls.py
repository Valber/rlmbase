# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns =patterns('elebox.views',
	url(r'^$', 'index'),
	url(r'^model3d/$', 'corpusview'),
	url(r'^element/$', 'element'),
	#url(r'^footprint/$', 'footprint'),
	#url(r'^component/$', 'component'),
)
