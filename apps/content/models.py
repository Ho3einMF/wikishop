from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField(max_length=2200)
    price = models.IntegerField(default=0)  # TODO => use DecimalField instead

    # Foreign Key Filed
    publishers = models.ForeignKey(to='accounts.User', on_delete=models.PROTECT)

    # Many to Many fields
    media_list = models.ManyToManyField(to='media.Media')

    def __str__(self):
        return self.title


# class Score(models.Model):
#     score = models.IntegerField(choices=SCORE_CHOICES)
#     user = models.ArrayReferenceField(to='accounts.User', on_delete=models.PROTECT, limit_choices_to=1)
#     post = models.ArrayReferenceField(to='content.Post', on_delete=models.PROTECT)

    # def __str__(self):
    #     return f'{self.user.username} : {self.score}'
