# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns =patterns('elebox.views',
	url(r'^$', 'index'),
	url(r'^model3d/(?P<aname>.*)$', 'corpusview'),
	url(r'^element/(?P<aname>.*)$', 'element'),
	url(r'^place/(?P<aname>.*)$', 'placeview'),
	#url(r'^component/$', 'component'),
)
