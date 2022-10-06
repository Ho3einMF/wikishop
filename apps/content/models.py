from django.db import models

# Create your models here.
from apps.content.conf import SCORE_CHOICES

from django.db.models import Avg

from apps.content.managers import PostManager


class Post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField(max_length=2200)
    price = models.IntegerField(default=0)  # TODO => use DecimalField instead

    # Foreign Key Filed
    publisher = models.ForeignKey(to='accounts.User', on_delete=models.PROTECT, related_name='posts')

    # Many to Many fields
    media_list = models.ManyToManyField(to='media.Media')

    objects = PostManager()

    @property
    def score_average(self):
        return self.scores.aggregate(score_average=Avg('score'))['score_average']

    def __str__(self):
        return self.title


class Score(models.Model):
    score = models.IntegerField(choices=SCORE_CHOICES)
    user = models.ForeignKey(to='accounts.User', on_delete=models.PROTECT)
    post = models.ForeignKey(to='content.Post', on_delete=models.PROTECT, related_name='scores')

    def __str__(self):
        return f'{self.user.username} : {self.score}'
