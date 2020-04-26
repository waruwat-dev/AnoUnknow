from django import forms
from django.forms import ModelForm, widgets
from .models import AnnouncementModel
from django.forms import MultiWidget

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
        
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        print(cleaned_data)
        if start_time > end_time:
            raise forms.ValidationError('End date should be greater than Start date')