from django import forms
from IndexApp import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):

	username = forms.CharField(max_length=128, label='Никнейм')
	password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

class SignupForm(UserCreationForm):

	first_name = forms.CharField(max_length=128, label='Имя')
	last_name = forms.CharField(max_length=128, label='Фамилия')
	email = forms.EmailField(max_length=128, label='Электронная почта')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class EditUserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', )

class EditProfileForm(forms.ModelForm):

	class Meta:
		model = models.Profile
		fields = ('location', 'birth_date', 'activity', 'about_text', 'photo', )
		labels = {
			'location': 'Место проживания',
			'birth_date': 'Дата рождения (ДД.ММ.ГГГГ)',
			'activity': 'Кратко о себе',
			'about_text': 'Развернуто о себе',
			'photo': 'Ваше фото',
		}
