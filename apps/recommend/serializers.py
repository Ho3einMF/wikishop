from rest_framework import serializers
from rest_framework.reverse import reverse

from apps.content.models import Post


class ItemRecommendUserSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return {
            'known_positives_items': [
                reverse(viewname='content:post-detail', kwargs={'post_id': item.id}, request=self.context['request'])
                for item in instance[0]
            ],
            'top_k_items': [
                reverse(viewname='content:post-detail', kwargs={'post_id': item.id}, request=self.context['request'])
                for item in instance[1]
            ]
        }

    class Meta:
        model = Post
        fields = '__all__'


class ItemRecommendItemSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return {
            'similar_items': [
                reverse(viewname='content:post-detail', kwargs={'post_id': item.id}, request=self.context['request'])
                for item in instance
            ]
        }

    class Meta:
        model = Post
        fields = '__all__'
