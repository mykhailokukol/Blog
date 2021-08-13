from django import forms
from IndexApp import models


class ProfileInfoEditForm(forms.Form):
	location = forms.CharField(max_length=32, label='Город, Страна')
	birth_date = forms.DateField(widget=forms.DateInput(), label='Дата рождения')
	activity = forms.CharField(max_length=128, label='Деятельность')
	about_text = forms.CharField(widget=forms.Textarea(attrs={
		"rows":5,
		"cols":20,
		"style":"resize:none;"
		}), label='О себе')
#
class ProfilePhotoEditForm(forms.Form):
	class Meta:
		model = models.Profile
		fields = (
				'photo',
			)
		labels = {
				'photo': 'Загрузите фото',
		}
