# Create your views here.
from rest_framework.generics import RetrieveAPIView

from apps.content.models import Post
from apps.content.serializers import PostDetailSerializer


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'
