from django.contrib.auth.models import UserManager
from django.utils import timezone

from knox.models import AuthTokenManager
from rest_framework.generics import get_object_or_404

from apps.accounts.utils import get_session_info


class CustomUserManager(UserManager):

    def prevent_self_user_reference(self, object_id):
        return self.exclude(id=object_id)

    def get_user_by_id(self, user_id):
        return get_object_or_404(self, id=user_id)

    def follow_user(self, requesting_user, target_user_id):
        self.get_user_by_id(target_user_id).followers.add(requesting_user)

    def unfollow_user(self, requesting_user, target_user_id):
        self.get_user_by_id(target_user_id).followers.remove(requesting_user)


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

    def get_user_sessions(self, user_id):
        return self.filter(user_id=user_id)

    def clean_expired_sessions(self):
        self.filter(expiry__lt=timezone.now()).delete()
