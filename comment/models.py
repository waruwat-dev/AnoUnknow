from django.db import models
from post.models import Post
class Comment(models.Model):
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    haha = models.IntegerField(default=0)
    sad = models.IntegerField(default=0)
    angry = models.IntegerField(default=0)
    post_id = models.ForeignKey(Post, null=True,on_delete=models.CASCADE)

    class Meta:
        ordering = ['time']

