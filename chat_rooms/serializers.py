from rest_framework import serializers
from .models import ChatRoom
from users.serializers import UserSerializer


class ChatRoomSerializer(serializers.ModelSerializer):
    admins = UserSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = "__all__"
