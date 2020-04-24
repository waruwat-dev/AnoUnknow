from django.db import models
from post.models import Post
from user.models import RandomUser

class Comment(models.Model):
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    haha = models.IntegerField(default=0)
    sad = models.IntegerField(default=0)
    angry = models.IntegerField(default=0)
    post_id = models.ForeignKey(Post, null=True,on_delete=models.CASCADE)
    commentBy = models.ForeignKey(RandomUser, null=True,on_delete=models.CASCADE, related_name='commentBy')

    class Meta:
        ordering = ['time']

