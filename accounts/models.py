from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .choices import GENDER_CHOICES, USER_TYPE_CHOICES


class User(AbstractUser):
    whatsapp = models.CharField(max_length=15)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    profile_pic = models.ImageField(upload_to="user-profile-pics", blank=True, null=True)
    city = models.CharField(max_length=64)
    is_mediator = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True, blank=True)

