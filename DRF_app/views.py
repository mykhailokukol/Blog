from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import viewsets, authentication, permissions, viewsets

from .models import Sprint, Task
from .serializers import SprintSerializer, TaskSerializer, UserSerializer

# Create your views here.

User = get_user_model()

class DefaultMixin(object):

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer

class SprintViewSet(viewsets.ModelViewSet):

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer


# def index(request):
#
#     return render(request, 'DRF_app/index.html', {
#
#     })
