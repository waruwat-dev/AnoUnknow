from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, 'chat/chat_friend.html', {})


@login_required
def chat(request):
    return render(request, 'chat/chat_friend.html')
