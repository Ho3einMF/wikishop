from rest_framework import serializers

from apps.media.models import Media


class MediaDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        exclude = ('id', 'post')
