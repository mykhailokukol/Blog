from django.shortcuts import render, redirect
from datetime import date
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, login, authenticate
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
	# Формула расчета возраста
	age = 'Мы неспособны посчитать =('
	if profile.birth_date is not None:
		age = date.today().year - profile.birth_date.year - ((date.today().month, date.today().day) < (profile.birth_date.month, profile.birth_date.day))

	return render(request, 'IndexApp/profile.html', {
			'profile': profile,
			'user_age': age,
		})

@login_required
def profile_edit(request):
	if request.method == 'POST':
		UserEditForm = forms.EditUserForm(request.POST, instance=request.user)
		ProfileEditForm = forms.EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
		if UserEditForm.is_valid() and ProfileEditForm.is_valid():
			user_form = UserEditForm.save()
			custom_form = ProfileEditForm.save(commit=False)
			custom_form.user = user_form
			custom_form.save()
			return redirect('/profile/')
	else:
		UserEditForm = forms.EditUserForm(instance=request.user)
		ProfileEditForm = forms.EditProfileForm(instance=request.user.profile)

	return render(request, 'IndexApp/profile_edit.html', {
			'UserEditForm': UserEditForm,
			'ProfileEditForm': ProfileEditForm,
		})

@login_required
def logout_view(request):
	logout(request)
	return redirect('/')

def login_view(request):
	logout(request)

	username = password = ''
	if request.method == 'POST':
		LoginForm = forms.LoginForm(request.POST)
		if LoginForm.is_valid():
			username = request.POST['username']
			raw_password = request.POST['password']
			user = authenticate(username=username, password=raw_password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('/')
	else:
		LoginForm = forms.LoginForm()

	return render(request, 'IndexApp/login.html', {
		'LoginForm': LoginForm,
	})

def signup_view(request):
	logout(request)

	if request.method == 'POST':
		form = forms.SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.email = form.cleaned_data.get('email')
			user.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/profile/')
	else:
		form = forms.SignupForm()

	return render(request, 'IndexApp/signup.html', {
		'SignupForm': form,
	})

def about_us(request):

	misha = models.Profile.objects.get(user=request.user)

	return render(request, 'IndexApp/about_us.html', {
		'user': request.user,
		'misha': misha,
	})
