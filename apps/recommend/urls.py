from django.urls import path

from apps.recommend.views import UserRecommendationItem, ItemRecommendationItem

app_name = 'recommend'
urlpatterns = [
    path('user/', UserRecommendationItem.as_view(), name='user-item'),
    path('item/<int:item_id>/', ItemRecommendationItem.as_view(), name='item-item'),
]
