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

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time > end_time:
            raise forms.ValidationError('End date should be greater than Start date')