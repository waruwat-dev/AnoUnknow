from django.shortcuts import render,redirect
from post.models import Post
from comment.models import Comment
from comment.forms import CommentForm

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