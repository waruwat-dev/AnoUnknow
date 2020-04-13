from idlelib.textview import view_file
from django.db import models

class Post(models.Model):
    view = models.IntegerField(default=0)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    haha = models.IntegerField(default=0)
    sad = models.IntegerField(default=0)
    angry = models.IntegerField(default=0)
    number_of_distribution = models.IntegerField(default=0)

    class Meta:
        ordering = ['time']
