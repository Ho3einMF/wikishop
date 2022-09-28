from django.urls import path
from knox.views import LogoutView, LogoutAllView

from apps.accounts.views import LoginView

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='login'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
    path(r'logout/all/', LogoutAllView.as_view(), name='logout-all'),
]
