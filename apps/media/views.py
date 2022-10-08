# Create your views here.
from rest_framework.generics import RetrieveAPIView

from apps.media.models import Media
from apps.media.serializers import MediaDetailSerializer


class MediaDetailAPIView(RetrieveAPIView):
    serializer_class = MediaDetailSerializer
    queryset = Media.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'media_id'
