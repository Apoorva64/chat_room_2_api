from rest_framework import serializers
from .models import Message
from users.serializers import UserSerializer
from chat_rooms.serializers import ChatRoomSerializer


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    # chat_room = ChatRoomSerializer(read_only=True)

    class Meta:
        model = Message
        fields = "__all__"
