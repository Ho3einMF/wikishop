from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models
from knox.models import AuthToken

from apps.accounts.managers import CustomUserManager, SessionManager


class User(AbstractUser):
    bio = models.TextField(max_length=150, blank=True, null=True)
    avatar = models.ForeignKey(to='media.Media', blank=True, null=True, on_delete=models.PROTECT)

    # Many to Many fields
    follower = models.ManyToManyField(to='User', related_name='followers')
    following = models.ManyToManyField(to='User', related_name='followings')
    saved_posts = models.ManyToManyField(to='content.Post', related_name='users_that_saved')

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Session(AuthToken):

    # extra fields
    ip = models.GenericIPAddressField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    operating_system = models.CharField(max_length=100, null=True, blank=True)
    device = models.CharField(max_length=100, null=True, blank=True)

    objects = SessionManager()

    def __str__(self):
        return f'username : {self.user.username}'
