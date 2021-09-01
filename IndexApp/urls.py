from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name='index_page'),
	path('profile/', views.profile, name='profile_page'),
	path('profile/edit/', views.profile_edit, name='profile_edit_page'),
	path('logout/', views.logout_view, name='logout'),
	path('login/', views.login_view, name='login'),
	path('signup/', views.signup_view, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
