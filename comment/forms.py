from django import forms
from django.forms import ModelForm, widgets
from django.forms.widgets import Textarea
from comment.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs= {
                'class': 'form-control card-text',
                'rows': '2'
            })
        }