from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def prevent_self_reference(self, object_id):
        return self.exclude(id=object_id)
