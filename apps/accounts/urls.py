from django.urls import path
from knox.views import LogoutView, LogoutAllView

from apps.accounts.views import LoginView, UserProfileAPIView, UserSignupAPIView, UserFollowersAPIView, \
    UserFollowingsAPIView, UserPostsAPIView, UserSavedPostsAPIView, UserFollowAPIView, UserUnfollowAPIView, \
    UserSessionsListAPIView

app_name = 'accounts'
urlpatterns = [
    path('signup/', UserSignupAPIView.as_view(), name='signup'),

    path(r'login/', LoginView.as_view(), name='login'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
    path(r'logout/all/', LogoutAllView.as_view(), name='logout-all'),
    path('sessions/', UserSessionsListAPIView.as_view(), name='sessions'),

    path('profile/', UserProfileAPIView.as_view(), name='my-profile'),
    path('profile/<int:user_id>/', UserProfileAPIView.as_view(), name='profile'),
    path('followers/<int:user_id>/', UserFollowersAPIView.as_view(), name='followers'),
    path('followings/<int:user_id>/', UserFollowingsAPIView.as_view(), name='followings'),

    path('posts/<int:user_id>/', UserPostsAPIView.as_view(), name='posts'),
    path('saved/posts/', UserSavedPostsAPIView.as_view(), name='saved-posts'),

    path('follow/', UserFollowAPIView.as_view(), name='follow'),
    path('unfollow/', UserUnfollowAPIView.as_view(), name='unfollow'),
]
