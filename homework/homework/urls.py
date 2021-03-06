"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from . import views
from .views import EntryList, EntryDetails
from rest_framework import routers
#from .views import data_api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^home$', views.home, name = 'home'),
	url(r'^add_plate$', views.add_plate, name = 'add_plate'),
	#url(r'^/data_api/$', views.data_api.as_view()),
    url(r'^plates/(?P<pk>[0-9]+)/$', EntryList.as_view(), name='EntryList'),
    url(r'^plates$', EntryDetails.as_view(), name='EntryDetails'),
    url(r'^angular$',  views.angular, name = 'angular'),
    url(r'^plate_update$',  views.plate_update, name = 'plate_update'),
]
