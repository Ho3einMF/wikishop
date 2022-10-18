from django.contrib.auth.backends import BaseBackend

from apps.accounts.models import User


class EmailAuthBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        if 'email' in kwargs:
            email = kwargs['email']
            password = kwargs['password']

            try:
                user = User.objects.get(email=email)
                if user.check_password(password) is True:
                    return user
            except User.DoesNotExist:
                return None
        return None
