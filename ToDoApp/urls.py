from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='todo_page'),
]
