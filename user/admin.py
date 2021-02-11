from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


def addNewPermission():
    post_content = ContentType.objects.get(app_label='post', model='post')
    per1 = Permission.objects.create(
        codename='view_all_post', name='Can View All Post', content_type=post_content)
    per2 = Permission.objects.create(
        codename='react_post', name='Can React Post', content_type=post_content)
    comment_content = ContentType.objects.get(
        app_label='comment', model='comment')
    per3 = Permission.objects.create(
        codename='react_comment', name='Can React Comment', content_type=comment_content)
    user_content = ContentType.objects.get(
        app_label='user', model='authen_user')
    per4 = Permission.objects.create(
        codename='view_profile', name='Can View Profile', content_type=user_content)


def addNewGroup():
    adminGroup = Group(name='Admin')
    normalGroup = Group(name='NormalUser')
    specialGroup = Group(name='Special')
    adminGroup.save()
    normalGroup.save()
    specialGroup.save()


def addPer2Group():
    adminGroup = Group.objects.get(name='Admin')
    normalGroup = Group.objects.get(name='NormalUser')
    specialGroup = Group.objects.get(name='Special')

    admin_permission = ['add_announcementmodel', 'view_announcementmodel', 'delete_announcementmodel', 'change_announcementmodel',
                        'delete_post', 'view_authen_user', 'add_banuser', 'view_all_post']
    for i in admin_permission:
        permission = Permission.objects.get(codename=i)
        adminGroup.permissions.add(permission)

    normal_permission = ['view_profile', 'add_post', 'view_post', 'delete_post', 'change_post', 'react_post',
                         'react_comment', 'add_comment', 'view_chat', 'view_message', 'add_chat']
    for i in normal_permission:
        permission = Permission.objects.get(codename=i)
        normalGroup.permissions.add(permission)

    permission = Permission.objects.get(codename='view_all_post')
    specialGroup.permissions.add(permission)
    adminGroup.save()
    normalGroup.save()
    specialGroup.save()


try:
    if Group.objects.count() == 0:
        addNewGroup()
        addNewPermission()
        addPer2Group()
except:
    print("An exception occurred")
