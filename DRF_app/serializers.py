from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse
from IndexApp import models as index_models


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
