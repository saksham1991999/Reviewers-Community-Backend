from django.db import models
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class Notification(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="notifications")
    link = models.CharField(max_length=256, blank=True, null=True)
    is_dismissed = models.BooleanField(default=False)
    is_promotional = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Notification, dispatch_uid="send_notification")
def send_notification(sender, instance, **kwargs):
    if not instance.is_dismissed:
        if instance.user:
            group_name = 'notifications_%s' % instance.user.username
        else:
            group_name = 'notifications'
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            group_name, {
                'type': "send_notification",
                'notification_id': instance.id
            }
        )