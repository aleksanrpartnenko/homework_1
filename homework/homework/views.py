# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.forms.models import model_to_dict
from django.conf import settings
from django.shortcuts import redirect
from django.views import View

import requests, os, sys, string, unicodedata, ipaddress, re

from .forms import *
from .models import *
def home(request):
	ENTRYS=ENTRY.objects.all().values_list('PLATE', 'NAME',)
	return render(request, 'home.html',  {'ENTRYS':ENTRYS,} )
def add_plate(request):
	if request.method == 'POST':
		form1 = PLATE_NAME(request.POST)
		if form1.is_valid() :
			if   ENTRY.objects.filter(PLATE = form1.cleaned_data['PLATE'] ).exists():
				return HttpResponseRedirect('error_page?non_unique')
				
			else:
				ENTRY.objects.create(NAME = (form1.cleaned_data['NAME']), PLATE=(form1.cleaned_data['PLATE']))
		else:
			return HttpResponseRedirect('error_page?errot_id')
	else:
		form1 = PLATE_NAME()
	return render(request, 'add_plate.html',  {'form1': form1,} )
def error_page(request):
	error_id = request.GET.get('error_id', None)
	if error_id == 'non_unique' :
		error_message='Supplied PLATE ID is not unique.'
	elif error_id == 'Name_invalid' :
		error_message='You have supplied invalid information to form. Name ID not recognized.'
	else:
		error_message='UNKNOWN ERROR. A squad of highly trained monkeys has been dispached to correct that.'
	return render(request, '/error_page.html', {'error_message': error_message, 'error_id': 'error_id'} )
def success_page(request):
	success_id = request.GET.get('success_id', None)
	if success_id == 'modified' :
		success_message='Entry successfuly modified'
	elif success_id == 'deleted' :
		success_message='Entry successfuly deleted'
	elif success_id == 'added' :
		success_message='Entry successfuly added'
	else:
		success_message='UNKNOWN ERROR. A squad of highly trained monkeys has been dispached to correct that.'
	return render(request, 'webapp/success_page.html', {'success_message': success_message} )
