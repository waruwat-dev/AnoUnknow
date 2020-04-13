from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import random

class Admin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)


class RandomUserModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255, default='')


class BanUserModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    ban_date = models.DateField(null=True, default=datetime.now())
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
        return RandomUserModel.objects.create(name=randomlist[0], user=self.user)

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
            Admin.objects.create(user=self.user)
            self.save()
        else:
            admin = Admin.objects.get(pk=self.user.id)
            admin.delete()

    def getBan(self):
        if self.ban_user:
            return BanUserModel.objects.get(pk=self.user.id)
        else:
            return None

    def ban(self, admin, val=True, remark=""):
        if val == self.ban_user:
            return
        if val == True:
            self.ban_user = True
            BanUserModel.objects.create(user=self.user, remark=remark, admin=admin)
            self.save()
        else:
            ban_user = BanUserModel.objects.get(pk=self.user.id)
            ban_user.delete()


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):  # create_normal_user
    if created:
        Authen_User.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):  # admin >> is_superuser, ban_user >> is_active
    instance.authen_user.save()
