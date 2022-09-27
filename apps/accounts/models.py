from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models

from apps.accounts.managers import CustomUserManager


class User(AbstractUser):
    bio = models.TextField(max_length=150, blank=True, null=True)
    avatar = models.ForeignKey(to='media.Media', blank=True, null=True, on_delete=models.PROTECT)

    # Many to Many fields
    follower = models.ManyToManyField(to='User', related_name='followers')
    following = models.ManyToManyField(to='User', related_name='followings')
    saved_posts = models.ManyToManyField(to='content.Post', related_name='saved_posts')

    objects = CustomUserManager()

    def __str__(self):
        return self.username
