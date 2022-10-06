from rest_framework import serializers

from apps.content.models import Post
from apps.media.serializers import MediaSerializer


class PostDetailSerializer(serializers.ModelSerializer):

    publisher = serializers.ReadOnlyField(source='publisher.username')
    media_list = MediaSerializer(many=True, read_only=True)
    score_average = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'
