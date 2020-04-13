import json
import urllib
from urllib import parse, request
from urllib.parse import urlencode
from django.shortcuts import redirect, render

from post.form import PostForm
from post.models import Post
from comment.models import Comment

def view_all_posts(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()

    context={
        'posts': posts,
        'form': PostForm(),
        'comments': comments
    }
    return render(request,template_name='post/post_index.html',context=context)

def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = Post.objects.create(
            text=form.cleaned_data['text']
        )
        post.save()
        print('post is saved')
        return redirect('view_all_posts')

    return redirect('get_post', context= {'form': form})

def view_post(request, pk):
    post = Post.objects.get(pk=pk)
    context={
        'post': post,
    }
    return render(request, template_name='post/view_post.html', context= context)

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

    return render(request, template_name='post/edit_post.html', context= {'form': form, 'pk': pk})
