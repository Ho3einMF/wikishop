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
    followers_count = serializers.ReadOnlyField(source='follower.count')
    followings_count = serializers.ReadOnlyField(source='following.count')

    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'avatar', 'followers_count', 'followings_count')


class UsersListSerializer(serializers.ModelSerializer):

    profile = serializers.HyperlinkedIdentityField(read_only=True, view_name='accounts:profile',
                                                   lookup_field='id', lookup_url_kwarg='user_id')
    avatar = MediaSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('profile', 'avatar')


class UserFollowersSerializer(serializers.ModelSerializer):

    followers = UsersListSerializer(source='follower', read_only=True, many=True)

    class Meta:
        model = User
        fields = ('followers',)


class UserFollowingsSerializer(serializers.ModelSerializer):

    followings = UsersListSerializer(source='following', read_only=True, many=True)

    class Meta:
        model = User
        fields = ('followings',)


class UserPostsSerializer(serializers.ModelSerializer):

    posts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='content:post-detail',
                                                lookup_field='id', lookup_url_kwarg='post_id')

    class Meta:
        model = User
        fields = ('posts',)


class UserSavedPostsSerializer(serializers.ModelSerializer):

    saved_posts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='content:post-detail',
                                                      lookup_field='id', lookup_url_kwarg='post_id')

    class Meta:
        model = User
        fields = ('saved_posts',)
