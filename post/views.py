import json
import urllib
from urllib import parse, request
from urllib.parse import urlencode
from django.shortcuts import redirect, render

from post.form import PostForm
from post.models import Post, tag_choices

def view_posts(request):
    api = urllib.request.urlopen('http://127.0.0.1:8000/post/api/post/')
    txt = api.read().decode('utf-8')
    json_obj = json.loads(txt)
    
    for i in json_obj:
        i['tag'] = [j[1] for j in tag_choices if j[0] == i['tag']][0]

    context={
        'posts': json_obj,
        'form': PostForm()
    }
    return render(request,template_name='post/post_index.html',context=context)

def view_post(request, pk):
    post = Post.objects.get(pk=pk)
    context={
        'post': post,
    }
    return render(request,template_name='post/view_post.html',context=context)

def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = Post.objects.create(
            text=form.cleaned_data['text'],
            tag=form.cleaned_data['tag']
        )
        post.save()
        print('post is saved')
        return redirect('get_post')

    return redirect('get_post', context= {'form': form})

def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    print('Post is deleted')
    return redirect('get_post')

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(instance=post)
    print(form)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.text = form.cleaned_data['text']
            post.tag = form.cleaned_data['tag']
            post.save()
            print('post is saved')
            return redirect('get_post')
    
    return render(request, template_name='post/edit_post.html', context= {'form': form, 'pk': pk})
    