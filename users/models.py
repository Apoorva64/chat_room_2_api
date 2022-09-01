from django.contrib.auth.models import AbstractUser
from django.db import models


def get_profile_picture_path(instance, filename):
    return f"/user/{instance.username}/profile_picture/{filename}"


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to=get_profile_picture_path)
