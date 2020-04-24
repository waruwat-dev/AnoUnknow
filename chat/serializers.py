from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# from chat.models import MessageModel
from rest_framework.serializers import ModelSerializer, CharField
# from user.models import RandomUser
from .models import Chat, Message

class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'random_user1', 'random_user2')

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class MessageSendSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ["text"]