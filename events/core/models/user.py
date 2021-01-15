import os
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


def make_path(_, filename):
    filename_ext = os.path.splitext(filename)

    return f"{uuid4().hex}.{filename_ext}"


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    profile_picture = models.ImageField(null=True, blank=True, upload_to=make_path)

    REQUIRED_FIELDS = ["username", "city", "state", "first_name", "last_name"]
    USERNAME_FIELD = "email"