from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):

    def prevent_self_reference(self, object_id):
        return self.exclude(id=object_id)
