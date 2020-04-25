from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.utils.timezone import now
import random
from django.contrib.auth.models import Group


class Admin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)


class NormalUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0, null=True)


# class RandomUserModel(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, default='', null=True)

class RandomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='', null=True)


class BanUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    # .DaField(null=True, default=now())
    ban_date = models.DateTimeField(null=True, auto_now_add=True)
    remark = models.TextField(null=True)
    admin = models.ForeignKey(Admin, on_delete=models.DO_NOTHING)


class Authen_User(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    normal_user = models.BooleanField(default=True)
    ban_user = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    def randomName(self):
        randomlist = ['A', 'B', 'C', 'D']
        random.shuffle(randomlist)
        return RandomUser.objects.create(name=randomlist[0], user=self.user)

    def getNormalUser(self):
        if self.normal_user:
            return NormalUser.objects.get(pk=self.user.id)
        else:
            return None

    def getAdmin(self):
        if self.admin:
            return Admin.objects.get(pk=self.user.id)
        else:
            return None

    def setAdmin(self, val=True):
        if val == self.admin:
            return
        if val == True:
            self.admin = True
            self.normal_user = False
            Admin.objects.create(user=self.user)
            my_group = Group.objects.get(name='NormalUser') 
            my_group.user_set.remove(self.user)
            my_group = Group.objects.get(name='Admin') 
            my_group.user_set.add(self.user)
            # my_group = Group.objects.get(name='Special') 
            # my_group.user_set.add(self.user)
            self.save()
        else:
            admin = Admin.objects.get(pk=self.user.id)
            admin.delete()

    def getBan(self):
        if self.ban_user:
            return BanUser.objects.get(pk=self.user.id)
        else:
            return None

    def ban(self, admin, val=True, remark=""):
        # if val == self.ban_user:
        #     return
        if val == True:
            self.ban_user = True
            self.normal_user = False
            BanUser.objects.create(
                user=self.user, remark=remark, admin=admin)
            self.save()
        else:
            ban_user = BanUser.objects.get(pk=self.user.id)
            ban_user.delete()


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):  # create_normal_user
    if created:
        Authen_User.objects.create(user=instance)
        NormalUser.objects.create(user=instance)
        my_group = Group.objects.get(name='NormalUser') 
        my_group.user_set.add(instance)


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):  # admin >> is_superuser, ban_user >> is_active
    instance.authen_user.save()
