# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.recommend.serializers import UserRecommendationItemSerializer
from apps.recommend.utils import load_model, sample_recommendation


class UserRecommendationItem(APIView):

    def get(self, request, *args, **kwargs):
        model = load_model()
        known_positives_items, top_k_items = sample_recommendation(model=model, user_id=self.request.user.id, top_k=5)
        known_positives_items = UserRecommendationItemSerializer(known_positives_items, many=True, read_only=True)
        top_k_items = UserRecommendationItemSerializer(top_k_items, many=True, read_only=True)
        return Response({
            'known_positives_items': known_positives_items.data,
            'top_k_items': top_k_items.data
        })
