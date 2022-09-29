# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.content.models import Post
from apps.content.serializers import PostListSerializer


class PostListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.object.get_all_posts()
