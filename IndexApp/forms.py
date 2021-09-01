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
