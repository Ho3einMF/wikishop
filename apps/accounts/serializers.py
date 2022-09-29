from rest_framework import serializers

from apps.accounts.models import User
from apps.media.serializers import MediaSerializer


class UserProfileSerializer(serializers.ModelSerializer):

    avatar = MediaSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'avatar', 'follower', 'following', 'saved_posts')
