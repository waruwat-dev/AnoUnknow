import json
import urllib
from urllib import parse, request
from urllib.parse import urlencode
from django.shortcuts import redirect, render
import requests

headers={'Content-type':'application/json', 'Accept':'application/json'}

def view_posts(request):
    api = urllib.request.urlopen('http://127.0.0.1:8000/post/api/post/')
    txt = api.read().decode('utf-8')
    json_obj = json.loads(txt)
    context={'posts':json_obj}
    return render(request,template_name='post/post_index.html',context=context)

def create_post(request):
    text_post = request.POST.get('txt')
    tag_post = request.POST.get('tag')

    dictionary = {}
    dictionary['text'] = text_post
    dictionary['tag'] = tag_post
    dictionary = json.dumps(dictionary).encode('utf-8')
    requests.post('http://127.0.0.1:8000/post/api/post/', data=dictionary, headers=headers)
    return redirect('get_post')

def delete_post(request, pk):
    requests.delete('http://127.0.0.1:8000/post/api/post/{}/'.format(pk) , headers=headers)
    return redirect('get_post')

def edit_post(request, pk):
    if request.method == 'POST':
        text_post = request.POST.get('txt')
        tag_post = request.POST.get('tag')

        dictionary = {}
        dictionary['text'] = text_post
        dictionary['tag'] = tag_post
        dictionary = json.dumps(dictionary).encode('utf-8')
        requests.put('http://127.0.0.1:8000/post/api/post/{}/'.format(pk), data=dictionary, headers=headers)
        return redirect('get_post')

    api = urllib.request.urlopen('http://127.0.0.1:8000/post/api/post/{}'.format(pk))
    txt = api.read().decode('utf-8')
    json_obj = json.loads(txt)
    context={'posts':json_obj}
    print(json_obj)
    return render(request, template_name='post/edit_post.html', context=context)
    