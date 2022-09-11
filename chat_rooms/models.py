from django.db import models


# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admins = models.ManyToManyField("users.User", related_name="chat_rooms_admin")

    def __str__(self):
        return self.name

