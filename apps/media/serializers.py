from rest_framework import serializers

from apps.media.models import Media


class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        exclude = ('id',)
