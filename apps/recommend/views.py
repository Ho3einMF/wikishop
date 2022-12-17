# Create your views here.
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.content.models import Post
from apps.recommend.serializers import ItemRecommendUserSerializer, ItemRecommendItemSerializer
from apps.recommend.tasks import get_item_user_recommend_ids, get_item_item_recommend_ids


# @method_decorator(queries_counter, name='dispatch')
class ItemRecommendUser(RetrieveAPIView):
    serializer_class = ItemRecommendUserSerializer

    def get_object(self):
        known_positives_items_ids, top_k_items_ids = \
            get_item_user_recommend_ids.delay(user_id=self.request.user.id, top_k=5).get()
        known_positive_items = Post.objects.get_posts_by_ids(id_list=known_positives_items_ids)
        top_items = Post.objects.get_posts_by_ids(id_list=top_k_items_ids)
        return known_positive_items, top_items


# @method_decorator(queries_counter, name='dispatch')
class ItemRecommendItem(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemRecommendItemSerializer

    def get_object(self):
        top_k_similar_items_ids = get_item_item_recommend_ids.delay(item_id=self.kwargs['item_id'], top_k=5).get()
        top_k_similar_items = Post.objects.get_posts_by_ids(id_list=top_k_similar_items_ids)
        return top_k_similar_items
