from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def index(request):
    return render(request, 'chat/index.html', {})

@login_required(login_url='login')
def room(request, room_name):
    print(55555)
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

@login_required(login_url='login')
def chat(request):
    return render(request, 'chat/chat_friend.html')