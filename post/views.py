import json
import urllib
from urllib import parse, request
from urllib.parse import urlencode
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from comment.models import Comment
from post.form import PostForm
from post.models import Post
from datetime import datetime 


def view_all_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'form': PostForm(),
    }
    return render(request, template_name='post/post_index.html', context=context)

def view_random_posts(request):
    getHashtag()
    context = {
        'form': PostForm()
    }
    return render(request, template_name='post/random_post.html', context=context)


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


def view_post(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, template_name='post/view_post.html', context=context)


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
    #[\wก-๙]*
    print(now)
    return HttpResponse(200)