from rest_framework import serializers
from rest_framework.reverse import reverse

from apps.content.models import Post


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
