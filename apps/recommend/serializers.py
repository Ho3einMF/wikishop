from rest_framework import serializers
from rest_framework.reverse import reverse

from apps.content.models import Post


class UserRecommendationItemSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return reverse(viewname='content:post-detail', kwargs={'post_id': instance.id})

    class Meta:
        model = Post
        fields = '__all__'
