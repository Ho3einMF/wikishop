from django.urls import path
from knox.views import LogoutView, LogoutAllView

from apps.accounts.views import LoginView, UserProfileAPIView, UserSignupAPIView, UserFollowersAPIView, \
    UserFollowingsAPIView, UserPostsAPIView

app_name = 'accounts'
urlpatterns = [
    path('signup/', UserSignupAPIView.as_view(), name='signup'),

    path(r'login/', LoginView.as_view(), name='login'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
    path(r'logout/all/', LogoutAllView.as_view(), name='logout-all'),

    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('followers/', UserFollowersAPIView.as_view(), name='followers'),
    path('followings/', UserFollowingsAPIView.as_view(), name='followings'),
    path('<int:user_id>/posts/', UserPostsAPIView.as_view(), name='posts'),
]
