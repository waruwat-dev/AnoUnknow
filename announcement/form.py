from django import forms
from django.forms import ModelForm, widgets
from .models import AnnouncementModel

class AnnouncementForm(ModelForm):
    class Meta:
        model = AnnouncementModel
        fields = ['type', 'text', 'start_time', 'end_time']
        widgets = {
            'text': forms.Textarea(attrs= {
                'class': 'form-control card-text',
                'rows': '3'
            })
        }