from django.urls import path

from apps.content.views import PostDetailAPIView, PostSendAPIView

app_name = 'content'
urlpatterns = [
    path('post/<int:post_id>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('post/send/', PostSendAPIView.as_view(), name='post-send'),
]
