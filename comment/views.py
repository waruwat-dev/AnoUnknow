from django.shortcuts import render, redirect
from post.models import Post
from comment.models import Comment
from comment.forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse


def addComment(request, pk):
    post = Post.objects.get(pk=pk)
    print(post)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment.objects.create(
            text=form.cleaned_data['text'],
            post_id=post
        )
        comment.save()
        print('Comment Success')
        return redirect('view_all_posts')


@csrf_exempt
def emotionComment(request, pk, type_emotion):
    comment = Comment.objects.get(pk=pk)
    if type_emotion == 1:
        comment.like += 1
        message(comment.post_id.id, {
                "like": comment.like, "comment": comment.id})
    elif type_emotion == 2:
        comment.haha += 1
        message(comment.post_id.id, {
                "haha": comment.haha, "comment": comment.id})
    elif type_emotion == 3:
        comment.angry += 1
        message(comment.post_id.id, {
                "angry": comment.angry, "comment": comment.id})
    elif type_emotion == 4:
        comment.sad += 1
        message(comment.post_id.id, {
                "sad": comment.sad, "comment": comment.id})
    comment.save()
    return HttpResponse(status=201)


def message(post_id, json):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "post_post%d" % post_id, {
            'type': 'chat_message',
            'message': json
        })
