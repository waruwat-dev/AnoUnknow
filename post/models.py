from idlelib.textview import view_file

from django.db import models

tag_choices = [
        ('POL', 'politics'),
        ('GEN', 'General'),
]

class Post(models.Model):
    view = models.IntegerField(max_length=10)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)
    like = models.IntegerField(max_length=10)
    haha = models.IntegerField(max_length=10)
    sad = models.IntegerField(max_length=10)
    angry = models.IntegerField(max_length=10)
    tag = models.CharField(max_length=3 ,choices=tag_choices)
    number_of_distribution = models.IntegerField(max_length=10)

    class Meta:
        ordering = ['time']
