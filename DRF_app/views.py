from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.sessions.models import Session
from rest_framework import viewsets
from rest_framework import permissions
from . import serializers
from IndexApp import models as index_models
from Chat import models as chat_models


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


class MessageViewSet(viewsets.ModelViewSet):
    """
    Обзор API модели 'Сообщение' в приложении 'Чат' с возможностью редактировать
    """
    queryset = chat_models.Message.objects.all().order_by('-sent')
    serializer_class = serializers.MessageSerializer
    permissions_class = [permissions.IsAuthenticated]


class SessionViewSet(viewsets.ModelViewSet):
    """
    Обзор API модели 'Сессия' с возможностью редактирования
    """
    queryset = Session.objects.all().order_by('session_key')
    serializer_class = serializers.SessionSerializer
    permissions_class = [permissions.IsAuthenticated]
