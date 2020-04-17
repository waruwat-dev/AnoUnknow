from rest_framework import serializers
from post.models import Post

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer


# class PostSerializer(ModelSerializer):

#     class Meta:
#         model = Post
#         fields = ('text')

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('text')
