# Create your views here.
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.recommend.serializers import ItemRecommendItemSerializer
from apps.recommend.utils import load_model, sample_recommendation, get_top_k_similar_items


class UserRecommendationItem(APIView):

    def get(self, request, *args, **kwargs):
        model = load_model()
        known_positives_items, top_k_items = sample_recommendation(model=model, user_id=self.request.user.id, top_k=5)
        known_positives_items = ItemRecommendItemSerializer(known_positives_items, many=True, read_only=True, context={'request': request})
        top_k_items = ItemRecommendItemSerializer(top_k_items, many=True, read_only=True, context={'request': request})
        return Response({
            'known_positives_items': known_positives_items.data,
            'top_k_items': top_k_items.data
        })


# @method_decorator(queries_counter, name='dispatch')
class ItemRecommendationItem(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemRecommendItemSerializer

    def get_object(self):
        return get_top_k_similar_items(item_id=self.kwargs['item_id'], top_k=5)
