from rest_framework import serializers
from .models import Comment

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer



class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']

class CommentSerializer(ModelSerializer):
    commentBy = serializers.CharField(read_only=True, source="commentBy.name")
    class Meta:
        model = Comment
        fields = "__all__"