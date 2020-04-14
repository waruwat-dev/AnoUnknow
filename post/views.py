import json
import urllib
from urllib import parse, request
from urllib.parse import urlencode
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from post.form import PostForm
from post.models import Post
from comment.models import Comment

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def view_all_posts(request):
    posts = Post.objects.all()
    # comments = Comment.objects.order_by('post_id_id').all()
    # commentz = set()
    # for i in comments:
    #     commentz.add(i.post_id_id)
    # commentz = list(commentz)  # commentz เก็บ post_idที่ไม่ซ้ำ
    # comment = dict()
    # for i in comments:
    #     for j in commentz:
    #         if i.post_id_id == j:
    #             comment[j] = i.text
    #             commentz.remove(j)
    # print(posts[0].comment_set.all())
    context = {
        'posts': posts,
        'form': PostForm(),
        # 'comment': comment
    }
    return render(request, template_name='post/post_index.html', context=context)


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
        return redirect('view_all_posts')

    return redirect('get_post', context={'form': form})


def view_post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post_id_id=pk)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, template_name='post/view_post.html', context=context)


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    print('Post is deleted')
    return redirect('view_all_posts')


def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(instance=post)
    print(form)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.text = form.cleaned_data['text']
            post.save()
            print('post is saved')
            return redirect('view_all_posts')

    return render(request, template_name='post/edit_post.html', context={'form': form, 'pk': pk})


# @api_view(['POST'])
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
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "post_post%d" % post_id, {
            'type': 'chat_message',
            'message': json
        })
