from django.urls import path
from knox.views import LogoutView, LogoutAllView

from apps.accounts.views import LoginView, UserProfileAPIView, UserSignupAPIView

app_name = 'accounts'
urlpatterns = [
    path('signup/', UserSignupAPIView.as_view(), name='signup'),

    path(r'login/', LoginView.as_view(), name='login'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
    path(r'logout/all/', LogoutAllView.as_view(), name='logout-all'),

    path('profile/', UserProfileAPIView.as_view(), name='profile')
]
