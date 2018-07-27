from django import forms

import re
class PLATE_NAME(forms.Form):
	PLATE = forms.CharField(label='PLATE', max_length=6)
	def clean_PLATE(self):
		pattern = re.compile("[a-zA-z]{3}[\d]{3}$")
		data = self.cleaned_data['PLATE']
		if not pattern.match(data):
			raise forms.ValidationError("Plate number is wrong")
		return data
	NAME = forms.CharField(label='NAME', max_length=100)
	def clean_NAME(self):
		pattern = re.compile("[a-zA-z]{1,20} [a-zA-z]{1,20}$")
		data = self.cleaned_data['NAME']
		if not pattern.match(data):
			raise forms.ValidationError("Name is wrong")
		return data
