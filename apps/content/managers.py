from django.db import models


class PostManager(models.Manager):

    def prevent_self_post_reference(self, user_id):
        return self.exclude(publisher__id=user_id)

    def get_posts_by_ids(self, id_list):
        dict_objs = self.objects.in_bulk(id_list=id_list)
        return [dict_objs[key_id] for key_id in id_list]
