from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from rest_framework import serializers
from rest_framework.reverse import reverse
from IndexApp import models as index_models
from Chat import models as chat_models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', ]


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = index_models.Profile
        fields = ['user', 'birth_date', 'activity', 'location', ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = index_models.Post
        fields = ['title', 'text', 'likes', ]


class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = index_models.PostComment
        fields = ['text', 'user', 'post', ]


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = chat_models.Message
        fields = ['text', 'sent', 'edited', 'author', 'image', 'anonymous_author']


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['session_key', 'expire_date', ]
