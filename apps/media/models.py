from django.db import models

import blurhash

# Create your models here.
from apps.media.conf import POSTS_IMAGES_DIRECTORY


class Media(models.Model):
    image = models.ImageField(upload_to=POSTS_IMAGES_DIRECTORY)
    blurhash = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.blurhash = blurhash.encode(self.image, x_components=4, y_components=3)
        super(Media, self).save(*args, **kwargs)
