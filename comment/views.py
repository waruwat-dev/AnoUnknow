from django.shortcuts import render, redirect
from post.models import Post
from comment.models import Comment
from comment.forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse, JsonResponse
from .serializers import CommentCreateSerializer, CommentSerializer
from rest_framework.decorators import api_view


# @api_view(['POST'])
@csrf_exempt
def addComment(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        serializer = CommentCreateSerializer(data=request.POST)
        if serializer.is_valid():
            user = request.user
            comment = serializer.save(post_id=post, commentBy=user.authen_user.randomName())
            serializer = CommentSerializer(comment)
            message(pk, {"addComment": comment.id})
            return JsonResponse(serializer.data, status=200)
    return HttpResponse(status=400)

def getComment(request, pk):
    comment = Comment.objects.get(pk=pk)
    serializer = CommentSerializer(comment)
    return JsonResponse(serializer.data, status=200)


@csrf_exempt
def emotionComment(request, pk, type_emotion):
    comment = Comment.objects.get(pk=pk)
    if type_emotion == 1:
        comment.like += 1
        message(comment.post_id.id, {
                "like": comment.like,
                "comment": comment.id})
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
