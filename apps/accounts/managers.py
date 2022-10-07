from django.contrib.auth.models import UserManager

from knox.models import AuthTokenManager
from rest_framework.generics import get_object_or_404

from apps.accounts.utils import get_session_info


class CustomUserManager(UserManager):

    def prevent_self_user_reference(self, object_id):
        return self.exclude(id=object_id)

    def get_user_by_id(self, user_id):
        return get_object_or_404(self, id=user_id)


class SessionManager(AuthTokenManager):

    def create_session(self, request, token_ttl):

        # get ip, location (country) and device with AuthToken information from knox to save in session model
        ip, location, operating_system, device = get_session_info(request)

        instance, token = self.create(user=request.user, expiry=token_ttl)

        instance.ip = ip
        instance.location = location
        instance.operating_system = operating_system
        instance.device = device

        instance.save()

        return instance, token
