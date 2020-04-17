from django.db import models
from user.models import Admin

# Create your models here.
typeOfAnnouncement = {
    ('01', 'Normal'),
    ('02', 'Warning')
}

class AnnouncementModel(models.Model):
    text =models.TextField()
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False)
    adminId = models.ForeignKey(Admin, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=2, choices=typeOfAnnouncement, default='01')
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['start_time']