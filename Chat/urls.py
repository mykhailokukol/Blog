from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.ChatView.as_view(), name='chat_page'),
]
