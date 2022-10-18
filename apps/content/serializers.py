from rest_framework import serializers
from rest_framework.reverse import reverse

from apps.content.conf import SCORE_CREATION_SUCCESSFULLY_MESSAGE, POST_SEND_SUCCESSFULLY_MESSAGE
from apps.content.models import Post, Score
from apps.media.models import Media
from apps.media.serializers import MediaDetailSerializer


class PostDetailSerializer(serializers.ModelSerializer):

    publisher = serializers.ReadOnlyField(source='publisher.username')
    media_list = MediaDetailSerializer(many=True, read_only=True)
    score_average = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'


class PostSendSerializer(serializers.ModelSerializer):

    media_list = serializers.ListField(child=serializers.FileField())

    class Meta:
        model = Post
        exclude = ('publisher',)

    def create(self, validated_data):
        media_list = validated_data.pop('media_list')
        post = Post.objects.create(publisher=self.context['request'].user, **validated_data)
        Media.objects.bulk_create([
            Media(media=media, blurhash=Media.objects.generate_blurhash(media), post=post)
            for media in media_list
        ])
        return post

    def to_representation(self, instance):
        return {
            'detail': {
                'message': POST_SEND_SUCCESSFULLY_MESSAGE,
                'link': reverse(viewname='content:post-detail',
                                kwargs={'post_id': instance.id}, request=self.context['request'])
            }
        }


class ScoreSetSerializer(serializers.ModelSerializer):

    target_post_id = serializers.CharField(source='post')

    class Meta:
        model = Score
        exclude = ('user', 'post')

    def create(self, validated_data):
        score = Score.objects.create(score=validated_data['score'],
                                     user=self.context['request'].user,
                                     post_id=validated_data['post'])
        return score

    def to_representation(self, instance):
        return {
            'detail': {
                'message': SCORE_CREATION_SUCCESSFULLY_MESSAGE,
                'your_score': instance.score,
                'link': reverse(viewname='content:post-detail',
                                kwargs={'post_id': instance.post.id}, request=self.context['request'])
            }
        }
