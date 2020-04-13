from django import forms
from django.forms import ModelForm, widgets
from django.forms.widgets import Textarea
from post.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs= {
                'class': 'form-control card-text',
                'rows': '3'
            })
        }