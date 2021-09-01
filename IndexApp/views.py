from django.shortcuts import render
from datetime import date
from django.contrib.auth.decorators import login_required, user_passes_test
from IndexApp import models, forms

# Create your views here.
def index(request):

	return render(request, 'IndexApp/index.html', {

		})

@login_required
def profile(request):
	user = request.user
	profiles_list = models.Profile.objects.all()
	profile = profiles_list.get(user=user.id)
	# Начало формулы расчета возраста
	age = date.today().year - profile.birth_date.year - (
		(date.today().month, date.today().day) < (
			profile.birth_date.month, profile.birth_date.day
			)
		)
	# Конец формулы расчета возраста

	return render(request, 'IndexApp/profile.html', {
			'profile': profile,
			'user_age': age,
		})

@login_required
def profile_edit(request):
	user = request.user
	profile = models.Profile.objects.get(user=user.id)
	ProfileInfoEditForm = forms.ProfileInfoEditForm()
	ProfilePhotoEditForm = forms.ProfilePhotoEditForm()
	return render(request, 'IndexApp/profile_edit.html', {
			'ProfileInfoEditForm': ProfileInfoEditForm,
			'ProfilePhotoEditForm': ProfilePhotoEditForm,
		})
