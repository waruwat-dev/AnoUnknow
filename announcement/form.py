from django import forms
from django.forms import ModelForm, widgets
from .models import AnnouncementModel
from django.forms import MultiWidget
from datetime import datetime

class AnnouncementForm(ModelForm):
    widget = forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'})
    start_time = forms.SplitDateTimeField(widget=widget)
    end_time = forms.SplitDateTimeField(widget=widget)
    class Meta:
        model = AnnouncementModel
        fields = ['type', 'text', 'start_time', 'end_time']
        widgets = {
            'text': forms.Textarea(attrs= {
                'class': 'form-control card-text',
                'rows': '3'
            })
        }
    
    def clean_start_time(self):
        data = self.cleaned_data['start_time']
        now = datetime.now()
        print(now)
        if data < now:
            raise forms.ValidationError('Start datetime should be greater than now')
        return data
        
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        print(cleaned_data)

        if start_time and start_time > end_time:
            raise forms.ValidationError('End datetime should be greater than Start datetime')