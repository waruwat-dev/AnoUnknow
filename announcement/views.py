from django.shortcuts import render
from .form import AnnouncementForm
from .models import AnnouncementModel
from user.models import Authen_User
import datetime

def viewAnnounce(request):
    pass

def announce(request):
    now = datetime.datetime.now()
    admin = request.user.authen_user.getAdmin()
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            start_time = form.cleaned_data['start_time']
            is_active=False
            if start_time > now:
                is_active=True
            AnnouncementModel.objects.create(
                text=form.cleaned_data['text'],
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time'],
                is_active=is_active,
                type=form.cleaned_data['type'],
                adminId=admin
            )
    else:
        form = AnnouncementForm()
    
    context = {
        'form': form,
        'title': 'Add Anouncement'
    }

    return render(request, 'announcement/add_announcement.html', context=context)


def editAnnounce(request):
    pass

def deleteAnnounce(request):
    pass