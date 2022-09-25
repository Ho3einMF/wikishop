from django.contrib.auth.models import AbstractUser

# Create your models here.
from djongo import models

from apps.accounts.managers import UserManager
from apps.media.models import Media


class User(AbstractUser):
    bio = models.TextField(max_length=150, blank=True, null=True)
    avatar = models.ForeignKey(Media, on_delete=models.CASCADE, blank=True, null=True)
    follower = models.ArrayReferenceField(to='User', on_delete=models.PROTECT, related_name='followers')
    following = models.ArrayReferenceField(to='User', on_delete=models.PROTECT, related_name='followings')
    saved_posts = models.ArrayReferenceField(to='content.Post', on_delete=models.CASCADE,
                                             null=True, blank=True, related_name='saved_posts')

    objects = UserManager()

    def __str__(self):
        return self.username
