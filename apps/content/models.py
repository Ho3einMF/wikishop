from djongo import models

# Create your models here.
from apps.accounts.models import User
from apps.media.models import Media


class Post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField(max_length=2200)
    price = models.IntegerField(default=0)  # TODO => use DecimalField instead

    # Foreign Key Filed
    publisher = models.ForeignKey(to=User, on_delete=models.PROTECT)

    # Many to Many fields
    media_list = models.ArrayReferenceField(to=Media, on_delete=models.CASCADE)
