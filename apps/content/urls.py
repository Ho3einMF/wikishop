from django.urls import path

from apps.content.views import PostDetailAPIView

app_name = 'content'
urlpatterns = [
    path('post/<int:post_id>/', PostDetailAPIView.as_view(), name='post-detail')
]
