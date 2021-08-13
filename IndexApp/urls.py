from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index_page'),
	path('profile/', views.profile, name='profile_page'),
]