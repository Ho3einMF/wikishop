from django.db import models


class PostManager(models.Manager):

    def get_all_posts(self):
        return self.all()
