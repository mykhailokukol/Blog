from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('profile/<int:pk>/', login_required(views.ProfileView.as_view()), name='profile_page'),
    path('post/edit/<int:pk>/', login_required(views.PostEditView.as_view()), name='post_edit_page'),
    path('post/<int:pk>/delete/', login_required(views.PostDeleteView.as_view()), name='post_delete_page'),
    path('profile/edit/', views.profile_edit, name='profile_edit_page'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('about-us/', views.about_us, name='about_us'),
    path('like/<int:pk>', views.like_post, name='like_post'),
    path('comment/<int:pk>', views.add_comment, name='add_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
