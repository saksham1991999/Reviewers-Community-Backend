from django.shortcuts import render, get_object_or_404, get_list_or_404
from .serializers import UserDetailSerializer, UserListSerializer
from .models import User
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsOwnerOrAdmin
from social.models import Follower, Post


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classes = [IsOwnerOrAdmin]
    serializer_class = UserDetailSerializer

    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated, ], name="Contacts")
    def contacts(self, request, *args, **kwargs):
        phone_numbers = request.data['phone_numbers']
        phone_numbers = list(phone_numbers.strip().strip(",").split(",").replace(" ", "").replace("-", ""))
        users = User.objects.filter(username__in=phone_numbers)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], permission_classes=[IsAuthenticated,], name="User Followers")
    def followers(self, request, *args, **kwargs):
        user = self.get_object()
        followers_id = Follower.objects.filter(user=user).values_list("follower", flat=True)
        users = get_list_or_404(User, id__in=followers_id)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], permission_classes=[IsAuthenticated,], name="User Followers")
    def following(self, request, *args, **kwargs):
        user = self.get_object()
        following_id = Follower.objects.filter(follower=user).values_list("user", flat=True)
        users = get_list_or_404(User, id__in=following_id)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], permission_classes=[IsAuthenticated,], name="User Followers")
    def follow(self, request, *args, **kwargs):
        user = self.get_object()
        follow_qs = Follower.objects.create(user=user, follower=request.user)
        return Response({"success": "User Followed"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], permission_classes=[IsAuthenticated,], name="User Followers")
    def unfollow(self, request, *args, **kwargs):
        user = self.get_object()
        follow_qs = get_object_or_404(Follower, user=user, follower=request.user)
        follow_qs.delete()
        return Response({"success": "User Un-Followed"}, status=status.HTTP_200_OK)


