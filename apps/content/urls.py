from django.urls import path

from apps.content.views import PostListAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='posts-list')
]
