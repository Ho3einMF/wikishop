# Create your views here.
from rest_framework.generics import RetrieveAPIView, CreateAPIView

from apps.content.models import Post
from apps.content.serializers import PostDetailSerializer, PostSendSerializer, ScoreSetSerializer


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'


class PostSendAPIView(CreateAPIView):
    serializer_class = PostSendSerializer


class ScoreSetAPIView(CreateAPIView):
    serializer_class = ScoreSetSerializer
