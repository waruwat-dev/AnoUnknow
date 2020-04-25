import json
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from post.models import Post
from post.serializers import PostSerializer

from .views import message


def get_random_posts(request):
    if request.method == 'GET':
        posts = list(Post.objects.filter(numberOfDistribution__gte=1))
        posts = reduce_distribute(posts)
        lenght = len(posts)
        if lenght < 5:
            allPosts = list(Post.objects.all().order_by('-time'))
            posts += allPosts[:5-lenght]
            print('Post by Time')
        random.shuffle(posts)
        serializer = PostSerializer(set(posts), many=True)
        # print('Get Post', serializer.data)
        return JsonResponse(serializer.data, safe=False)
        # return render(request, 'post/list_post_components.html', {"posts":posts})

def get_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post/post_component.html', {"post":post})

def get_detail_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post/DetailPostComponent.html', {"post":post})

def distribute_post(request, post_id):
    user = request.user
    check = Post.objects.filter(pk=post_id ,distributeUser__user__id=user.id)
    if check:
        print("You've already distributed this post")
    else:
        post = Post.objects.get(pk=post_id)
        post.numberOfDistribution += 5
        post.save()
        post.distributeUser.add(user.authen_user.randomName())
        print("distributed post")
        message(post.id, {"distribute": post.getNumberOfDis})
    return HttpResponse(200)

def reduce_distribute(posts):
    random.shuffle(posts)
    for post in posts[:5]:
        post.numberOfDistribution -= 1
        post.save()
    return posts[:5]

def edit_post(request):
    data = dict(request.POST)
    print(data['id'][0])
    post = Post.objects.get(pk=int(data['id'][0]))
    post.text = data['text'][0]
    post.save()
    return HttpResponse(200)
    # form = PostForm(instance=post)
    # print(form)
    # if request.method == 'POST':
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post.text = form.cleaned_data['text']
    #         post.save()
    #         print('post is saved')
    #         return redirect('view_post', pk=pk)

    # return render(request, template_name='post/edit_post.html', context={'form': form, 'pk': pk})
