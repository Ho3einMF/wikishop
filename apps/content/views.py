# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.content.models import Post
from apps.content.serializers import PostsListSerializer


class PostListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostsListSerializer

    def get_queryset(self):
        return Post.objects.get_all_posts()
