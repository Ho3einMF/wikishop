from django.contrib.auth.models import AbstractUser

# Create your models here.
from djongo import models

from apps.accounts.managers import UserManager
from apps.media.models import Media


class User(AbstractUser):

    bio = models.TextField(max_length=150, blank=True, null=True)
    avatar = models.EmbeddedField(model_container=Media, blank=True, null=True)
    follower = models.ArrayReferenceField(to='User', on_delete=models.PROTECT, related_name='followers')
    following = models.ArrayReferenceField(to='User', on_delete=models.PROTECT, related_name='followings')
    # TODO saved_posts = models.ArrayReferenceField(to='Post', on_delete=models.PROTECT)

    objects = UserManager()

    def __str__(self):
        return self.username
