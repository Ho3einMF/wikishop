from rest_framework import serializers

from apps.accounts.models import User
from apps.media.serializers import MediaSerializer


class UserProfileSerializer(serializers.ModelSerializer):

    avatar = MediaSerializer(read_only=True)
    follower_count = serializers.ReadOnlyField(source='follower.count')
    following_count = serializers.ReadOnlyField(source='following.count')

    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'avatar', 'follower_count', 'following_count')
