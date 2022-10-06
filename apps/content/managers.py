from django.db import models


class PostManager(models.Manager):

    def prevent_self_post_reference(self, user_id):
        return self.exclude(publisher__id=user_id)
