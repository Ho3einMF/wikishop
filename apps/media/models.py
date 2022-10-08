from django.db import models

# Create your models here.
from apps.media.conf import POSTS_MEDIA_DIRECTORY
from apps.media.managers import MediaManager


class Media(models.Model):
    media = models.FileField(upload_to=POSTS_MEDIA_DIRECTORY)
    blurhash = models.CharField(max_length=200)
    post = models.ForeignKey('content.Post', on_delete=models.CASCADE, related_name='media_list')

    objects = MediaManager()
