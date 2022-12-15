# Create your views here.
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.recommend.serializers import ItemRecommendUserSerializer, ItemRecommendItemSerializer
from apps.recommend.utils import load_model, sample_recommendation, get_top_k_similar_items


# @method_decorator(queries_counter, name='dispatch')
class ItemRecommendUser(RetrieveAPIView):
    serializer_class = ItemRecommendUserSerializer

    def get_object(self):
        model = load_model()
        known_positives_items, top_k_items = sample_recommendation(model=model, user_id=self.request.user.id, top_k=5)
        return known_positives_items, top_k_items


# @method_decorator(queries_counter, name='dispatch')
class ItemRecommendItem(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemRecommendItemSerializer

    def get_object(self):
        return get_top_k_similar_items(item_id=self.kwargs['item_id'], top_k=5)
