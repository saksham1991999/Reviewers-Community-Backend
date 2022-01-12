from django.db import models

from .choices import PLATFORM_CHOICES, REVIEW_TYPE_CHOICES


class Product(models.Model):
    user = models.ForeignKey('accounts.User', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256)
    url = models.URLField(null=True, blank=True)
    price = models.PositiveIntegerField()
    refund = models.PositiveIntegerField()
    description = models.TextField()
    platform = models.CharField(max_length=64, choices=PLATFORM_CHOICES)
    review_type = models.CharField(max_length=64, choices=REVIEW_TYPE_CHOICES)
    image = models.ImageField(null=True, blank=True)
    mediator_only = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
