from rest_framework import serializers

from apps.accounts.models import User
from apps.accounts.utils import check_password_confirmation
from apps.media.serializers import MediaSerializer


class UserSignupSerializer(serializers.ModelSerializer):

    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation')

    def validate_password_confirmation(self, value):
        return check_password_confirmation(self.initial_data['password'], value)

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'], password=validated_data['password'])


class UserProfileSerializer(serializers.ModelSerializer):

    avatar = MediaSerializer(read_only=True)
    follower_count = serializers.ReadOnlyField(source='follower.count')
    following_count = serializers.ReadOnlyField(source='following.count')

    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'avatar', 'follower_count', 'following_count')
