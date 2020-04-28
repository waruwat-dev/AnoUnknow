import datetime
from datetime import datetime as dtm
from django.forms.models import model_to_dict

from announcement.serializers import AnnouncementSerializer
from django.contrib.auth.decorators import permission_required, login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from announcement.serializers import AnnouncementSerializer
from user.models import Authen_User

from .form import AnnouncementForm
from .models import AnnouncementModel, typeOfAnnouncement

@login_required(login_url='login')
@permission_required('announcement.view_announcementmodel', raise_exception=True)
def viewAnnounce(request):
    announcements = AnnouncementModel.objects.filter(is_active=True)
    typeDict = {t[0]: t[1] for t in typeOfAnnouncement}
    for announcement in announcements:
        announcement.type = typeDict[announcement.type]
    context = {
        'announcements': announcements
    }

    return render(request, 'announcement/view_announcement.html', context=context)

@login_required(login_url='login')
@permission_required('announcement.add_announcementmodel', raise_exception=True)
def announce(request):
    admin = request.user.authen_user.getAdmin()

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            object_announce = form.save()
            object_announce.adminId = admin
            object_announce.save()
            print('Create Announcement --', admin.user.username)
            return redirect('view_announcement')
        else:
            form = AnnouncementForm(request.POST)
    else:
        form = AnnouncementForm()
    
    context = {
        'form': form,
        'title': 'Add Anouncement'
    }

    return render(request, 'announcement/add_announcement.html', context=context)

@login_required(login_url='login')
@permission_required('announcement.change_announcementmodel', raise_exception=True)
def editAnnounce(request, announcement_id):
    admin = request.user.authen_user.getAdmin()
    announcement = AnnouncementModel.objects.get(pk=announcement_id)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            object_announce = form.save()
            object_announce.adminId = admin
            object_announce.save()
            print('Edit Announcement --', admin.user.username)
            return redirect('view_announcement')
        else:
            form = AnnouncementForm(request.POST, instance=announcement)
    else:
        form = AnnouncementForm(instance=announcement)
    
    context = {
        'form': form,
        'title': 'Edit Anouncement'
    }

    return render(request, 'announcement/add_announcement.html', context=context)
    
@login_required(login_url='login')
@permission_required('announcement.delete_announcementmodel', raise_exception=True)
def deleteAnnounce(request, announcement_id):
    announcement = AnnouncementModel.objects.get(pk=announcement_id)
    announcement.is_active = False
    announcement.save()
    print('Deleted --', announcement.id)
    return redirect('view_announcement')

def getAnnounceJSON(request):
    now = datetime.datetime.now()
    announces = AnnouncementModel.objects.filter(start_time__lte=now, end_time__gt=now, is_active=True)
    json_obj =  AnnouncementSerializer(announces, many=True)
    return JsonResponse(json_obj.data, safe=False)