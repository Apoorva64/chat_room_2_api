from django.db import models


# Create your models here.

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    chat_room = models.ForeignKey("chat_rooms.ChatRoom", related_name="messages", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", related_name="messages", on_delete=models.CASCADE)
    edited = models.BooleanField(default=False)
    seen_by = models.ManyToManyField("users.User", related_name="seen_messages")

    def __str__(self):
        return self.content
