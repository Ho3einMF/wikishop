from django.contrib.auth import login, user_logged_in

# Create your views here.
from django.utils import timezone
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.conf import USER_CREATION_SUCCESSFUL_MESSAGE
from apps.accounts.models import Session, User
from apps.accounts.serializers import UserProfileSerializer, UserSignupSerializer, UserFollowersSerializer, \
    UserFollowingsSerializer, UserPostsSerializer


class UserSignupAPIView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'details': USER_CREATION_SUCCESSFUL_MESSAGE}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
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


class UserProfileAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

    @staticmethod
    def get(request, *args, **kwargs):
        serializer = UserProfileSerializer(request.user, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserFollowersAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserFollowersSerializer

    def get_queryset(self):
        return User.objects.get_user(self.request.user.id)


class UserFollowingsAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserFollowingsSerializer

    def get_queryset(self):
        return User.objects.get_user(self.request.user.id)


class UserPostsAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPostsSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'
