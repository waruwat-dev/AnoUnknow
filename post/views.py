import json
import urllib
from datetime import datetime, timedelta
from urllib import parse, request
from urllib.parse import urlencode

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import re
from comment.models import Comment
from post.form import PostForm
from post.models import Post


@login_required(login_url='login')
@permission_required('post.view_all_post', raise_exception=True)
def view_all_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'form': PostForm(),
    }
    return render(request, template_name='post/post_index.html', context=context)


def view_random_posts(request):
    context = {
        'form': PostForm(),
        'hashtags': getHashtag()
    }
    return render(request, template_name='post/random_post.html', context=context)

def view_hashtag(request, word):
    if request.method == 'POST':
        word = request.POST.get('word')
        print(word)
        posts = Post.objects.filter(text__icontains=word)
    else:
        posts = Post.objects.filter(text__icontains=word)
        all_post = list()
        for post in posts:
            if re.search(r"#[\wก-๙]*", post.text):
                all_post.append(post) 
        posts = all_post

    context = {
        'hashtags': getHashtag(),
        'posts': posts
    }
    return render(request, template_name='post/hashtag.html', context=context)

@login_required(login_url='login')
@permission_required('post.add_post', raise_exception=True)
def create_post(request):
    user = request.user
    form = PostForm(request.POST)
    if form.is_valid():
        post = Post.objects.create(
            text=form.cleaned_data['text'],
            createBy=user.authen_user.randomName()
        )
        post.save()
        print('post is saved')
        return redirect('view_random_posts')

    return render(request, template_name='post/post_index.html', context={'form': form})

@login_required(login_url='login')
def view_post(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, template_name='post/view_post.html', context=context)

@login_required(login_url='login')
@permission_required('post.delete_post', raise_exception=True)
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    print('Post is deleted')
    return redirect('view_all_posts')

@csrf_exempt
def emotionPost(request, pk, type_emotion):
    post = Post.objects.get(pk=pk)
    if type_emotion == 1:
        post.like += 1
        message(post.id, {"like": post.like})
    elif type_emotion == 2:
        post.haha += 1
        message(post.id, {"haha": post.haha})
    elif type_emotion == 3:
        post.angry += 1
        message(post.id, {"angry": post.angry})
    elif type_emotion == 4:
        post.sad += 1
        message(post.id, {"sad": post.sad})
    post.save()
    return HttpResponse(status=201)

def message(post_id, json):
    json["post"] = post_id
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "post_post%d" % post_id, {
            'type': 'chat_message',
            'message': json
        })

def getHashtag():
    now = datetime.now()
    time = now - timedelta(hours=24) 
    hashtags = list()
    stemp = now

    while time > (now - timedelta(weeks=4)) and len(set(hashtags)) < 5:
        posts = Post.objects.filter(time__gte=time, time__lt=stemp)
        for i in posts:
            hashtags +=re.findall(r"#[\wก-๙]*", i.text)
        time -= timedelta(hours=24) 
        stemp -= timedelta(hours=24)
    
    top = dict()
    for hashtag in set(hashtags):
        top[hashtag] = hashtags.count(hashtag)
    top = sorted(top.items(), key=lambda x: x[1], reverse=True)
    return top[:5]