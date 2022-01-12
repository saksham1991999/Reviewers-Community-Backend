from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    is_dismissible = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Notification
        fields = [
            "id",
            "title",
            "title_hi",
            "description",
            "description_hi",
            "image",
            "link",
            "datetime",
            "is_dismissible",
            "is_promotional",
        ]

    def get_is_dismissible(self, obj):
        request = self.context.get('request', None)
        if request:
            if obj.user == request.user:
                return True
        return False
