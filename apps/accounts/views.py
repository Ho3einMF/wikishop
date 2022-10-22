from django.contrib.auth import login, user_logged_in

# Create your views here.
from django.http import Http404
from django.utils import timezone
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.conf import FOLLOW_MESSAGE, USER_NOT_FOUND_ERROR, UNFOLLOW_MESSAGE
from apps.accounts.models import Session, User
from apps.accounts.serializers import UserProfileSerializer, UserSignupSerializer, UserFollowersSerializer, \
    UserFollowingsSerializer, UserPostsSerializer, UserSavedPostsSerializer, UserSessionsSerializer, UserLoginSerializer


class UserSignupAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSignupSerializer


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        token_limit_per_user = self.get_token_limit_per_user()
        if token_limit_per_user is not None:
            now = timezone.now()
            token = request.user.auth_token_set.filter(expiry__gt=now)
            if token.count() >= token_limit_per_user:
                return Response(
                    {"error": "Maximum amount of tokens allowed per user exceeded."},
                    status=status.HTTP_403_FORBIDDEN
                )
        token_ttl = self.get_token_ttl()

        # Difference with package
        instance, token = Session.objects.create_session(request, token_ttl)

        user_logged_in.send(sender=request.user.__class__,
                            request=request, user=request.user)
        data = self.get_post_response_data(request, token, instance)
        return Response(data)


class UserSessionsListAPIView(ListAPIView):
    serializer_class = UserSessionsSerializer

    def get_queryset(self):
        return Session.objects.get_user_sessions(user_id=self.request.user.id)


class UserProfileAPIView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    def get_object(self):
        if 'user_id' in self.kwargs:
            return User.objects.get_user_by_id(self.kwargs['user_id'])
        return User.objects.get_user_by_id(self.request.user.id)


class UserFollowersAPIView(RetrieveAPIView):
    serializer_class = UserFollowersSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'


class UserFollowingsAPIView(RetrieveAPIView):
    serializer_class = UserFollowingsSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'


class UserPostsAPIView(RetrieveAPIView):
    serializer_class = UserPostsSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'


class UserSavedPostsAPIView(RetrieveAPIView):
    serializer_class = UserSavedPostsSerializer

    def get_object(self):
        return User.objects.get_user_by_id(self.request.user.id)


class UserFollowAPIView(APIView):

    @staticmethod
    def patch(request, *args, **kwargs):
        try:
            User.objects.follow_user(requesting_user=request.user,
                                     target_user_id=request.data['target_user_id'])
            return Response(data={'detail': FOLLOW_MESSAGE}, status=status.HTTP_200_OK)
        except Http404:
            return Response(data={'detail': USER_NOT_FOUND_ERROR}, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(data={'target_user_id': 'This field is required'}, status=status.HTTP_400_BAD_REQUEST)


class UserUnfollowAPIView(APIView):

    @staticmethod
    def patch(request, *args, **kwargs):
        try:
            User.objects.unfollow_user(requesting_user=request.user,
                                       target_user_id=request.data['target_user_id'])
            return Response(data={'detail': UNFOLLOW_MESSAGE}, status=status.HTTP_200_OK)
        except Http404:
            return Response(data={'detail': USER_NOT_FOUND_ERROR}, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(data={'target_user_id': 'This field is required'}, status=status.HTTP_400_BAD_REQUEST)
