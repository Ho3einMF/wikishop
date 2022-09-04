from django.db import models

# Create your models here.


class Media(models.Model):
    url = models.URLField(max_length=200)
    blurhash = models.CharField(max_length=200)
    aspect_ratio = models.FloatField()
