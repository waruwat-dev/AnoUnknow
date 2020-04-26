from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user.models import RandomUser
from .models import Chat, Message
from django.db.models import Q
from .serializers import ChatSerializer, MessageSendSerializer, MessageSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@login_required
@permission_required('chat.view_chat', raise_exception=True)
def index(request):
    return render(request, 'chat/chat_friend.html', {})


@login_required
@permission_required('chat.add_chat', raise_exception=True)
def createChat(request, randomuser):
    user = request.user
    randomuser1 = user.authen_user.randomName()
    randomuser2 = RandomUser.objects.get(pk=randomuser)
    if randomuser2.user == user:
        return HttpResponse(status=400)
    chat = Chat.objects.filter(Q(random_user1__user=user, random_user2=randomuser2) | Q(
        random_user2__user=user, random_user1=randomuser2))
    if not chat.exists():
        chat = Chat.objects.create(
            random_user1=randomuser1,
            random_user2=randomuser2
        )
    return redirect('chat_index')


@login_required
def getFriend(request):
    chats = Chat.objects.filter(
        Q(random_user1__user=request.user) | Q(random_user2__user=request.user))
    user1 = chats.filter(random_user1__user=request.user)
    user1 = map(lambda x: {
                "id": x.id, "name": x.random_user2.name, "my_id": x.random_user1.id}, user1)
    user2 = chats.filter(random_user2__user=request.user)
    user2 = map(lambda x: {
                "id": x.id, "name": x.random_user1.name, "my_id": x.random_user2.id}, user2)
    friends = list(user1) + list(user2)

    return JsonResponse(data=friends, status=200, safe=False)


@login_required
@permission_required('chat.view_message', raise_exception=True)
def messageView(request, chat_id):
    chat = Chat.objects.get(pk=chat_id)
    if chat.random_user1.user == request.user:
        user = chat.random_user1
    else:
        user = chat.random_user2
    if request.method == "GET":
        messages = Message.objects.filter(chat_id=chat)
        serializer = MessageSerializer(messages, many=True)
        return JsonResponse(data=serializer.data, status=200, safe=False)
    elif request.method == "POST":
        serializer = MessageSendSerializer(data=request.POST)
        if serializer.is_valid():
            chat = serializer.save(randomUser1=user, chat_id=chat)
            return HttpResponse(status=201)
    return HttpResponse(status=400)

@login_required
def getMessage(request, message_id):
    message = Message.objects.get(pk=message_id)
    serializer = MessageSerializer(message)
    return JsonResponse(data=serializer.data, status=200, safe=False)