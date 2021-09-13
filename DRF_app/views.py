from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from . import serializers
from IndexApp import models as index_models


class UserViewSet(viewsets.ModelViewSet):
    """
    Обзор API модели Пользователя с возможностью редактировать
    """
    queryset = User.objects.all().order_by('-username')
    serializer_class = serializers.UserSerializer
    permissions_class = [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    """
    Обзор API модели 'Профиля' с возможностью редактировать
    """
    queryset = index_models.Profile.objects.all().order_by('-created')
    serializer_class = serializers.ProfileSerializer
    permissions_class = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """
    Обзор API модели 'Пост' с возможностью редактировать
    """
    queryset = index_models.Post.objects.all().order_by('-title')
    serializer_class = serializers.PostSerializer
    permissions_class = [permissions.IsAuthenticated]


class PostCommentViewSet(viewsets.ModelViewSet):
    """
    Обзор API модели 'Комментарий к Посту' с возможностью редактировать
    """
    queryset = index_models.PostComment.objects.all().order_by('-post')
    serializer_class = serializers.PostCommentSerializer
    permissions_class = [permissions.IsAuthenticated]
