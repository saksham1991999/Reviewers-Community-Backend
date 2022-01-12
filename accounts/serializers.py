from rest_framework import serializers
from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
import random

from .models import User


class CustomRegisterSerializer(RegisterSerializer):
    referral_code = serializers.CharField(allow_blank=True, allow_null=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField(allow_blank=True, allow_null=True)
    email = serializers.EmailField(allow_blank=True, allow_null=True)
    profile_pic = serializers.ImageField()
    gender = serializers.CharField()
    city = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'profile_pic', 'gender', 'city')

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'profile_pic': self.validated_data.get('profile_pic', ''),
            'gender': self.validated_data.get('gender', ''),
            'city': self.validated_data.get('city', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.save()
        adapter.save_user(request, user, self)
        return user


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    profile_pic = serializers.SerializerMethodField(read_only=True)
    first_name = serializers.SerializerMethodField(read_only=True)
    last_name = serializers.SerializerMethodField(read_only=True)
    is_mediator = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Token
        fields = ('key', 'user', 'username', 'profile_pic', 'first_name', 'last_name')

    def get_username(self, obj):
        return obj.user.username

    def get_profile_pic(self, obj):
        if obj.user.profile_pic:
            return obj.user.profile_pic.url
        return None

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_is_mediator(self, obj):
        return obj.user.is_mediator


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            "profile_pic",
            "gender",
            "is_mediator",
            "city",
            "verified",
            "whatsapp",
            "verified_by",
            "active",
        )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            "profile_pic",
            "gender",
            "is_mediator",
            "city",
            "verified",
            "whatsapp",
            "verified_by",
            "active",
        )