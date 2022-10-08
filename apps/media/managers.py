import blurhash
from django.db import models


class MediaManager(models.Manager):

    @staticmethod
    def generate_blurhash(media):
        return blurhash.encode(media, x_components=4, y_components=3)
