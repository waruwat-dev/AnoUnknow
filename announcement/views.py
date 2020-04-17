import datetime
from django.shortcuts import redirect, render
from user.models import Authen_User
from .form import AnnouncementForm
from .models import AnnouncementModel, typeOfAnnouncement


def viewAnnounce(request):
    announcements = AnnouncementModel.objects.filter(is_active=True)
    typeDict = {t[0]: t[1] for t in typeOfAnnouncement}
    for announcement in announcements:
        announcement.type = typeDict[announcement.type]
    print(announcements)
    context = {
        'announcements': announcements
    }

    return render(request, 'announcement/view_announcement.html', context=context)


def announce(request):
    now = datetime.datetime.now()
    admin = request.user.authen_user.getAdmin()

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            start_time = form.cleaned_data['start_time']
            form = form.save()
            if start_time > now:
                form.is_active = True
            form.adminId = admin
            form.save()
            print('Create Announcement --', admin.user.username)
            return redirect('view_announcement')
    else:
        form = AnnouncementForm()
    
    context = {
        'form': form,
        'title': 'Add Anouncement'
    }

    return render(request, 'announcement/add_announcement.html', context=context)


def editAnnounce(request, announcement_id):
    now = datetime.datetime.now()
    admin = request.user.authen_user.getAdmin()
    announcement = AnnouncementModel.objects.get(pk=announcement_id)

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            start_time = form.cleaned_data['start_time']
            form = form.save()
            if start_time > now:
                form.is_active = True
            form.adminId = admin
            form.save()
            print('Create Announcement --', admin.user.username)
            return redirect('view_announcement')
    else:
        form = AnnouncementForm(instance=announcement)
    
    context = {
        'form': form,
        'title': 'Edit Anouncement'
    }

    return render(request, 'announcement/add_announcement.html', context=context)
    

def deleteAnnounce(request, announcement_id):
    announcement = AnnouncementModel.objects.get(pk=announcement_id)
    announcement.is_active = False
    announcement.save()
    print('Deleted --', announcement.id)
    return redirect('view_announcement')