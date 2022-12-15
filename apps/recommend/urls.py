from django.urls import path

from apps.recommend.views import ItemRecommendUser, ItemRecommendItem

app_name = 'recommend'
urlpatterns = [
    path('user/', ItemRecommendUser.as_view(), name='user-item'),
    path('item/<int:item_id>/', ItemRecommendItem.as_view(), name='item-item'),
]
