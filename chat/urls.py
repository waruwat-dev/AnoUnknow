from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from chat import views


urlpatterns = [
    path('', views.index, name='chat_index'),
    path('friends/', views.getFriend, name='get_friends'),
    path('create/<int:randomuser>', views.createChat, name='create_chat'),
    path('message/<int:chat_id>', views.messageView, name='chat_message'),
    path('getmessage/<int:message_id>', views.getMessage, name='chat_getmessage'),
    path('block/<int:chatId>', views.blockChat, name='chat_block_chat')
]