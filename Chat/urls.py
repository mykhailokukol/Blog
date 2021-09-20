from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.ChatView.as_view()), name='chat_page'),
    path('<int:pk>/', login_required(views.MessageEditView.as_view()), name='edit_msg_page'),
]
