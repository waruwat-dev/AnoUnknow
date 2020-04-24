from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from django.db import models
from user.models import RandomUser

class Chat(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    random_user1 = models.ForeignKey(
        RandomUser, null=True,
        on_delete=models.DO_NOTHING,
        related_name="random_user1"
    )
    random_user2 = models.ForeignKey(RandomUser,
                                     null=True,
                                     on_delete=models.DO_NOTHING,
                                     related_name="random_user2"
                                     )
    is_active = models.BooleanField(default=True)

    def notify(self):
        notification = {
            'type': 'recieve_group_message',
            'message': {"chat":self.id, "random_user1":self.random_user1.id, "random_user2":self.random_user2.id, "name": self.random_user1.name}
        }
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "{}".format(self.random_user1.user.id), notification)
        async_to_sync(channel_layer.group_send)(
            "{}".format(self.random_user2.user.id), notification)

    def save(self, *args, **kwargs):
        new = self.id
        super(Chat, self).save(*args, **kwargs)
        if new is None:
            self.notify()

    class Meta:
        ordering = ['-create_date']


class Message(models.Model):
    time = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField(null=True)
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    randomUser1 = models.ForeignKey(RandomUser, on_delete=models.DO_NOTHING)

    def notify(self):
        notification = {
            'type': 'recieve_group_message',
            'message': '{}'.format(self.id)
        }

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "{}".format(self.chat_id.random_user1.user.id), notification)
        async_to_sync(channel_layer.group_send)(
            "{}".format(self.chat_id.random_user2.user.id), notification)

    def save(self, *args, **kwargs):
        new = self.id
        super(Message, self).save(*args, **kwargs)
        if new is None:
            self.notify()

    class Meta:
        ordering = ('-time',)
