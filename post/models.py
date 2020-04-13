<<<<<<< HEAD
=======
from idlelib.textview import view_file

>>>>>>> parent of 9b48b3e... view all post
from django.db import models
from django.contrib.auth.models import User


tag_choices = [
        ('POL', 'Politics'),
        ('GEN', 'General'),
]

class Post(models.Model):
    view = models.IntegerField(default=0)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    haha = models.IntegerField(default=0)
    sad = models.IntegerField(default=0)
    angry = models.IntegerField(default=0)
    numberOfDistribution = models.IntegerField(default=0)
    createBy = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['time']

