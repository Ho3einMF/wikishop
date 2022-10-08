# Create your views here.
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from apps.content.conf import POST_SEND_SUCCESSFULLY_MESSAGE
from apps.content.models import Post
from apps.content.serializers import PostDetailSerializer, PostSendSerializer


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id'


class PostSendAPIView(APIView):

    @staticmethod
    def post(request):
        serializer = PostSendSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            data = {
                'detail': {
                    'message': POST_SEND_SUCCESSFULLY_MESSAGE,
                    'link': reverse(viewname='content:post-detail',
                                    kwargs={'post_id': serializer.instance.id}, request=request)
                }
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
