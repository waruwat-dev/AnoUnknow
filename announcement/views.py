import datetime
from datetime import datetime as dtm
from django.forms.models import model_to_dict

from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from announcement.serializers import AnnouncementSerializer
from user.models import Authen_User

from .form import AnnouncementForm
from .models import AnnouncementModel, typeOfAnnouncement


@permission_required('announcement.view_announcement')
def viewAnnounce(request):
    announcements = AnnouncementModel.objects.filter(is_active=True)
    typeDict = {t[0]: t[1] for t in typeOfAnnouncement}
    for announcement in announcements:
        announcement.type = typeDict[announcement.type]
    context = {
        'announcements': announcements
    }

    return render(request, 'announcement/view_announcement.html', context=context)

@permission_required('announcement.add_announcement')
def announce(request):
    admin = request.user.authen_user.getAdmin()

    if request.method == 'POST':
        data = localToDate(dict(request.POST), ['start_time', 'end_time'])
        form = AnnouncementForm(data)
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

@permission_required('announcement.change_announcement')
def editAnnounce(request, announcement_id):
    admin = request.user.authen_user.getAdmin()
    announcement = AnnouncementModel.objects.get(pk=announcement_id)
    # announcement = dateTolocal(model_to_dict(announcement), ['start_time', 'end_time'])
    if request.method == 'POST':
        data = localToDate(dict(request.POST), ['start_time', 'end_time'])
        form = AnnouncementForm(data, instance=announcement)
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
    

@permission_required('announcement.delete_announcement')
def deleteAnnounce(request, announcement_id):
    announcement = AnnouncementModel.objects.get(pk=announcement_id)
    announcement.is_active = False
    announcement.save()
    print('Deleted --', announcement.id)
    return redirect('view_announcement')

def getAnnounceJSON(request):
    now = datetime.datetime.now()
    announces = AnnouncementModel.objects.filter(start_time__lte=now, end_time__gt=now)
    json_obj =  AnnouncementSerializer(announces, many=True)
    return JsonResponse(json_obj.data, safe=False)

def localToDate(data, change):
    new_data = dict()
    for k, v in data.items():
        new_data[k] = v[0]

    for name in change:
        new_data[name] = new_data[name].replace('T', ' ')
    return new_data

def dateTolocal(data, change):
    for name in change:
        data[name] = data[name].strftime("%Y/%m/%d %H:%M:%S").replace(' ', 'T')
    return data