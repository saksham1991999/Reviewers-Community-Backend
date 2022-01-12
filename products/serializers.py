from django.db.models import Q
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Product
        fields = "__all__"

