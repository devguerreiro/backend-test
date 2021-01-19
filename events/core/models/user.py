import os
from uuid import uuid4

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


def make_path(_, filename):  # pragma: no cover -> no complexity
    filename_ext = os.path.splitext(filename)

    return f"{uuid4().hex}.{filename_ext}"


class CustomUserQuerySet(models.QuerySet):
    def user_by_id(self, id):
        return self.get(pk=id)

    def all_friends(self, user):
        return self.user_by_id(user.id).friends.all()

    def all_invitations_of_type(self, user, invitation_type):
        return self.user_by_id(user.id).invitations_received.filter(type=invitation_type)

    def remove_friend(self, user, friend):
        return self.user_by_id(user.id).friends.remove(friend)

    def is_unregistered(self, email):
        return not self.filter(email=email).exists()


class CustomUserManager(UserManager):
    def get_queryset(self):
        return CustomUserQuerySet(self.model, using=self._db)

    def get_all_friends(self, user):
        return self.get_queryset().all_friends(user)

    def get_all_invitations_of_type(self, user, invitation_type):
        return self.get_queryset().all_invitations_of_type(user, invitation_type)

    def remove_friend(self, user, friend):
        return self.get_queryset().remove_friend(user, friend)

    def is_unregistered(self, email):
        return self.get_queryset().is_unregistered(email)


class CustomUser(AbstractUser):
    """
    User model that has the following attributes:
        - email
        - username
        - first_name
        - last_name
        - city
        - state
        - password
        - bio
        - profile_picture
        - friends

    REQUIRED_FIELDS = ["username", "first_name", "last_name", "city", "state"]
    USERNAME_FIELD = "email"
    """

    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    profile_picture = models.ImageField(null=True, blank=True, upload_to=make_path)
    friends = models.ManyToManyField("CustomUser", through="Friendship")

    REQUIRED_FIELDS = ["username", "first_name", "last_name", "city", "state"]
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    class Meta:
        ordering = ["first_name", "last_name"]


class Friendship(models.Model):
    """
    Friendship model that has the following attributes:
        - user1
        - user2
        - created_at
    """

    user1 = models.ForeignKey(
        "CustomUser", related_name="friendships1", related_query_name="friendship1", on_delete=models.CASCADE
    )
    user2 = models.ForeignKey(
        "CustomUser", related_name="friendships2", related_query_name="friendship2", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user1_id", "user2_id"]
